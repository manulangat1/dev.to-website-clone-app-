import React from 'react'
import {Route,NavLink,Link} from 'react-router-dom'
import { connect } from 'react-redux'
class Header extends React.Component{
    render(){
        const {isAuthenticated} = this.props
        return(
            <header>
                <div className="container">
                    <h1>Dev.to</h1>
                    <div>
                    <ul>
                    <li> <NavLink to="/">Home</NavLink> </li>
                    <li> <NavLink to="/register/">Register</NavLink> </li>
                    <li> <NavLink to="/login/">Login</NavLink> </li>
                </ul>
                    </div>
                </div>
                
            </header>
        )
    }
}
const mapStateToProps = state => ({
    isAuthenticated:state.auth.isAuthenticated,
    user:state.auth.user
})
export default (mapStateToProps,null)(Header)