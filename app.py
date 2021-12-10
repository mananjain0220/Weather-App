import requests
from flask import Flask, render_template, request
import configparser

app = Flask(__name__)
		
def get_weather_updates(zipcode,api_keys):
	url = 'http://api.openweathermap.org/data/2.5/weather?zip={}&units=metric&appid={}'.format(zipcode,api_keys)
	r = requests.get(url)
	return r.json()


def get_api_key():
	config = configparser.ConfigParser()
	config.read('config.ini')
	return config['openweathermap']['api']

#print(get_weather_updates('95129',get_api_key()))




@app.route('/' )
def weather_dashboard():
	
	return render_template('homepage.html')


@app.route('/result', methods = ['POST'])
def render_results():
	api_key = get_api_key()
	zip_code = request.form['zipCode']
	data = get_weather_updates(zip_code,api_key)
	temp ="{0:.2f}".format( data["main"]['temp'])
	feels_like = "{0:.2f}".format( data["main"]['feels_like'])
	weather = data['weather'][0]['main']
	location = data['name']

	return render_template('result.html', location = location, temp= temp, feels_like = feels_like, weather = weather)






if __name__ == "__main__":
    app.run(debug = True)