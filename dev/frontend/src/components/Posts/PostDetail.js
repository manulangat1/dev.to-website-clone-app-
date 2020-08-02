import React from 'react'
import { connect } from 'react-redux'
import { loadPost ,addLike} from '../../actions/posts'
import MarkdownPreview from '@uiw/react-markdown-preview';

class PostDetail extends React.Component{
    componentDidMount(){
        const {id } = this.props.match.params
        if (id){
            this.props.loadPost(id)
        }
    }
    
    render(){
        const onClick = id => {
            // const {id} = this.props.match.params
            console.log("hey")
            if (id){
                console.log(id)
                this.props.addLike(id)
            }
        }
        const { post } = this.props
        const postD = (
            <div className="container">
                <h1>{post.title}</h1>
                <MarkdownPreview source={post.body} />
                <p>{post.likes} upvotes {post.dislikes} downvotes</p>
                <button onClick={onClick.bind(this,post.id)}>Like</button>
            </div>
        )
        const notFound = (
            <h1>Details not found this may be an eeero on our part</h1>
        )
        return(
            <section id="postDetail">
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
export default connect(mapStateToProps,{loadPost,addLike})(PostDetail)