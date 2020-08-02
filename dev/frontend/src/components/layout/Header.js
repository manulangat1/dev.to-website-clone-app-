import React from 'react'
import {Route,NavLink,Link} from 'react-router-dom'
import { connect } from 'react-redux'
import { logout } from '../../actions/auth'
class Header extends React.Component{
    render(){
        const {isAuthenticated} = this.props

        const guestLinks = (
            <div className="container">
                    <h1>Dev.to</h1>
                    <div>
                    <ul>
                    {/* <li> <NavLink to="/">Home</NavLink> </li> */}
                    <li> <NavLink to="/register/">Register</NavLink> </li>
                    <li> <NavLink to="/login/">Login</NavLink> </li>
                </ul>
                    </div>
                </div>
        )
        const authLinks = (
            <div className="container">
                    <NavLink to="/">
                    <h1>Dev.to</h1>
                    </NavLink> 
                    <div>
                    <ul>
                    <li> </li>
                    {/* <li> <NavLink to="/login/">Login</NavLink> </li> */}
                    <li><button onClick= {this.props.logout} className=""><i class="fas fa-sign-out-alt"> Log out</i></button></li>
                </ul>
                    </div>
                </div>
        )
        return(
            <header>
                {isAuthenticated ? authLinks : guestLinks}
            </header>
        )
    }
}
const mapStateToProps = state => ({
    isAuthenticated:state.auth.isAuthenticated,
    user:state.auth.user
})
export default connect(mapStateToProps,{logout})(Header)