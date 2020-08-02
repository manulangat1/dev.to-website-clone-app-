import React from 'react'
import { Link } from 'react-router-dom'

class NotFound extends React.Component{
    render(){
        return(
            <section>
                <p>Link not working.... Kindly <Link to="/">Head over to Home</Link></p>
            </section>
        )
    }
}
export default NotFound