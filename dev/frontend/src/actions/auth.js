import {LOGOUT_SUCCESS,USER_LOADED,
    USER_LOADING,AUTH_ERROR,LOGIN_USER,
    REGISTER_SUCCESS, 
    LOGIN_SUCCESS } from './types'
import axios from 'axios'

export const register = ({username,password,email,bio}) => dispatch => {
    const config = {
        headers:{
            'Content-Type':'application/json'
        }
    }
    // const  body = JSON.stringify({username,password,email,bio})
    const  body = {username,password,email,bio}
    axios
        .post('/auth/register/',body,config)
        .then(res => {
            dispatch({
                type:REGISTER_SUCCESS,
                payload:res.data
            })
        })
        .catch(err => console.log(err))
    
}
export const loadUser = () => (dispatch,getState) => {
    dispatch({type:USER_LOADING})    
    axios.get('/auth/user/',tokenConfig(getState))
         .then(res => {
             dispatch({
                 type:USER_LOADED,
                 payload:res.data
             })
         })
         .catch(err => console.log(err))
}
export const login = (username,password) => dispatch => {

    //Headers
    const config = {
        headers:{
            'Content-Type':'application/json'
        }
    }
    const  body = JSON.stringify({username,password})
    axios.post('/auth/login/',body,config)
         .then(res => {
             dispatch({
                 type:LOGIN_SUCCESS,
                 payload:res.data
             })
         })
         .catch(err => console.log(err))
}
//LOGOUT
export const logout = () => (dispatch,getState) => {
    axios.post('/auth/logout/',null,tokenConfig(getState))
         .then(res => {
             dispatch({
                 type:LOGOUT_SUCCESS
             })
         })
         .catch(err => console.log(err))
}

export const tokenConfig = getState => {
    //GET token
    const token = getState().auth.token;

    //Headers
    const config = {
        headers:{
            'Content-Type':'application/json'
        }
    }
    if(token){
        config.headers['Authorization'] = `Token ${token}`
    }
    return config
}