import { GET_POSTS,ADD_POSTS,GET_POST, ADD_LIKE }  from '../actions/types'

const initialState = {
    posts:[],
    post:[],
    like:[],
    hasMore:true,
    offset:0,
    limit:20
}
export default function(state=initialState,action){
    switch(action.type){
        case GET_POSTS:
            return {
                ...state,
                posts:action.payload
            }
        case GET_POST:
            return {
                ...state,
                post:action.payload
            }
        case ADD_LIKE:
            return{
                ...state,
                like:action.payload
            }
        default:
            return state
    }
}