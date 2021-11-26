from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.commons.exceptions import NotFoundError

import tkinter as tk

window = tk.Tk()
window.title("Weather detector")
window.resizable(width='FALSE', height='FALSE')
window.geometry("400x500")
window["bg"] = "SlateBlue2"

config_dict = get_default_config()
config_dict['language'] = 'ru'  
owm = OWM('6d00d1d4e704068d70191bad2673e0cc')

mgr = owm.weather_manager()

def getcity():
    city = entry.get()
    if city:
    	observation = mgr.weather_at_place(city)
    	w = observation.weather
    	temp = w.temperature('celsius')["temp"]
    	result.config(text = (f"В городе {city} сейчас:\n {w.detailed_status} \n Температура равна {temp} градусов."))
	#except NotFoundError:
    	#result.config(text = 'Не найдено место: {city}')


none = ' '

metka = tk.Label(text = 'Введите город:')
metka.pack()
metka["bg"] = "SlateBlue2"

entry = tk.Entry(width = 50)
entry.pack()

knopka = tk.Button(text = 'Узнать погоду', width = 30, height = 3, command = getcity)
knopka.place(x = 89, y = 50)
knopka["bg"] = "mediumpurple1"

result = tk.Label(text = none, font = ("Helvetica", "10", "italic underline"))
result.place(x = 15, y = 130)
result["bg"] = "SlateBlue2"

window.mainloop()