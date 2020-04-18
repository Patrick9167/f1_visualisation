import React, { Component } from 'react'
import * as d3 from 'd3';
import chroma from 'chroma-js';
import '../style/App.css'
import { scaleLinear } from 'd3-scale'
import { max, min } from 'd3-array'
import { select } from 'd3-selection'

const width = 1060;
const height = 700;
const margin = {top: 20, right: 70, bottom: 50, left: 50};
// etc


/* This is a basic d3 bar chart to show how to us d3 in react
   from https://medium.com/@Elijah_Meeks/interactive-applications-with-react-d3-f76f7b3ebc71*/

class BarChart extends Component {
   state={
     bars:[],
     line_coords:0,
     label:"",
     xScale: d3.scaleLinear().range([margin.left, width - margin.right]),//[0, width]),
     yScale: d3.scaleLinear().range([height - margin.bottom, margin.top]),
    // colorScale: d3.scaleLinear()
   };

   xAxis = d3.axisBottom().scale(this.state.xScale)//.tickFormat('%b')
   yAxis = d3.axisLeft().scale(this.state.yScale)//.tickFormat(d=>'${d}s')

   static getDerivedStateFromProps(nextProps, prevState) {
     if(!nextProps.data) return null; //data not loaded
     const{data}=nextProps;
     const{xScale, yScale, tempScale, colorScale}=prevState;


    // data = [linetype, lap_times, total_laps, longest_lap, avg_lap, best_lap]

    const totalLaps = parseInt(data[2]);
    const rectWidthScaling = 20-(totalLaps/9)
    const longestLap=data[3]
    const lapComplete = data[1].length;
    const timesMax = d3.max(data[1]);

    xScale.domain([0,totalLaps]);
    yScale.domain([0,longestLap]);

    //Check if best_lap or avg_lap to display
    var line_coords=yScale(data[4])
    var label = "Avg. Lap"
    if(data[0]==1) {
      line_coords=yScale(data[5])
      label = "Best Lap"
    }

    //calculate x and y for each rect
    var i = 1
    const bars = data[1].map(d=> {
      const y1 = yScale(d/60)
      const x1 =  xScale(i);
      i+=1
      return {
        x: x1,
        y: yScale(d),
        height: (height-margin.bottom)-yScale(d),
        width: rectWidthScaling,
        fill: "black",
      }
    })
    if(timesMax==0) bars[0].height=0;
    return {bars, line_coords, label}
   }

componentDidUpdate() {
  d3.select(this.refs.xAxis).call(this.xAxis);
  d3.select(this.refs.yAxis).call(this.yAxis);
}

render() {
      return (
        <div className="barchart">
        <svg height={height} width={width}>
          {this.state.bars.map((d, i) =>
            (<rect key={i} x={d.x} y={d.y} width={d.width} height={d.height} fill={d.fill} />))}
          <line x1={margin.left} x2={width-margin.right/2} y1={this.state.line_coords} y2={this.state.line_coords} strokeWidth={2} stroke="red"/>
          <text transform={`translate(${width-margin.right}, ${this.state.line_coords-5})`} fill="red">{this.state.label}</text>
           <g>
             <g ref='xAxis' transform={`translate(0, ${height-margin.bottom})`} />
             <text transform={`translate(${(width/2)-margin.right}, ${height-10})`}>Lap</text>
             <g ref='yAxis' transform={`translate(${margin.left}, 0)`} />
             <text className="yTrans">Lap Time (s)</text>
           </g>
        </svg>
        </div>
      )
   }
}
export default BarChart

// width={width} height={height}
