# imports
import tkinter
import requests


api_key = 'f16a3084be77a020f9139a17538ae497'

# inistialise a window
root = tkinter.Tk()

# title
root.title('Weather App')

# geometry
# root.geometry('365x100')

def get_city_weather():
    try:
        city = my_city.get()
        api_call = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        weather_data = requests.get(api_call).json()['main']
        my_weather = 'temp is ' + str(weather_data['temp']) +' pressure ' + str(weather_data['pressure']) + " Humidity is " + str(weather_data['humidity'])
        display.delete('1.0',tkinter.END)
        display.insert('1.0',my_weather)
    except KeyError:
        message = 'PLease enter a valid city name'
        display.delete('1.0',tkinter.END)
        display.insert('1.0',message)



# label
city_label = tkinter.Label(root, text='City Name')
city_label.grid(row=0,column=0)

# entry
my_city=tkinter.StringVar()
city_entry = tkinter.Entry(root, textvariable=my_city)
city_entry.grid(row=0, column=1)

# button
my_button = tkinter.Button(root, text='Submit', command=get_city_weather)
my_button.grid(row=0, column=2)

# display
display = tkinter.Text(root, height=4, width=45)
display.grid(row=1,column=0, columnspan=3)

# mainloop
root.mainloop()