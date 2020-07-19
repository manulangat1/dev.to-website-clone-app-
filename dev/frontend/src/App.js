import React from 'react';

import store from './store'
import { Provider } from 'react-redux'
import Posts from './components/Posts/Post'
class App extends React.Component{
  render(){
    return(
      <Provider store={store}>
      <main>
        <h1>hj</h1>
        <Posts />
      </main>
      </Provider>
    )
  }
}

export default App;
