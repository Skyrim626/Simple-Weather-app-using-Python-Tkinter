"""pip install this libraries(recommended):
    
    requests
    customtkinter
    sys
    BeautifulSoup
    tkintermapview

"""

from tkinter import*
from tkinter import ttk
from tkinter import messagebox as mssg
from PIL import ImageTk, Image
from time import strftime

import customtkinter
import sys
from tkintermapview import TkinterMapView

from Settings import Weather_Update


#----------Map View Area----------#
def mark_location():
    """Marks a location"""
    current_position = map_widget.get_position()
    mark_list.append(map_widget.set_marker(current_position[0], current_position[1]))

def clear_marker():
    """Deletes a marker"""
    for marker in mark_list:
        marker.delete()

def chosen_city(event = None):
    """Displays the City Location"""
    try:
        city = city_entry.get()
        map_widget.set_address(city)
        
    except:
        mssg.showwarning('Not Found!', 'City Not Found!')
        map_widget.set_address("Cagayan de Oro")
    
def slider_event(value):
    """This zooms in/out World Map"""
    map_widget.set_zoom(value)


def map_view_area():
    
    """This views map area"""
    
    try:
        """Hides Frame Area"""
        weather_area.grid_forget() if weather_area.winfo_manager() else weather_area.grid(row = 0, column = 1, sticky = 'ne', padx = 5, pady = 5)
    
    except:
        pass
    
    #-----Configure Buttons-----#
    search_button.config(command = chosen_city)
    set_mark.config(command = mark_location, state = 'normal', text = 'Set Marker')
    clear_mark.config(command = clear_marker, state = 'normal', text = 'Clear Markers')
    
    global map_view_frame
    map_view_frame = Frame(window, width = 800, height = 100, bg = '#2F2F2F', bd = 5, relief = RIDGE,)
    
    map_view_frame.grid(row = 0, column = 1, sticky = 'ne', padx = 20, pady = 10)
    
    try:
        global map_widget
        map_widget = TkinterMapView(map_view_frame, corner_radius=8, bg = '#2F2F2F', width = 550, height = 440)
        map_widget.grid(row = 0, column = 0)
        
        map_widget.set_address("Cagayan de Oro")
    
    except Exception as e:
        print(e)
        pass
    
    slider = customtkinter.CTkSlider(map_view_frame, width = 280, height=16, from_=0, to=19, border_width = 5, command = slider_event)
    slider.grid(row = 1, column = 0, pady = 15)
    
        
#-------------------------------------#

#----------Weather View Area----------#

def show_hide():
    """Shows menu"""
    if show_ui.get() == 1:
        only_frame.grid_forget() if only_frame.winfo_manager() else only_frame.grid(row = 0, column = 0, sticky = 'ne')
        
        left_body_Frame.grid(row = 0, column = 0, sticky = 'nswe')
        weather_area.grid(row = 0, column = 1, sticky = 'ne', padx = 5, pady = 5)
        hide_ui.select()
    
    else:
        pass

def hide_show():
    """Hides the main window"""
    if hide_ui.get() == 1:
        pass
        
    else:
        
        try:
            weather_area.grid_forget() if weather_area.winfo_manager() else weather_area.grid(row = 0, column = 1, sticky = 'ne', padx = 5, pady = 5)
            
            left_body_Frame.grid_forget() if left_body_Frame.winfo_manager() else left_body_Frame.grid(row = 0, column = 0, sticky = 'nswe')
            global only_frame
            only_frame = customtkinter.CTkFrame(window, width = 50, height = 150)
            only_frame.grid(row = 0, column = 0, sticky = 'ne')
            global show_ui
            show_ui = customtkinter.CTkSwitch(only_frame, text = 'Show UI', command = show_hide)
            show_ui.grid(row = 0, column = 0, sticky = 'e', padx = 10, pady = 10)
            #show_ui.select()
        
        except:
            print('Unhide')
            pass

