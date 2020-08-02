import React from 'react';

import store from './store'
import { Provider } from 'react-redux'
import Posts from './components/Posts/Post'
import NotFound from './components/error/NotFound'
import PostDetail from './components/Posts/PostDetail'
import Login from './components/auth/Login'
import Register from './components/auth/Register'
import { HashRouter as Router,Route,Switch} from 'react-router-dom'

import Header from './components/layout/Header'
import Footer from './components/layout/Footer'

import './styles/main.scss'

class App extends React.Component{
  render(){
    return(
      <Provider store={store}>
      <Router>
      <Header />
      <main>
        
        <Switch>

        <Route exact path="/post/:id" component={PostDetail} />
        <Route exact path="/" component={Posts} />
        <Route exact path="/login/" component={Login}  />
        <Route exact path="/register/" component={Register}  />
        <Route exact path="**" component={NotFound} />
        
        </Switch>
      </main>
      <Footer />
      </Router>
      </Provider>
    )
  }
}

export default App;
