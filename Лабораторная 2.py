import requests
city = "Moscow, RU"
appid = "06d8ae120069f60a21c9e317652e9457"
res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Ваш град прожувания:", city)
print("____________________________")
print("Погода на севодни:")
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:",  data['main']['temp'],  "ГРАДУСОВ ПО ЦЕЛЬСИЮ ")
print("Минимальная температура:", data['main']['temp_min'], "ГРАДУСОВ ПО ЦЕЛЬСИЮ ")
print("Максимальная температура:", data['main']['temp_max'], "ГРАДУСОВ ПО ЦЕЛЬСИЮ ")
print("Скорость ветренных явлений:", data['wind']['speed'], "м/с")
print("Видимость невидимостей:", data['visibility'], "м")
res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("____________________________")
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемперадура <", "ЯБЛОКИ",
          '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные гуслопайки <",
          i['weather'][0]['description'], ">", "\r\nСкорость ветродуя <", i['wind']['speed'], "м/с >",
          "\r\nВидимость невиданных невидимостей <", i['visibility'], "ОАО МММ >")
    print("()()()263.ТРАКТОР.RF()()()")
print("()()()263.ТРАКТОР.RF()()()")