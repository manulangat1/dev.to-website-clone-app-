import React from 'react'
import { connect } from 'react-redux'
import { loadPosts } from '../../actions/posts'
import { Link } from 'react-router-dom'
import ReactMarkdown from "react-markdown";
import MarkdownPreview from '@uiw/react-markdown-preview';

// import 'github-markdown-css'

class Posts extends React.Component{
    componentDidMount(){
        this.props.loadPosts()
    }
    constructor(props){
        super(props)
        const {posts,hasMore} = this.props
        window.onscroll = () => {
            
            // console.log(this.props.posts)
            if (!hasMore) return
            console.log(hasMore)
            if(document.documentElement.scrollHeight - document.documentElement.scrollTop === document.documentElement.clientHeight ){
                console.log("hello")
            }
        }
        
    }
    
    render(){
        return(
            <section>
                {
                    this.props.posts.map(post => (
                        <div key={post.id}>
                            <h1>{post.title}</h1>
                            {/* <p>{post.body}</p> */}
                            <div className="markdown-body">
                            {/* <ReactMarkdown source={post.body} /> */}
                            <MarkdownPreview source={post.body} />
                            </div>
                            <Link to={`/post/${post.id}`}>Read more</Link>
                        </div>
                    ))
                }
            </section>
        )
    }
}
const mapStateToProps = state => ({
    posts:state.posts.posts,
    hasMore:state.posts.hasMore,
    limit:state.posts.limit,
    offset:state.posts.offset
})
export default connect(mapStateToProps,{loadPosts})(Posts)