<h1 align="center">IRC ACC Scripts</h1>

## Consists of a number of scripts for setting the race server and capturing results from the ACC game.

## Entry List Creator
Generates an `entrylist` based on the signups on the website. <br> 
Requires `signuplatest.json` for the latest roster for the ACC Season <br>
> Run command: `python entryListCreator.py` 

---

## Result to Grid
Generates the new `entrylist` for the next ACC Race, depending on the finishing order of the previous race of the weekend. <br>
> Run command: `python resultToGrid.py` 

---

## Result Split
Split the website result file into multiple result files based on the driver classes. <br>
Requires `classes.json`, a *config* file denoting the Driver - Class mapping.

*Optional Flag* at the end `-s` to save class results to separate JSON files <br>
If enabled, the script saves the class results in the `results` directory
> Run command: `node resultSplit.js <PATH_TO_RESULT_FILE> [-s]`
