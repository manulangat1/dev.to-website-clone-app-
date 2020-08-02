import React from 'react'
import { connect } from 'react-redux'
import { loadPosts } from '../../actions/posts'
import { Link } from 'react-router-dom'
import ReactMarkdown from "react-markdown";
import MarkdownPreview from '@uiw/react-markdown-preview';
import axios from 'axios'


class Posts extends React.Component{
    componentDidMount(){
        this.props.loadPosts()
    }
    
    loadPost = (getState) =>  {
        
        this.setState({loading:true},() => {
            const {offset,limit} = this.state
            axios.get(`/api/?limit=${limit}&offset=${offset}`)
                .then(res => {
                    const newPosts = res.data.posts
                    const hasMore = res.data.has_more

                    this.setState({
                        hasMore,
                        loading:false,
                        Posts:[...this.state.Posts,...newPosts],
                        offset:offset+limit
                    })
                    console.log(this.state.Posts)
                })
                .catch()
        })
    }
    constructor(props){
        super(props)
        this.state = {
            error:false,
            loading:false,
            Posts:[],
            hasMore:true,
            offset:0,
            limit:4
        }
        const {error,loading,hasMore} = this.props
        window.onscroll = () => {
            
            // console.log(this.props.posts)
            if (loading || error  || !hasMore) return
            console.log(hasMore)
            if(document.documentElement.scrollHeight - document.documentElement.scrollTop === document.documentElement.clientHeight ){
                this.props.loadPosts()
                console.log("pdhdh")
            }
        }
        
    }
    
    render(){
        const {error,loading,posts,hasMore} = this.props
        return(
            <section id="post">
                <div className="container">
                <div style={{overflow:'hidden',flex:1}}>
                    <div className="grids">
                {
                   posts.map(post => (
                        <div key={post.id}>
                            <h1>{post.title}</h1>
                            <div className="markdown-body">
                            <MarkdownPreview source={post.body} />
                            </div>
                            <Link to={`/post/${post.id}`}>Read more</Link>
                        </div>
                    ))
                }
                </div>
                {!hasMore && <div className="noMore">No more results</div>}
                {loading && <div>Loading</div>}
                </div>
                </div>
            </section>
        )
    }
}
const mapStateToProps = state => ({
    posts:state.posts.posts,
    hasMore:state.posts.hasMore,
    limit:state.posts.limit,
    offset:state.posts.offset,
    error:state.posts.error
})
export default connect(mapStateToProps,{loadPosts})(Posts)