import axios from 'axios'
import { GET_POSTS,ADD_POSTS} from './types'


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