def display_weather(city):
    """Displays Weather Update"""
    if city != '':
        location_update, time_update, cloud_info, weather_info, wind_info, humidity_info, speed_info, precipitation_info = Weather_Update(city + " weather")
        
        location.config(text = location_update)
        
        time_city.config(text = time_update)
        celsius_label.config(text = weather_info + '°C')
        
        wind_display.config(text = wind_info)
        humidity_display.config(text = humidity_info)
        speed_display.config(text = speed_info)
        precipitation_display.config(text = precipitation_info)
        
        if cloud_info.lower() == 'mostly cloudy' or cloud_info.lower() == 'cloudy':
            cloud_label.config(text = cloud_info + ' feels like ' + weather_info + '°')
            display_cloud.config(image = clouds_library[0])
            
        elif cloud_info.lower() == 'mostly sunny' or cloud_info.lower() == 'sunny':
            cloud_label.config(text = cloud_info + ' feels like ' + weather_info + '°')
            display_cloud.config(image = clouds_library[1])
            
        elif cloud_info.lower() == 'rain':
            cloud_label.config(text = cloud_info + ' feels like ' + weather_info + '°')
            display_cloud.config(image = clouds_library[3])
            
        elif cloud_info.lower() == 'light rain showers':
            cloud_label.config(text = cloud_info + ' feels like ' + weather_info + '°')
            display_cloud.config(image = clouds_library[2])
            
        elif cloud_info.lower() == 'partly cloudy' or cloud_info.lower() == 'clear with periodic clouds':
            cloud_label.config(text = cloud_info + ' feels like ' + weather_info + '°')
            display_cloud.config(image = clouds_library[4])
            
        elif cloud_info.lower() == 'clear':
            cloud_label.config(text = cloud_info + ' feels like ' + weather_info + '°')
            display_cloud.config(image = clouds_library[5])
        
    else:
        pass


def refreshing():
    
    """It just refresh the Weather"""
    
    if city_entry.get() != None:
        display_weather(city_entry.get())
    
    else:
        display_weather('Cagayan de Oro')

