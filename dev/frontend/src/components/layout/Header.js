import React from 'react'
import {Route,NavLink,Link} from 'react-router-dom'

class Header extends React.Component{
    render(){
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
export default Header