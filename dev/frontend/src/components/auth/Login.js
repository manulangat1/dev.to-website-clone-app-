import React from 'react'

import  { connect } from 'react-redux'

import { login } from '../../actions/auth'
import { Link,Redirect } from 'react-router-dom'
class Login extends React.Component{
    state = {
        username:'',
        password:''
    }
    onChange = e => {
        this.setState({[e.target.name]:e.target.value})
    }
    onSubmit = e => {
        e.preventDefault()
        console.log(this.state.username)
        const {username,password} = this.state
        this.props.login(username,password)
        this.setState({
            username:"",
            password:""
        })
    }
    render(){
        if(this.props.isAuthenticated){
            return <Redirect to="/" />
        }
        const {username,password} = this.state
        return(
            <section id="login">
                <h1>Login </h1>
                <div className="form">
                    <form onSubmit={this.onSubmit}>
                    <div>
                        <label>Username</label>
                        <input type="text" value={username} name="username" className="form-control" onChange={this.onChange} />
                    </div>
                    <div>
                        <label>password</label>
                        <input type="password" value={password} name="password" className="form-control" onChange={this.onChange} />
                    </div>
                    <input type="submit" className="primary-btn" Value="Sign in"/>
                    </form>
                </div>
            </section>
        )
    }
}
const mapStateToProps = state => ({
    isAuthenticated:state.auth.isAuthenticated,
    user:state.auth.user
})
export default connect(mapStateToProps,{login})(Login)
// export default Login