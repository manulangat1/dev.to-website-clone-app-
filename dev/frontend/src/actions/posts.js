import axios from 'axios'
import { GET_POSTS,ADD_POSTS,GET_POST} from './types'


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