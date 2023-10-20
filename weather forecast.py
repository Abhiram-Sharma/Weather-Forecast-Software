theme_menu=['SandyBeach','Light brown 13','python','black','random']

import PySimpleGUI as sg

# Define the layout
layout = [
    [sg.Text('City:'), sg.Input(key='city')],
    [sg.Text('Country:'), sg.Input(key='country')],
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
        city = values['city']
        country = values['country']

        # fetch the weather data

        weather_data = "Weather data for " + city + ", " + country
        print(weather_data)

window.close()