def weather_area():
    
    try:
        """Hides Frame Area"""
        map_view_frame.grid_forget() if map_view_frame.winfo_manager() else map_view_frame.grid(row = 0, column = 1, sticky = 'ne', padx = 5, pady = 5)
    
    except:
        pass
    
    #-----Configure Buttons-----#
    search_button.config(command = lambda: display_weather(city_entry.get()))
    set_mark.config(command = refreshing, state = 'active', text = 'Refresh')
    clear_mark.config(command = None, state = DISABLED, text = 'Show Future')
    
    global weather_area
    weather_area = customtkinter.CTkFrame(window, width = 780, height = 200, bd = 1, bg = 'black')
    weather_area.grid(row = 0, column = 1, sticky = 'ne', padx = 10, pady = 5)
    
    title_area = customtkinter.CTkFrame(weather_area, width = 400, height = 150)
    title_area.grid(row = 0, column = 0, padx = 10, pady = 10)
    
    mid_area = customtkinter.CTkFrame(weather_area, width = 400, height = 150)
    mid_area.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'w')
    
    right_area = customtkinter.CTkFrame(weather_area, width = 50, height = 150)
    right_area.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'ne')
    
    bottom_area = customtkinter.CTkFrame(weather_area, width = 400, height = 150)
    bottom_area.grid(row = 5, column = 0, padx = 5, pady = 5)
    
    global location
    location = customtkinter.CTkLabel(title_area, text = '', text_font = ('Roboto Medium', 17))
    location.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'w')
    
    current_weather = customtkinter.CTkLabel(mid_area, text = 'Current Weather', text_font = ('Roboto Medium', 10))
    current_weather.grid(row = 0, column = 0, padx = 10, pady = 3, sticky = 'nw')
    
    global time_city
    time_city = customtkinter.CTkLabel(mid_area, text = '', text_font = ('Roboto Medium', 10))
    time_city.grid(row = 1, column = 0, sticky = 'n', pady = 3, padx = 5)
    
    #------This is where to display celsius
    global celsius_label
    celsius_label = customtkinter.CTkLabel(weather_area, text = '', text_font = ('Poppins', 25))
    celsius_label.grid(row = 2, column = 0)
    
    global cloud_label
    cloud_label = customtkinter.CTkLabel(weather_area, text = '', text_font = ('Poppins', 7))
    cloud_label.grid(row = 3, column = 0, sticky = 'n')
    
    change_temperature = customtkinter.CTkButton(right_area, text = 'Change Temperature', text_font = ('Roboto Medium', 10), command = None)
    change_temperature.grid(row = 1, column = 0, sticky = 'ne')
    
    #-----Bottom Area Frame-----#
    label_1 = customtkinter.CTkLabel(bottom_area, text = 'Wind', text_font = ('Roboto Medium', 10))
    label_1.grid(row = 1, column = 0, pady = 3, padx = 5)
    
    label_2 = customtkinter.CTkLabel(bottom_area, text = 'Humidity', text_font = ('Roboto Medium', 10))
    label_2.grid(row = 1, column = 1, pady = 3, padx = 5)
    label_3 = customtkinter.CTkLabel(bottom_area, text = 'Speed', text_font = ('Roboto Medium', 10))
    label_3.grid(row = 1, column = 2, pady = 3, padx = 5)
    label_4 = customtkinter.CTkLabel(bottom_area, text = 'Precipitation', text_font = ('Roboto Medium', 10))
    label_4.grid(row = 1, column = 3, pady = 3, padx = 5)
    
    global wind_display, humidity_display, speed_display, precipitation_display
    
    wind_display = customtkinter.CTkLabel(bottom_area, text = 'Example', text_font = ('Roboto Medium', 10))
    wind_display.grid(row = 3, column = 0, pady = 3, padx = 5)
    humidity_display = customtkinter.CTkLabel(bottom_area, text = 'Example', text_font = ('Roboto Medium', 10))
    humidity_display.grid(row = 3, column = 1, pady = 3, padx = 5)
    speed_display = customtkinter.CTkLabel(bottom_area, text = 'Example', text_font = ('Roboto Medium', 10))
    speed_display.grid(row = 3, column = 2, pady = 3, padx = 5)
    precipitation_display = customtkinter.CTkLabel(bottom_area, text = 'Example', text_font = ('Roboto Medium', 10))
    precipitation_display.grid(row = 3, column = 3, pady = 3, padx = 5)
    
    
    
    global hide_ui
    hide_ui = customtkinter.CTkSwitch(master = right_area, text = 'Hide/Show UI', command = hide_show)
    hide_ui.grid(row = 3, column = 0)
    hide_ui.select()
    
    
    #-----Configure grid-----#
    weather_area.grid_rowconfigure(4, minsize=140)
    bottom_area.grid_rowconfigure(0, minsize=3)
    bottom_area.grid_rowconfigure(2, minsize=1)
    bottom_area.grid_rowconfigure(5, minsize=5)
    right_area.grid_rowconfigure(2, minsize=5)
    right_area.grid_rowconfigure(5, minsize=5)
    
    #-----Display Weather Update-----#
    global display_cloud
    display_cloud = customtkinter.CTkLabel(weather_area, bg = '#2F2F2F', fg = '#2F2F2F')
    display_cloud.grid(row = 4, column = 0, sticky = 'w')
    #-----Default location-----#
    display_weather('Cagayan de Oro')
    
    

#----------------------------------------#

#----------Background Wallpaper----------#

