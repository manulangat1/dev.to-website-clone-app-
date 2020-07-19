import React from 'react'
import { connect } from 'react-redux'
import { loadPost } from '../../actions/posts'
import MarkdownPreview from '@uiw/react-markdown-preview';

class PostDetail extends React.Component{
    componentDidMount(){
        const {id } = this.props.match.params
        if (id){
            this.props.loadPost(id)
        }
    }
    render(){
        const { post } = this.props
        const postD = (
            <div>
                <h1>{post.title}</h1>
                <MarkdownPreview source={post.body} />
                <p>{post.likes} upvotes {post.dislikes} downvotes</p>
                <button>Like</button>
            </div>
        )
        const notFound = (
            <h1>Details not found this may be an eeero on our part</h1>
        )
        return(
            <section>
                {
                    post ? postD : notFound
                }
            </section>
        )
    }
}
const mapStateToProps = state => ({
    post:state.posts.post
})
export default connect(mapStateToProps,{loadPost})(PostDetail)