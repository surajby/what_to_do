from app import app
from flask import render_template, request
from recommend_action import recommend_action

@app.route('/',methods = ['GET','POST'])
#@app.route('/index')
def index():
    #the json text files' path to recommend actions, change this
    file_path = '/home/sby/Documents/webapps/randomness/app/weather_types.txt'
    weather = ''
    wa = ''
    place =''
    
    if request.method == 'POST':
        #user['nickname'] = request.form['name']
        place = request.form['city']
        (weather,wa) = recommend_action(place, file_path)
        
    return render_template('index.html',title = 'hello', wa = wa, weather = weather, place = place)
    #return render_template('index.html',title = 'hello', user = user)
    
