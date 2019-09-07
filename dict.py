weather= {
    "city": "Москва",
    "temperature": "20"
}
print(weather)
temperature=int(weather["temperature"])
print(temperature-5)
print(len(weather))
print(weather.get("country", "Россия"))
weather["date"]="27.05.2019"
print(weather)
print(len(weather))