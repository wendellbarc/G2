import time
import datetime
from flask import Flask, render_template, request, jsonify
import requests
import requests_cache
from prometheus_flask_exporter import PrometheusMetrics
from flask_prometheus import monitor 
import sys


requests_cache.install_cache(expire_after=300)

app = Flask(__name__)

@app.route('/version')
def version():
    return render_template('version.html')


@app.route('/')
def root():
 return render_template('newmain.html')



@app.route('/weather', methods=['POST', 'GET'])
def weather():
    lat = request.form['lat']
    lon = request.form['lon']
    t_threshold = request.form['t_threshold']
    w_threshold = request.form['w_threshold']
    metric = request.form['metric']
    r = requests.get('https://api.darksky.net/forecast/25526a9ace577c46efe91103749d39ed/'+lat+','+lon+'?units='+metric+'&exclude=minutely,flags,hourly')


    old_stdout = sys.stdout
    log_file = open("cache.log","w")
    sys.stdout = log_file

    print ('Cache enabled for this request:', r.from_cache)
    print('Request:', requests_cache.get_cache())

    sys.stdout = old_stdout
    log_file.close()


    json=r.json()

    epoch=json['currently']['time']
    currenttime=time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(epoch))
    
    return render_template('newweather.html', json=json, currenttime=currenttime, t_threshold=t_threshold, w_threshold=w_threshold)


monitor(app, port=8000)

if __name__ == '__main__':
 import logging
 logging.basicConfig(filename='logs.log',level=logging.DEBUG)
 app.run(host='0.0.0.0')
