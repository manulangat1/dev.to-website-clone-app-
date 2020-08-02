import {LOGIN_SUCCESS,LOGIN_FAIL,USER_LOADED,
    USER_LOADING,AUTH_ERROR,LOGIN_USER,
    REGISTER_SUCCESS,
    LOGOUT_SUCCESS } from '../actions/types'

const intialState = {
    token:localStorage.getItem('token'),
    isAuthenticated:null,
    isLoading:false,
    user:null
}

export default function(state=intialState,action){
    switch(action.type){
        case LOGIN_SUCCESS:
            case REGISTER_SUCCESS:
            case REGISTER_RIDER:
                localStorage.setItem('token',action.payload.token)
                return{
                    ...state,
                    ...action.payload,
                    isAuthenticated:true,
                    isLoading:false
                }
            case USER_LOADING:
                return{
                    ...state,
                    isLoading:true
                }
            case USER_LOADED:
                return{
                    ...state,
                    isAuthenticated:true,
                    isLoading:false,
                    user:action.payload
                }
            case AUTH_ERROR:
            case LOGIN_FAIL:
            case LOGOUT_SUCCESS:
                localStorage.removeItem('token')
                return {
                    ...state,
                    isAuthenticated:null,
                    isLoading: false,
                    user:null,
                    token:null
                }
            default:
                return state
    }
}