def default_background():
    """Sets Background Wallpaper depends on what local time the user have
    
    """
    if int(strftime('%I')) == 6 or int(strftime('%I')) < 13 and strftime('%p') == 'AM':
        label_place_background.config(image = weather_image[0])
    

    elif int(strftime('%I')) <= 2 and int(strftime('%I')) < 5 and strftime('%p') == 'PM':
        
        label_place_background.config(image = weather_image[1])
        
    elif int(strftime('%I')) == 5 or int(strftime('%I')) <= 12 and strftime('%p') == 'PM':
        label_place_background.config(image = weather_image[2])
        
    elif int(strftime('%I')) == 1 and int(strftime('%I')) <= 5 and strftime('%p') == 'AM':
        label_place_background.config(image = weather_image[2])

def change_mode():
    """Change mode dark/light"""
    if switch.get() == 1:
        #window.configure(bg = '#2F2F2F')
        customtkinter.set_appearance_mode("dark")
        #customtkinter.set_appearance_mode("light")
        
    else:
        #window.configure(bg = '#FFFFFF')
        customtkinter.set_appearance_mode("light")
        #customtkinter.set_appearance_mode("dark")


def local_time():
    """Displays local time clock"""
    time_display = strftime('%I:%M:%S %p')
    time_label.config(text = time_display)
    time_label.after(1000, local_time)

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

WIDTH = 780
HEIGHT = 560

window = Tk()
window.title('Weather App')
window.configure(bg = '#2F2F2F')
window.geometry(f"{WIDTH}x{HEIGHT}")
#window.geometry("720x1350")

#----------Background----------#
#----------Resizing Images----------#
pic1 = Image.open("background/sunrise.png")
pic2 = Image.open("background/sunset.png")
pic3 = Image.open("background/night_time.jpg")
image1_resize = pic1.resize((780, 560), Image.ANTIALIAS)
image2_resize = pic2.resize((780, 560), Image.ANTIALIAS)
image3_resize = pic3.resize((780, 560), Image.ANTIALIAS)

#-----Background-----#
weather_image = [ImageTk.PhotoImage(image1_resize), ImageTk.PhotoImage(image2_resize), ImageTk.PhotoImage(image3_resize)]

picture_1 = Image.open("cloud_update/mostly_cloudy.png")
picture_2 = Image.open("cloud_update/mostly_sunny.png")
picture_3 = Image.open("cloud_update/light_rain_showers.png")
picture_4 = Image.open("cloud_update/rain.png")
picture_5 = Image.open("cloud_update/partly_cloudy.png")
picture_6 = Image.open("cloud_update/clear.png")


mostly_cloudy_image = picture_1.resize((550, 230), Image.ANTIALIAS)
mostly_sunny_image = picture_2.resize((550, 230), Image.ANTIALIAS)
light_rain_showers_image = picture_3.resize((550, 230), Image.ANTIALIAS)
rain_image = picture_4.resize((550, 230), Image.ANTIALIAS)
partly_cloudy_image = picture_5.resize((550, 230), Image.ANTIALIAS)
clear_image = picture_6.resize((550, 230), Image.ANTIALIAS)




#-----Cloud Types-----#
clouds_library = [ImageTk.PhotoImage(mostly_cloudy_image), ImageTk.PhotoImage(mostly_sunny_image), ImageTk.PhotoImage(light_rain_showers_image), ImageTk.PhotoImage(rain_image), ImageTk.PhotoImage(partly_cloudy_image), ImageTk.PhotoImage(clear_image)]


label_place_background = Label(window, bg = '#2F2F2F')
    
label_place_background.place(x = 0, y = 0, relwidth = 1, relheight = 1)


#----------Frame----------#
left_body_Frame = customtkinter.CTkFrame(window, bg = '#2F2F2F', width = 500, highlightbackground = '#2F2F2F', highlightthickness = 0)
left_body_Frame.grid(row = 0, column = 0, sticky = 'nswe')

