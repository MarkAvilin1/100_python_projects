from datetime import datetime
import requests

USERNAME = "mark1"
TOKEN = "a1s2d3f4g5"
ID = "graph1"
headers = {
    "X-USER-TOKEN": TOKEN
}
today = datetime.now().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = F"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "shibafu"
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/{ID}"
# post_pixel_config = {
#     "date": today,
#     "quantity": "18.7"
# }
# response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{post_pixel_endpoint}/{today}"
update_pixel_config = {
    "quantity": "11.3"
}
response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
print(response.text)

delete_pixel_endpoint = f"{post_pixel_endpoint}/{today}"
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)

# delete_user_endpoint = "https://pixe.la/v1/users/mark"
# response = requests.delete(url=delete_user_endpoint, headers=headers)
# print(response.text)
