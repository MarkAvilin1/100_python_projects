weather_list = {
    'Monday': 53.6,
    'Tuesday': 57.2,
    'Wednesday': 59.0,
    'Thursday': 57.2,
    'Friday': 69.8,
    'Saturday': 71.6,
    'Sunday': 75.2
}

# list_f_v = [(i * 9 / 5) + 32 for i in weather_list.values()]
# list_f_k = [i for i in weather_list]

weather_f = {k: round((v * 9 / 5) + 32, 2) for (k, v) in weather_list.items()}

print(weather_f)
