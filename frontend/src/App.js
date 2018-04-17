import React, { Component } from 'react';
import './App.css';


const URL = "http://obyvacka.tk:8080";


class App extends Component {

  constructor(props) {
    super(props);
    this.state = {color: {r: 0, g: 0, b: 0}};
    this.setColor.bind(this);
    this.getXMLHttpRequest.bind(this);
    this.getXMLHttpRequest("GET").send();
  }

  getXMLHttpRequest(type) {
    const http = new XMLHttpRequest();
    http.open(type, URL, true);
    http.setRequestHeader("Content-type", "application/json");
    http.onreadystatechange = () => {
      if(http.readyState === 4 && http.status === 200) {
        const color = JSON.parse(http.responseText);
        this.setState({color: color});
      }
    }
    return http;
  }

  setColor(r, g, b) {
    this.getXMLHttpRequest("POST").send(JSON.stringify({r, g, b}));
  }
  
  render() {
    const {r, g, b} = this.state.color;
    const stringColor = `rgb(${r}, ${g}, ${b})`;
    
    return (
      <div className="App" >
        <header className="App-header" style={{ backgroundColor: stringColor }}>
          <h1 className="App-title">svetlo</h1>
        </header>
        
        <p className="App-intro">
          Nastav si svetlo!
        </p>

        <div>
          <button onClick={() => this.setColor(0, 0, 0)}>Tma</button>
          <button onClick={() => this.setColor(...[r, g, b].map(x => Math.max(0,Math.floor(x*0.9))))}>Intenzita -10%</button>
          <button onClick={() => this.setColor(...[r, g, b].map(x => Math.min(255,Math.floor(x*1.1))))}>Intenzita +10%</button>
        </div>
        
        <div>
          <button onClick={() => this.setColor(255, 0, 0)}>Red</button>
          <button onClick={() => this.setColor(0, 255, 0)}>Green</button>
          <button onClick={() => this.setColor(0, 0, 255)}>Blue</button>
          <button onClick={() => this.setColor(255,147,41)}>Sviečka</button>
          <button onClick={() => this.setColor(255,255,255)}>100%</button>
          <button onClick={() => this.setColor(255,73,18)}>Maťova žiarovka</button>
          <button onClick={() => this.setColor(50,30,10)}>Noc</button>
          <button onClick={() => this.setColor(126,0,219)}>Vodíková lampa</button>
        </div>
          

        <hr />

        <input type="range" value={r} min="0" max="255" step="1" onChange={(e) => this.setColor(e.target.value, g, b)}/>
        <input type="range" value={g} min="0" max="255" step="1" onChange={(e) => this.setColor(r, e.target.value, b)}/>
        <input type="range" value={b} min="0" max="255" step="1" onChange={(e) => this.setColor(r, g, e.target.value)}/>
      </div>
    );
  }
}

export default App;
