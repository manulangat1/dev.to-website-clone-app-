import React from 'react'
import {Route,NavLink,Link} from 'react-router-dom'

class Header extends React.Component{
    render(){
        return(
            <header>
                <ul>
                    <li> <NavLink to="/">Home</NavLink> </li>
                    <li> <NavLink to="/login/">Login</NavLink> </li>
                </ul>
            </header>
        )
    }
}
export default Header