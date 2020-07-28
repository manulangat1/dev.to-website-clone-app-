import React from 'react';

import store from './store'
import { Provider } from 'react-redux'
import Posts from './components/Posts/Post'
import NotFound from './components/error/NotFound'
import PostDetail from './components/Posts/PostDetail'
import Login from './components/auth/Login'
import { HashRouter as Router,Route,Switch} from 'react-router-dom'
class App extends React.Component{
  render(){
    return(
      <Provider store={store}>
      <Router>
      <main>
        <Switch>

        <Route exact path="/post/:id" component={PostDetail} />
        <Route exact path="/" component={Posts} />
        <Route exact path="/login/" component={Login}  />
        <Route exact path="**" component={NotFound} />
        
        </Switch>
      </main>
      </Router>
      </Provider>
    )
  }
}

export default App;
