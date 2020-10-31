# ML experiment plan

__Aim__: 
* __To predict the specific lap time. (of that circuit) each test will be circuit based__
  * Maybe to find what is more important for each circuit
* Also, could make the strategy/#ofpits as the target value
  1. So the predicted value could be 1 or 2 (for pitstops; a bit simple)
  2. Or "2 M-S-M" to determine the exact strategy.. maybe even something like "2 22-5-19" as the length of stints (laps per stint) will be easily calculated whereas I would be guessing the tyre type based on the stint length


*notes
* continuous data - want down to thousands of a second at least

__Features/Predictors__: *open to changes*
* driverID (the driver)[lap_times]
* lap# (maybe tie this into fuel)
* laps since pitstop (new tyres/determine how many laps after is optimum time reached)[pit_stops.csv/stop]
* pos (helps to know if driver is fighting/defending. May need to find way to determine distance from surrounding drivers)
* constructor (for car type)

**Adding qualyfying times may work but will need processing for current fuel amount etc


