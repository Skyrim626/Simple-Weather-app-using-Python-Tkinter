from datetime import date


def save_text(location, time, info, weather, wind, humidity, speed, precipitation):
    """This saves the history output for no fucking reason"""
    
    today_ = date.today()
    
    file = open("History_Folder/" + str(today_) +'. txt', 'a')
    file.write("\nLocation: {}\nTime: {}\nInfo: {}\nWeather: {} C\nWind: {}\nHumidity: {}\nSpeed: {}\nPrecipitation: {}\n".format(location, time, info, weather, wind, humidity, speed, precipitation))
    
    file.close()
    
print(date.today())