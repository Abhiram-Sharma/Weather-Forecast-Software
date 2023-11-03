import requests
from datetime import date
import datetime

def Get_Weather(city,dateT):
  
  def SplitDate(d):
    listdat=[int(d[0:4]),int(d[5:7]),int(d[8:10])]
    return listdat
  
  def GetWeatherDict(cityname,dat):
        
        geonames_username = 'abaf2023'
        city_name = cityname

        url = f'http://api.geonames.org/searchJSON?q={city_name}&maxRows=1&username={geonames_username}'
        response = requests.get(url)
        

        if response.status_code == 200:
            data = response.json()
            if data['totalResultsCount'] > 0:
                city_data = data['geonames'][0]
                lat = city_data['lat']
                lon = city_data['lng']
            else:
                print(f"City '{city_name}' not found.")
        else:
            print(f"Request failed with status code {response.status_code}")

        stdt=dat
        endt=stdt
        url = f'https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={stdt}&end_date={endt}&daily=temperature_2m_mean,apparent_temperature_mean,rain_sum,windspeed_10m_max&timeformat=unixtime&timezone=Asia%2FSingapore'
        response = requests.get(url)
        a=response.json()
        return a["daily"]

  #get Todays date in yyyy-mm-dd as string
  
  dateOfTdy=date.today()
  
  if date(SplitDate(dateT)[0],SplitDate(dateT)[1],SplitDate(dateT)[2])>=(dateOfTdy-datetime.timedelta(days = 10)):
    
    class dayWeather:
      def __init__(self,date1):
        #attributes
        self.date=date1
        WeatherData=GetWeatherDict(city,date1)
        #add api here to fetch the bellow values
        self.t=WeatherData['temperature_2m_mean'][0]    #Temperature
        self.fl=WeatherData['apparent_temperature_mean'][0]    #FeelsLike
        self.ws=WeatherData['windspeed_10m_max'][0]    #Windspeed
        self.rn=WeatherData['rain_sum'][0]      #Rainfall
        
    # write code here
    
  
    #add date time function to take 5 dates before current date
    
    d1=dayWeather(str(date.today()-datetime.timedelta(days = 14))) # 5 day before today
    d2=dayWeather(str(date.today()-datetime.timedelta(days = 13))) # 4 day before today
    d3=dayWeather(str(date.today()-datetime.timedelta(days = 12))) # 3 day before today
    d4=dayWeather(str(date.today()-datetime.timedelta(days = 11))) # 2 day before today
    d5=dayWeather(str(date.today()-datetime.timedelta(days = 10))) # 1 day before today
  
    # Getting date Range
    from datetime import date as dt                            #Import date from datetime library
    def NoDays(date2):                   
      date1=str(dt.today()-datetime.timedelta(days=1))                                #Taking Today's Date as Date1
      datetime1=dt.fromisoformat(date1)                    #Taking date1 in numerical form
      datetime2=dt.fromisoformat(date2)                    #Taking date2 in numerical form
      x=str(datetime2-datetime1)                             #Substracting two dates
      l=x.split()                                            #spliting x into ['No of days','days','00:00:00']                                 
      return int(l[0]) if int(l[0])>0 else 0
    
    #Weighted average calculation
    def weightedAvg(d1,d2,d3,d4,d5):
      d=((d1*9)+(d2*6)+(d3*5)+(d4*4)+(d5*2))/26
      return d
  
    # Function to calculate parametre
    def paramCalc(n, d1, d2, d3, d4, d5):
      if n == 1:
          if d1==None:
            return 0
          else:
            return d1
      elif n == 2:
        if d2==None:
          return 0
        else:
          return d2
      elif n == 3:
        if d3==None:
          return 0
        else:
          return d3
      elif n == 4:
        if d4==None:
          return 0
        else:
          return d4
      elif n == 5:
        if d5==None:
          return 0
        else:
          return d5
      else:
          # Recursively calculate the parameter for day n as the average of the past 5 days
          param_n_minus_1 = paramCalc(n - 1, d1, d2, d3, d4, d5)
          param_n_minus_2 = paramCalc(n - 2, d1, d2, d3, d4, d5)
          param_n_minus_3 = paramCalc(n - 3, d1, d2, d3, d4, d5)
          param_n_minus_4 = paramCalc(n - 4, d1, d2, d3, d4, d5)
          param_n_minus_5 = paramCalc(n - 5, d1, d2, d3, d4, d5)
          return weightedAvg(param_n_minus_1, param_n_minus_2, param_n_minus_3, param_n_minus_4 ,param_n_minus_5)
    
    #define n here, number of days between today and the target day +5
    n=NoDays(dateT)+14

    t1=paramCalc(n,d1.t,d2.t,d3.t,d4.t,d5.t)
    fl1=paramCalc(n,d1.fl,d2.fl,d3.fl,d4.fl,d5.fl)
    ws1=paramCalc(n,d1.ws,d2.ws,d3.ws,d4.ws,d5.ws)
    rn1=paramCalc(n,d1.rn,d2.rn,d3.rn,d4.rn,d5.rn)
    
  else:
    # send api request to get data and unpack the result and map to the respective elements
    WeatherData=GetWeatherDict(city,dateT)
    #add api here to fetch the bellow values
    t1=WeatherData['temperature_2m_mean'][0]    #Temperature
    fl1=WeatherData['apparent_temperature_mean'][0]    #FeelsLike
    ws1=WeatherData['windspeed_10m_max'][0]    #Windspeed
    rn1=WeatherData['rain_sum'][0]      #Rainfall
    
  result={
    "Temp":t1,
    "FeelsLike":fl1,
    "Wind":ws1,
    "Rain":rn1
    }
  return result
