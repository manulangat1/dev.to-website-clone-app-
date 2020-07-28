import React from 'react'
import { Link } from 'react-router-dom'

class NotFound extends React.Component{
    render(){
        return(
            <section id="notFound">
                <div className="container">
                <p>Link not working.... Kindly <Link to="/">Head over to Home</Link></p>
                </div>
            </section>
        )
    }
}
export default NotFound