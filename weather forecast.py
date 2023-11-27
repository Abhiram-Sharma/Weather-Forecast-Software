# theme_menu=['SandyBeach','Light brown 13','python','black','random']
import os
try:
    import PySimpleGUI as sg
except:
    os.system(f'cmd /c "pip install PySimpleGUI"')
    import PySimpleGUI as sg
try:
    import requests
except:
    os.system(f'cmd /c "pip install requests"')
    import requests

from Get_Weatherfunction import Get_Weather as GW

# Define the layout
layout = [
    [sg.Text('City :'), sg.InputText(key='city')],
    [sg.Text('Date :'), sg.InputText(key='Date'),sg.CalendarButton("Select Date",close_when_date_chosen=True,target="Date",format='%Y-%m-%d')],
    [sg.Button('Get Weather'), sg.Button('Exit')],
    [sg.Output(size=(80, 20))]
]

# Create the window
sg.theme("SandyBeach")
window = sg.Window('Weather Forecast', layout)


# Event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Get Weather':
        city = values['city'].lower()
        DateT = values['Date']

        # fetch the weather data
        '''
        result={
            "Temp":t1,
            "FeelsLike":fl1,
            "Wind":ws1,
            "Rain":rn1
            }
        '''
        
        city=city.capitalize()
        try:
            wdata=GW(city,DateT)
            print(f"Weather Data for {city} on {DateT} :")
            print(f"> Lattitude {wdata['lat']}° Longitude {wdata['lon']}°")
            print(f"> Windspeed : {round(wdata['Wind']*5/18)} m/s")
            print(f"> Rain : {round(wdata['Rain'])} mm")
            print(f"> Temperature : {round(wdata['Temp'])}°C")
            print(f"> Feels Like : {round(wdata['FeelsLike'])}°C\n")
        except:
            print(f"{city} does not exist\n")
        

window.close()
