import React, {Component} from 'react';
import GetData from './components/DataServer/Getdata';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
      
        <h1 className="header">Tempurature Data</h1>
          <GetData/>
          
      </div>
    );
    }
}

export default App;
