import React, { Component } from 'react';
import './fonts/Roboto/Roboto-Medium.ttf'
import f1_logo from './logos/f1_logo.png';
import './style/App.css';
import BarChart from './components/BarChart.js';
import driverLaps from './f1/modifiedlaptimes2019.json';
import teams from './f1/teams.json'
import circuits from './f1/circuits.json'
import engineLaps from './f1/engines.json'


function importAll(r) {
  return r.keys().map(r);
}


class App extends Component {
  state = {
    laptimes: driverLaps,
    team: "4",
    driver: "1",
    driverRef1: "1",
    driverRef2: "822",
    circuit: "ALI_",
    linetype:0,
  };

  updateDriver(t) {
    this.setState({driver: teams[t]["driver00"]})
    this.setState({driverRef1: teams[t]["driver00"]})
      if(t=="6" || t=="8") {
        if(parseInt(circuits[this.state.circuit]["key"])  <=1021) {
          this.setState({driverRef2: teams[t]["driver01"]})
        } else if(parseInt(circuits[this.state.circuit]["key"])>1021) {
          this.setState({driverRef2: teams[t]["driver02"]})
        }
      } else {
        this.setState({driverRef2: teams[t]["driver01"]})
      }
  }

  handleTeamClick = (e) => {
    this.setState({laptimes:driverLaps})
    this.setState({team: e.target.value});
    this.setState({driver: teams[e.target.value]["driver00"]})
    document.getElementById('engine_info').style.display = 'none';
    document.getElementById('current_driver_info').style.display = 'block';
  }

  handleEngineClick = (e) => {
    this.setState({laptimes: engineLaps});
    this.setState({team: engineLaps[e.target.value]["team"]})
    this.setState({driver: e.target.value})
    document.getElementById('engine_info').style.display = 'block';
    document.getElementById('current_driver_info').style.display = 'none';
  }

  handleDriverClick = (e) => {
    this.setState({driver: e.target.value});
  }

  handleCircuitClick = (e) => {
    this.setState({circuit: e.target.value});
  }

  handleLineTypeClick = (e) => {
    this.setState({linetype: e.target.value});
  }