#----------left_body_Frame----------#
left_body_Frame.grid_rowconfigure(0, minsize=10)
left_body_Frame.grid_rowconfigure(1, minsize=50)
left_body_Frame.grid_rowconfigure(2, minsize=50)
left_body_Frame.grid_rowconfigure(3, minsize=50)
left_body_Frame.grid_rowconfigure(4, minsize=50)
left_body_Frame.grid_rowconfigure(5, minsize=50)
left_body_Frame.grid_rowconfigure(6, minsize=50)
left_body_Frame.grid_rowconfigure(7, minsize=90)
left_body_Frame.grid_rowconfigure(5, weight = 1)
left_body_Frame.grid_rowconfigure(8, minsize=5)
left_body_Frame.grid_rowconfigure(10, minsize=10)
left_body_Frame.grid_rowconfigure(12, minsize=20)
left_body_Frame.grid_columnconfigure(0, minsize=50)

#----------Label----------#

category = customtkinter.CTkLabel(left_body_Frame, text = 'Categories', text_font = ('Roboto Medium', 10))
category.grid(row = 1, column = 0)

time_label = customtkinter.CTkLabel(left_body_Frame, text = '00:00:00', text_font = ('Roboto Medium', 10))
time_label.grid(row = 2, column = 0)

#-----Radio Button-----#

Radio_value = IntVar(value = 0)

#-----Mark Buttons-----#
mark_list = []#Insert Marked Locations

set_mark = customtkinter.CTkButton(left_body_Frame, fg_color = ("gray75", "gray30"), text_font = ('Roboto Medium', 10), command = None, state = DISABLED)
set_mark.grid(row = 6, column = 0)

clear_mark = customtkinter.CTkButton(left_body_Frame, fg_color = ("gray75", "gray30"), text_font = ('Roboto Medium', 10), command = None, state = DISABLED)
clear_mark.grid(row = 7, column = 0)


timer_button = customtkinter.CTkRadioButton(left_body_Frame, text = 'Timer     ', text_font = ('Roboto Medium', 10), variable = Radio_value, value = 2, state = DISABLED)
timer_button.grid(row = 3, column = 0)

map_button = customtkinter.CTkRadioButton(left_body_Frame, text = 'Map        ', text_font = ('Roboto Medium', 10), variable = Radio_value, value = 3, command = map_view_area)
map_button.grid(row = 4, column = 0)

weather_button = customtkinter.CTkRadioButton(left_body_Frame, text = 'Weather', text_font = ('Roboto Medium', 10), variable = Radio_value, value = 4, command = weather_area)
weather_button.grid(row = 5, column = 0)

#----------The Search Button----------#

search_button = customtkinter.CTkButton(left_body_Frame, text = 'Search', fg_color = ("gray75", "gray30"), text_font = ('Roboto Medium', 10), command = None)
search_button.grid(row = 9, column = 0)

#-----Entry-----#
city_entry = customtkinter.CTkEntry(left_body_Frame, placeholder_text = 'Enter City/Region', width = 160, height = 50, text_font = ('Roboto Medium', 10))
city_entry.grid(row = 8, column = 0, pady = 10, padx =
 10)

#-----Dark mode/Light mode-----#
switch = customtkinter.CTkSwitch(master = left_body_Frame, text = 'Dark Mode', command = change_mode)
switch.grid(row = 11, column = 0, padx = 10, pady = 10, sticky = 'sw')

#Default Setting
switch.select()
default_background()
map_button.select()
weather_button.select()
weather_area()


#Run Local Time
local_time()

#window.overrideredirect(1)
window.resizable(False, False)
window.mainloop()



"""        Categories

    
    Timer
    Weather
    World Map
    
    
    Dark Mode(Optional)
    Analog Clock(Optional)[Clock Family]
    
    
    
    
    Add background depending what type of weather(Pics must be seasons)
    
    Add Transparency(Optional)
    
    Celsius To Fahrenheit
    Formula:
    (0°C × 9/5) + 32 = 32°F
    
    Fahrenheit To Celsius
    Formula:
    (32°F − 32) × 5/9 = 0°C

    


"""