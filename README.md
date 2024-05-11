# Sanalouhos Solver

Solves the Sanalouhos game Helsingin Sanomat. Playable here: https://sanalouhos.datadesk.hs.fi/
Uses Selenium to automatically fetch the data for each day. The selenium_data_importer.py implements abstract_data_importer which can be used to manually input Sanalouhos data (to decouple it from the actual game files).

## How to use

First install the required dependencies:
`pip install -r requirements.txt`

Then you can run the script:
`python main.py`.


## Word list
The program uses a word list downloaded from KOTUS: https://kaino.kotus.fi/lataa/nykysuomensanalista2024.csv

## Example output

```
11:12:02 Sanalouhos Solver 2000
11:12:02 Initialized word list with 104211 words
11:12:04 Initialized Sanalouhos solver with the following matrix:
['h', 'a', 'u', 't', 'o']
['r', 't', 'a', 'a', 'o']
['a', 'v', 'e', 'l', 'i']
['a', 'a', 't', 'r', 'a']
['t', 'v', 'a', 'v', 'l']
['a', 'a', 't', 't', 'i']
11:12:05 Found 1082 possible words from the matrix
11:12:05 Starting solve...
11:12:15 Solution found (30 coordinates, 5 words)
valittaa     vartalo      hautoa
________
. . . . .    . . . . .    h a u t o
. . . . .    r t a . o    . . . a .
. . . . .    a v . l .    . . . . .
. . . . a    . . . . .    . . . . .
. . a v l    . . . . .    . . . . .
. a t t i    . . . . .    . . . . .
________
tavata       eri
________
. . . . .    . . . . .
. . . . .    . . . . .
. . . . .    . . e . i
a a t . .    . . . r .
t v . . .    . . . . .
a . . . .    . . . . .
________
```