def Get_Weather(city,dateT):
  def GetWeatherDict(cityname,dat):
    try:
        import requests
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


        
        def SplitDate(d):
          listdat=[int(d[0:4]),int(d[5:7]),int(d[8:10])]
          return listdat

        def UNIX_TimeConv(datelist):
          import datetime
          datentime=datetime.datetime(datelist[0],datelist[1],datelist[2],00,00,00)
          UNIX_dateTime=datentime.timestamp()
          return UNIX_dateTime
        
        dtn=SplitDate(dat)
        dt=UNIX_TimeConv(dtn)
      
        wAPIkey="" #API key for Open weather Map history API
        url = f'https://history.openweathermap.org/data/3.0/history/timemachine?lat={lat}&lon={lon}&dt={dt}&appid={wAPIkey}'
        response = requests.get(url)

        d=dict(response["main"])
        del d["temp_min"]
        del d["temp_max"]
        d["windspeed"]=response["wind"]["speed"]
        d["Clouds"]=response["clouds"]["all"]
        d["rain"]=response["rain"]["1h"]
        return d
      
    except Exception as e:
        print("Error Occured :"+str(e))
        return

  
  if date>=dateOfTdy:
    class dayWeather:
      def __init__(self,date1):
        #attributes
        self.date=date1
        WeatherData=GetWeatherDict(city,date1)
        #add api here to fetch the bellow values
        h=WeatherData["humidity"]     #Humidity
        t=WeatherData["temp"]    #Temperature
        fl=WeatherData["feels_like"]    #FeelsLike
        ws=WeatherData["windspeed"]    #Windspeed
        cl=WeatherData["Clouds"]    #Cloud
        pr=WeatherData["pressure"]  #Pressure
        rn=WeatherData["rain"]      #Rainfall
        
    # write code here
  
    #add date time function to take 5 dates before current date
    d1=dayWeather(dateOfTdy-5) # 5 day before today
    d2=dayWeather(dateOfTdy-4) # 4 day before today
    d3=dayWeather(dateOfTdy-3) # 3 day before today
    d4=dayWeather(dateOfTdy-2) # 2 day before today
    d5=dayWeather(dateOfTdy-1) # 1 day before today
  
    # Getting date Range
    import datetime
    from datetime import date as dt                            #Import date from datetime library
    def loop(n):
        if n<=1:
            if n<=0:                                        
                print('The weather on '+date2+' is:')      #In case the date is before current day
            return 1                                     
        else:
            base=dt.today()                              #alloting base date
            print(base+datetime.timedelta(days=n))       #printing the days
            return n*loop(n-1)                              
    date1=str(dt.today())                                #Taking Today's Date as Date1
    date2=input('Enter the second date: ')                 #Taking date entered as Date2
    datetime1=dt.fromisoformat(date1)                    #Taking date1 in numerical form
    datetime2=dt.fromisoformat(date2)                    #Taking date2 in numerical form
    x=str(datetime2-datetime1)                             #Substracting two dates
    l=x.split()                                            #spliting x into ['No of days','days','00:00:00']                                 
    print(loop(int(l[0])))                                 #considering No of days in the list and calling the function from the loop function
  
    #Weighted average calculation
    def weightedAvg(d1,d2,d3,d4,d5):
      d=((d11*9)+(d2*6)+(d3*5)+(d4*4)+(d5*2))/26
      return d
  
    # Function to calculate parametre
    def paramCalc(n, d1, d2, d3, d4, d5):
      if n == 1:
          return d1
      elif n == 2:
          return d2
      elif n == 3:
          return d3
      elif n == 4:
          return d4
      elif n == 5:
          return d5
      else:
          # Recursively calculate the parameter for day n as the average of the past 5 days
          param_n_minus_1 = paramCalc(n - 1, d1, d2, d3, d4, d5)
          param_n_minus_2 = paramCalc(n - 2, d1, d2, d3, d4, d5)
          param_n_minus_3 = paramCalc(n - 3, d1, d2, d3, d4, d5)
          param_n_minus_4 = paramCalc(n - 4, d1, d2, d3, d4, d5)
          param_n_minus_5 = paramCalc(n - 5, d1, d2, d3, d4, d5)
          return weightedAvg(param_n_minus_1, param_n_minus_2, param_n_minus_3, param_n_minus_4 ,param_n_minus_5)
    
    h1=parammCalc(n,d1.h,d2.h,d3.h,d4.h,d5.h)
    t1=parammCalc(n,d1.t,d2.t,d3.t,d4.t,d5.t)
    fl1=parammCalc(n,d1.fl,d2.fl,d3.fl,d4.fl,d5.fl)
    ws1=parammCalc(n,d1.ws,d2.ws,d3.ws,d4.ws,d5.ws)
    cl1=parammCalc(n,d1.cl,d2.cl,d3.cl,d4.cl,d5.cl)
    pr1=parammCalc(n,d1.pr,d2.pr,d3.pr,d4.pr,d5.pr)
    rn1=parammCalc(n,d1.rn,d2.rn,d3.rn,d4.rn,d5.rn)
    
  else:
    # send api request to get data and unpack the result and map to the respective elements
    WeatherData=GetWeatherDict(city,dateT)
    #add api here to fetch the bellow values
    h=WeatherData["humidity"]     #Humidity
    t=WeatherData["temp"]    #Temperature
    fl=WeatherData["feels_like"]    #FeelsLike
    ws=WeatherData["windspeed"]    #Windspeed
    cl=WeatherData["Clouds"]    #Cloud
    pr=WeatherData["pressure"]  #Pressure
    rn=WeatherData["rain"]      #Rainfall
    
  result={
    "Humidity":h1,
    "Temp":t1,
    "FeelsLike":fl1,
    "Wind":ws1,
    "Cloud":cl1,
    "Pressure":pr1,
    "Rain":rn1
    }
  return result

  
