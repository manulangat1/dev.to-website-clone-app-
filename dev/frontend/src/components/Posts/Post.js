import React from 'react'
import { connect } from 'react-redux'
import { loadPosts } from '../../actions/posts'

class Posts extends React.Component{
    componentDidMount(){
        this.props.loadPosts()
    }
    render(){
        return(
            <section>
                <h1>hey</h1>
            </section>
        )
    }
}
const mapStateToProps = state => ({
    posts:state.posts.posts
})
export default connect(mapStateToProps,{loadPosts})(Posts)