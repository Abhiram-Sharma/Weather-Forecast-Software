The Following Document is to provide a brief description of the Weather Forecasting Software.

It is a GUI based Weather prediction software, based on python.
The following Modules have been used in the Source Code :
	- PySimpleGUI (for providing a clean user interface for the Software)
	- Requests (for Integrating APIs)
	- DateTime (for Computing date and time parameters)

APIs Used:
	- GeoNames (for obtaining latitude and longitue of the City)
	- Open-Meteo (To get Historical Data of weather parameters, used to predict the future weather

Key-Programming-Concepts Used :
	- Functions
	- API requests
	- Recursions
	- Object Oriented Programming
	- Graphical User Interface
	- Weighted Average

Files :
	- Read_Me.txt :
		Brief Information on the Source Code
	- Get_Weatherfunction.py :
		contains Main Function with multiple sub functions to fetch values to display
	- weather forecast.py :
		The Primary Program to Execute the Software, contains the GUI to Integrate with the Main Function
	- weather forecast.exe :
		An Executable file with  pre loaded libraries, compiled using psg compiler.
		helps to avoid hazzels in running the program without additionaly installing other modules.
Note :
    if the executable file fails to start, Kindly Install the following Libraries using the bellow commands in CMD
        - pip install pysimplegui
------------------------------------------------------------------------------------------------------------------------

Project By:
	- Abhiram Sharma (23BDS1093)
	- Mohammad Afzal Khan (23BDS1163)
