from flask import Flask, render_template, request
from flask_cors import CORS
from controller import Controller
import os

title = os.getenv("SUNRISE_SUNSET_TITLE", "Sunrise/Sunset")

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
   return render_template('index.html', title=title)

@app.route('/report', methods=['POST', 'GET'])
def ezw():
    if request.method == 'POST':
       data = request.json
       location = data['location']

       sunriseController = Controller()

       geoLocation = sunriseController.getLocation(location)
       if geoLocation == None:
           searchArea = "Unknown location"
           reportTemplate = render_template('reports.html', area=searchArea)
           return reportTemplate

       searchArea = geoLocation.address
       sunriseReports = sunriseController.getSunriseReport(data, geoLocation)

       reportTemplate = render_template('reports.html', area=searchArea, reports=sunriseReports)

    return reportTemplate

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=False,host='0.0.0.0')
