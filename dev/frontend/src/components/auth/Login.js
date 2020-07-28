import React from 'react'

import  { connect } from 'react-redux'


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
    }
    render(){
        const {username,password} = this.state
        return(
            <section>
                <h1>Login </h1>
                <div className="form">
                    <form onSubmit={this.onSubmit}>
                    <div>
                        <label>Username</label>
                        <input type="text" value={username} name="username" onChange={this.onChange} />
                    </div>
                    <div>
                        <label>password</label>
                        <input type="password" value={password} name="password" onChange={this.onChange} />
                    </div>
                    <input type="submit" className="btn-primary" Value="Sign in"/>
                    </form>
                </div>
            </section>
        )
    }
}
const mapStateToProps = state => ({

})
// export default connect(mapStateToProps,{})(Login)
export default Login