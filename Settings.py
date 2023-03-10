from bs4 import BeautifulSoup
import requests
from save_history import save_text


headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def Weather_Update(city):
    """Sets  Weather Update, location, info, time"""
    
    city = city.replace(" ", "+")
    
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    
    soup = BeautifulSoup(res.text, 'html.parser')
    
    location = soup.select('#wob_loc')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    wind = soup.select('#wob_ws')[0].getText().strip()
    humidity = soup.select('#wob_hm')[0].getText().strip()
    speed = soup.select('#wob_tws')[0].getText().strip()
    precipitation = soup.select('#wob_pp')[0].getText().strip()
    
    #Send TxT file
    save_text(location, time, info, weather, wind, humidity, speed, precipitation)
    
    return location, time, info, weather, wind, humidity, speed, precipitation
    
    
    
    
    
    
    
