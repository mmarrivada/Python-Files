from flask import *
from chartdb import *
import json
app = Flask(__name__)

@app.route("/")
def home():

    return render_template('chart.html')
    # return "Hello World"

@app.route('/chart_data')
def get_chartdata():
    return json.dumps(get_details())


if __name__ == "__main__":
    app.run(debug=True)


