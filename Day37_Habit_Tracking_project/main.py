import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

# #CREATE USER
USERNAME = ""
TOKEN = ""

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}

# response = requests.post(url = pixela_endpoint, json = user_params)
# print(response.text)

# #Create GRAPH
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id":"pythoncourse1",
#     "name":"Learning Graph",
#     "unit":"hours",
#     "type":"int",
#     "color":"ajisai"
# }
#
# graph_headers = {
#     "X-USER-TOKEN":TOKEN
# }
#
# response = requests.post(url = graph_endpoint, json = graph_config, headers = graph_headers)
# print(response.text)

# #DELETE GRAPH
# graph_to_delete = "pythoncourse1"
# graph_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_to_delete}"
#
# graph_delete_headers = {
#     "X-USER-TOKEN":TOKEN
# }
#
# response = requests.delete(url = graph_delete_endpoint, headers = graph_delete_headers)
# print(response.text)

# #POST PIXEL
# add_pixel_graph = "pythoncourse1"
# add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{add_pixel_graph}"
#
# add_pixel_headers = {
#     "X-USER-TOKEN":TOKEN
# }
#
# today = datetime(year = 2024, month = 4,day = 21)
#
# add_pixel_parameters = {
#     "date":today.strftime("%Y%m%d"),
#     "quantity":"4"
# }
#
# response = requests.post(url = add_pixel_endpoint, json = add_pixel_parameters, headers = add_pixel_headers)
# print(response.text)


