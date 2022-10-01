from flask import Flask

import dbcreds as dbc
import json
import dbhelpers
from dbhelpers import run_statement

app = Flask(__name__)

@app.get('/cars')
def get_cars():
    results= run_statement('CALL get_cars()')
    if(type(results) == list):
        cars_json = json.dumps(results, default=str)
        return cars_json
    else:
        return "sorry something went wrong"    

app.run(debug=True)        