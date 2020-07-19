import React from 'react'
import { connect } from 'react-redux'
import { loadPosts } from '../../actions/posts'

import ReactMarkdown from "react-markdown";

class Posts extends React.Component{
    componentDidMount(){
        this.props.loadPosts()
    }
    render(){
        return(
            <section>
                {
                    this.props.posts.map(post => (
                        <div key={post.id}>
                            <h1>{post.title}</h1>
                            <p>{post.body}</p>
                            <ReactMarkdown source={post.body} />
                        </div>
                    ))
                }
            </section>
        )
    }
}
const mapStateToProps = state => ({
    posts:state.posts.posts
})
export default connect(mapStateToProps,{loadPosts})(Posts)