import pandas
import datetime as dt

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

# data = pandas.read_csv('01.11.202239_lat.csv', sep=';')
# for (index, row) in data.iterrows():
#     act_list = [{row.letter: row.code} for (index, row) in data.iterrows()]
#     print(row.Amount)
#     # print(row[index])
#     print(row[index][6])
# print(data)

data = pandas.read_csv('01.11.202239_lat.csv', sep=';', decimal=',', parse_dates=['ActDate'], dayfirst=True)
for row in data.itertuples(index=False):
    print(row)
    col_names = [row[i] for i in range(0, len(row))]
    # act_list = [{row.letter: row.code} for (index, row) in data.iterrows()]
    print(type(row[0]))
    print(row[0].month)
    print(row.ContrN)
print(col_names)
    # print(row.Amount)
    # print(row[index])



