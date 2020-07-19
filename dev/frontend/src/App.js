import React from 'react';

import store from './store'
import { Provider } from 'react-redux'

class App extends React.Component{
  render(){
    return(
      <Provider store={store}>
      <main>
        <h1>hj</h1>
      </main>
      </Provider>
    )
  }
}

export default App;
