import React from 'react'

import Post from './Post'
import Sticky from 'react-stickynode';
class Dashboard extends React.Component{
    sidebar = document.getElementById("sidebar")
    constructor(){
        super()
        window.onscroll = () => {
            
            console.log("hdjd")
            if(document.documentElement.scrollHeight - document.documentElement.scrollTop === document.documentElement.clientHeight ){
                console.log("pdhdh")
                console.log(document.documentElement.scrollHeight + document.documentElement.scrollHeight)
                this.sidebar.style({height:document.documentElement.scrollHeight + document.documentElement.scrollHeight})
                console.log(this.sidebar)
            }
        }
    }
    render(){
        return(
            <section id="dash">
                <div className="container">
                <Sticky enabled={true} top={50} bottomBoundary={1200} innerClass="sidepanel" >
                        {/* <YourComponent/> */}
                        <h1>ppp</h1>
                </Sticky>
                    {/* <div id="page-wrap">
                    <div id="sidebar">
                        <h1>hey</h1>
                    </div>
                    </div> */}
                    <div className="main">
                    <Post />
                    </div>
                    
                </div>
            </section>
        )
    }
}
export default Dashboard