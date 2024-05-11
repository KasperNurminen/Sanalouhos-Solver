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