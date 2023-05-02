import requests
import auth
import datetime as dt

TODAY = dt.date.today().strftime('%Y%m%d')

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{auth.USERNAME}/graphs"
POST_ENDPOINT = f"{GRAPH_ENDPOINT}/{auth.GRAPH_ID}"
DELETE_ENDPOINT = f"{POST_ENDPOINT}/{auth.DELETE_DATE}"
UPDATE_ENDPOINT = f"{POST_ENDPOINT}/{auth.UPDATE_DATE}"


headers = {
    "X-USER-TOKEN": auth.TOKEN
}

user_params = {
    "token": auth.TOKEN,
    "username": auth.USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_params = {
    "id": auth.GRAPH_ID,
    "name": "Pages Tracker",
    "unit": "pages",
    "type": "int",
    "color": "shibafu",
}

post_params = {
    "date": TODAY,
    "quantity": input("How many pages have you read today?: "),
}

update_params = {
    "quantity": "0"
}

# Create user
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# Create a graph
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)

# Post, Delete, Update

response = requests.post(url=POST_ENDPOINT, json=post_params, headers=headers)
print(response.text)

# response = requests.post(url=DELETE_ENDPOINT, headers=headers)
# print(response.text)

# response = requests.post(url=UPDATE_ENDPOINT, params=update_params, headers=headers)
# print(response.text)
