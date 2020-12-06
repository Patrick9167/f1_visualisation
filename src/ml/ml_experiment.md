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
|driverId|constructorId|engineId|lap#|pit|laps after pit|pos|time(min)|time(ms)|
|---|---|---|---|---|---|---|---|---|
| int | int | [0..3] | [1..N]| [0,1]| [1..K]| [1..20]| m:sss:msmsms | 00000

* __driverID__ (the driver)[lap_times]
* __constructorId__ (for car type)
* __engineId__ (for engine type)(may need one hot encoding)
* __lap#__ (maybe tie this into fuel)
* __laps since pitstop__ (new tyres/determine how many laps after is optimum time reached)[pit_stops.csv/stop]
* __pos__ (helps to know if driver is fighting/defending. May need to find way to determine distance from surrounding drivers)
* __time(min)__ (will need investigation to understand the correct format)
* __time(ms)__ (this could be the better choice for some models as target)

**Adding qualyfying times may work but will need processing for current fuel amount etc

## Analysis 1
__R studio__


