import pandas

# data = pandas.read_csv('weather_data.csv')

# temp_list = data['temp'].to_list()

# avg = sum(temp_list) / len(temp_list)
#
# avg = data['temp'].mean()
# max_temp = data['temp'].max()
#
# print(avg)
# print(max_temp)

# print(data[data['temp'] == data['temp'].max()])

# monday = data[data['day'] == 'Monday']
# print(monday.temp * 1.8 + 32)

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# data.fillna({'Primary Fur Color': '-'})['Primary Fur Color']

# fur_color = data['Primary Fur Color']
fur_color = data.fillna({'Primary Fur Color': '-'})['Primary Fur Color']

colors_s = fur_color.unique()
colors_l = colors_s.tolist()

# print(data.count(axis='Primary Fur Color'))
# print(fur_color.count('white'))

res_dict = {'fur color': [], 'count': []}
for color in colors_s:
    if color != '-':
        count = len(data[data['Primary Fur Color'] == color])
        res_dict['fur color'].append(color)
        res_dict['count'].append(count)

res_data_frame = pandas.DataFrame.from_dict(res_dict)
res_data_frame.to_csv('squirrel_count.csv')

print(res_data_frame)