  render() {
    const carPic = importAll(require.context('./f1/images/cars/', false, /\.(JPEG|PNG|png|jpe?g|svg)$/));
    const circuitPic = importAll(require.context('./f1/images/circuits/', false, /\.(PNG|png|jpe?g|svg)$/));


    const data = [this.state.linetype,this.state.laptimes[this.state.driver][this.state.circuit+"time"], circuits[this.state.circuit]["total_laps"],
     circuits[this.state.circuit]["longest_lap"], circuits[this.state.circuit]["avg_lap"], circuits[this.state.circuit]["best_lap"]]

    return (
      <div className="App">
        <div className="App-header">
          <h2 id="mainTitle">F1 2019 Lap Times</h2>
        </div>

        <div className="menu_wrapper_team">
            <h2>Teams</h2>
            <button value="4" onClick={this.handleTeamClick}>Mercedes</button>
            <button value="1" onClick={this.handleTeamClick}>Ferrari</button>
            <button value="6" onClick={this.handleTeamClick}>Red Bull</button>
            <button value="3" onClick={this.handleTeamClick}>Maclaren</button>
            <button value="7" onClick={this.handleTeamClick}>Renault</button>
            <button value="8" onClick={this.handleTeamClick}>Toro Rosso</button>
            <button value="5" onClick={this.handleTeamClick}>Racing Point</button>
            <button value="0" onClick={this.handleTeamClick}>Alfa Romeo</button>
            <button value="2" onClick={this.handleTeamClick}>Haas</button>
            <button value="9" onClick={this.handleTeamClick}>Williams</button>
        </div>

        <div className="menu_wrapper_engine">
            <h2>Engines</h2>
            <button value="mercedes" onClick={this.handleEngineClick}>Mercedes</button>
            <button value="ferrari" onClick={this.handleEngineClick}>Ferrari</button>
            <button value="renault" onClick={this.handleEngineClick}>Renault</button>
            <button value="honda" onClick={this.handleEngineClick}>Honda</button>
        </div>

        <div className="menu_wrapper_circuit">
            <h2>Circuits</h2>
            <button value="ALI_" onClick={this.handleCircuitClick}>Australia</button>
            <button value="BAH_" onClick={this.handleCircuitClick}>Bahrain</button>
            <button value="CHI_" onClick={this.handleCircuitClick}>China</button>
            <button value="AZE_" onClick={this.handleCircuitClick}>Azerbaijan</button>
            <button value="SPA_" onClick={this.handleCircuitClick}>Spain</button>
            <button value="MON_" onClick={this.handleCircuitClick}>Monaco</button>
            <button value="CAN_" onClick={this.handleCircuitClick}>Canada</button>
            <button value="FRA_" onClick={this.handleCircuitClick}>France</button>
            <button value="AUS_" onClick={this.handleCircuitClick}>Austria</button>
            <button value="UKS_" onClick={this.handleCircuitClick}>UK</button>
            <button value="GER_" onClick={this.handleCircuitClick}>Germany</button>
            <button value="HUN_" onClick={this.handleCircuitClick}>Hungary</button>
            <button value="BEL_" onClick={this.handleCircuitClick}>Belgium</button>
            <button value="ITA_" onClick={this.handleCircuitClick}>Italian</button>
            <button value="SIN_" onClick={this.handleCircuitClick}>Singapore</button>
            <button value="RUS_" onClick={this.handleCircuitClick}>Russia</button>
            <button value="JAP_" onClick={this.handleCircuitClick}>Japan</button>
            <button value="MEX_" onClick={this.handleCircuitClick}>Mexico</button>
            <button value="USA_" onClick={this.handleCircuitClick}>USA</button>
            <button value="BRA_" onClick={this.handleCircuitClick}>Brazil</button>
            <button value="ABU_" onClick={this.handleCircuitClick}>Abu Dhabi</button>
        </div>
        <div className="chart_legend_wrapper">
          <h2 className="teamHeaderBox">{teams[this.state.team]["teamRef"]}</h2>
          <BarChart data={data} />

          <div id="engine_info">
            <img className="en" src={carPic[parseInt(this.state.team)]} />
            <p>Teams = {teams[this.state.team]["teams"]}</p>
          </div>

          <div id="current_driver_info">
          <img className="dr" src={carPic[parseInt(this.state.team)]} />
          <img className="dr" src={carPic[parseInt(this.state.team)]} />
          <div className="dr_name"><button value={teams[this.state.team]["driver00"]}  onClick={this.handleDriverClick}>{teams[this.state.team]["driver00Ref"]}</button></div>
          <div className="dr_name"><button value={teams[this.state.team]["driver01"]}  onClick={this.handleDriverClick}>{teams[this.state.team]["driver01Ref"]}</button></div>
          </div>
        </div>
        <div className="circuit_wrapper">
          <h2>{circuits[this.state.circuit]["circuitName"]}</h2>
          <img className="circ" src={circuitPic[parseInt(circuits[this.state.circuit]["raceId"])]} />
          <h3>Location = {circuits[this.state.circuit]["country"]}</h3>
          <h3>Total Laps = {circuits[this.state.circuit]["total_laps"]}</h3>
          <h3>Lap Length = {circuits[this.state.circuit]["lap_length"]}km</h3>
          <h3>Turns = {circuits[this.state.circuit]["turns"]}</h3>
          <h3>Full Throttle = {circuits[this.state.circuit]["full_throttle"]}%</h3>
          <h3>Max flat out stretch = {circuits[this.state.circuit]["flat_out_long"]}m</h3>
          <button className="lineToggle" value={1} onClick={this.handleLineTypeClick}><h3>Best lap</h3></button>
          <button className="lineToggle" value={0} onClick={this.handleLineTypeClick}><h3>Average lap</h3></button>
        </div>
      </div>
      // needs to be a json file of circuits with the {id=race # in calendar, name=full name or nickname, circuitAbbr = abbreviation prefix}

      // The names here have to be determined by this.state.team (so maybe need json file with {team,driver00,driver01)
      // so the name and driver id have to be linked there
      // Also need a team average before the specific driver is chosen
      //then need to print circuits on page too with info below

      //#### for team 6: 842 until and including race 1021 || 848 after
      //#### for team 8: 848 until and including race 1021 || 842 after

    );
  }
}

export default App;
