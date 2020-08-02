import { GET_POSTS,ADD_POSTS,GET_POST, ADD_LIKE }  from '../actions/types'

const initialState = {
    posts:[],
    post:[],
    like:[],
    hasMore:true,
    offset:0,
    limit:4,
    error:false,
    loading:false
}
export default function(state=initialState,action){
    switch(action.type){
        case GET_POSTS:
            return {
                ...state,
                posts:[...state.posts,...action.payload.posts],
                hasMore:action.payload.has_more,
                error:false,
                loading:false,
                offset:state.offset+state.limit
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