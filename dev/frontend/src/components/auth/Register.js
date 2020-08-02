import React from 'react'
import { connect } from 'react-redux'
import { Redirect } from 'react-router-dom'
import {register} from '../../actions/auth'
class Register extends React.Component{
    state = {
        username:'',
        password:'',
        password2:'',
        bio:'',
        email:''
    }
    onChange = e => this.setState({[e.target.name]:e.target.value})
    onSubmit = e => {
        e.preventDefault()
        const { username,password,password2,bio,email} = this.state
        console.log(username,password,password2,bio,email)
        
        if(password === password2){
            const newUser = {
                username,password,bio,email
            }
            this.props.register(newUser)
        }
    }
    render(){
        if (this.props.isAuthenticated){
            return <Redirect to="/" />
        }
        const { username,password,password2,bio,email} = this.state
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
                    <div>
                        <label>password</label>
                        <input type="password" value={password2} name="password2" className="form-control" onChange={this.onChange} />
                    </div>
                    <div>
                        <label>email</label>
                        <input type="email" value={email} name="email" className="form-control" onChange={this.onChange} />
                    </div>
                    <div>
                        <label>Bio</label>
                        <input type="text" value={bio} name="bio" className="form-control" onChange={this.onChange} />
                    </div>
                    <input type="submit" className="primary-btn" Value="Sign in"/>
                    </form>
                </div>
            </section>
        )
    }
}
const mapStateToProps = state => ({
    isAuthenticated:state.auth.isAuthenticated
})
export default connect(mapStateToProps,{register})(Register)
// export default Register