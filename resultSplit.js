// Author: kapilace6
// Script to split Race results to various class results
// Run command: node resultsplit.js <PATH_TO_RESULT_FILE>

var t, r, re
var race, classes
var fs = require('fs')

// Read json from classes. 
// Classes.json contains the class assigned to each driver
try { classes = require('./classes.json') }
catch (e) {
    switch (e.code) {
        case 'MODULE_NOT_FOUND': 
            console.error('Classes json file not found.')
            break

        default:
            console.error('Something went wrong with the Result json file: ' + e.code)
            break
    }
    process.exit()
}

// Read results file from args
try { race = require(process.argv[2]) }
catch (e) {
    switch (e.code) {
        case 'ERR_INVALID_ARG_TYPE': 
            console.error('Result json file missing as argument')
            break

        case 'MODULE_NOT_FOUND': 
            console.error('Result json file not found. Add \".\/\" to the path to reference current working directory')
            break

        default: 
            console.error('Something went wrong with the Result json file: ' + e.code)
            break
    }
    process.exit()
}

// Iterate through the classes in classes.json
for(var c in classes) {
    t = race.track
    t.season_id = classes[c].season

    // Filter Drivers which are present in class
    re = race.results.filter(d => classes[c].drivers.includes(d.driver_id))

    r = {track: t, results: re}
    console.log(r)
    console.log("------ ^ " + c.toUpperCase() + " ^ ------")

    // Write to results directory if save flag enabled
    if(process.argv.length > 3 && process.argv[3].toLowerCase() == '-s') {
        if(!fs.existsSync('./results'))
            fs.mkdirSync('./results')
        
        fs.writeFile(`results/IRC_ACC_${r.track.season_id}_R${r.track.round}_${c.toUpperCase()}.json`, 
            JSON.stringify(r), 'utf-8', 
            (err) => { if(err) console.error(err) }
        )
    }
}