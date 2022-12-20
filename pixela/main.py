import requests
import datetime as dt


pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "dzmitry"
TOKEN = "wed34f-5%^dd"
GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "weight graph",
    "unit": "kg",
    "type": "float",
    "color": "ajisai"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Create pixel section

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# data_date = dt.datetime.now()
data_date = dt.datetime.strptime("18.12.2022", "%d.%m.%Y")

pixel_post_config = {
    "date": data_date.strftime('%Y%m%d'),
    "quantity": "92.4"
}

# response = requests.post(url=pixel_post_endpoint, json=pixel_post_config, headers=headers)
# print(response.text)

# Update section

data_date = dt.datetime.strptime("19.12.2022", "%d.%m.%Y")
new_value = "93.1"
pixel_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{data_date.strftime('%Y%m%d')}"

pixel_put_config = {
    "quantity": new_value
}

# response = requests.put(url=pixel_put_endpoint, json=pixel_put_config, headers=headers)
# print(response.text)

# Delete section

data_date = dt.datetime.strptime("18.12.2022", "%d.%m.%Y")
pixel_del_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{data_date.strftime('%Y%m%d')}"

response = requests.delete(url=pixel_del_endpoint, headers=headers)
print(response.text)


