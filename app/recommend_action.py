def recommend_action(location,fp): 
    import pywapi
    import random
    import json

    #location = raw_input("enter your location : ") 
    location_id = pywapi.get_loc_id_from_weather_com(location)
    location_id = location_id[0][0]

    weather = pywapi.get_weather_from_weather_com(location_id)
    print weather['current_conditions']['station'], 'is', weather['current_conditions']['text'] 

    weather_condition = weather['current_conditions']['text'] 

    conditions = weather['current_conditions']['text']
    conditions_list = conditions.split()

    with open(fp) as data:
        todo = json.load(data)

    hit = list(set(conditions_list).intersection(todo))

    if hit:
        weather_action =  random.choice(todo[random.choice(hit)])
        
    else:
        weather_action = "Sorry! not smart enough to recommend!"
        
    return (weather_condition,weather_action)
