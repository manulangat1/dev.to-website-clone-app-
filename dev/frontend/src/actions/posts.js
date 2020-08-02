import axios from 'axios'
import { GET_POSTS,ADD_POSTS,GET_POST, ADD_LIKE,REMOVE_LIKE} from './types'


export const loadPosts = () => (dispatch,getState) => {
    axios
        .get('/api/')
        .then( res => {
            dispatch({
                type:GET_POSTS,
                payload:res.data
            })
        })
        .catch(err => console.log(err))
}

export const loadPost = id => (dispatch,getState) => {
    const config={
        headers:{
            'Content-Type':'application/json'
        }
    }
    axios
        .get(`/api/post/${id}/`)
        .then(
            res => {
                dispatch({
                    type:GET_POST,
                    payload:res.data
                })
            }
        )
        .catch(err => console.log(err))
}
export const addLike = id => (dispatch,getState) => {
    const config={
        headers:{
            'Content-Type':'application/json'
        }
    }
    const body = JSON.stringify({id})
    axios
        .post('/api/like/create/',body,config)
        .then(res => {
            dispatch({
                type:ADD_LIKE,
                payload:res.data
            })
        })
        .catch(err => console.log(err))
}