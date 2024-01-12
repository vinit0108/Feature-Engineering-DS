import requests

# Replace these variables with your actual credentials and workspace ID
username = 'your_username'
password = 'your_password'
workspace_id = 'your_workspace_id'

#  API URLs
auth_url = 'https://authauthenticate'
base_url = 'https://api/2/0/workspaces/'

# Headers for authentication
auth_headers = {
    'Authorization': 'Basic ' + username + ':' + password,
    'Content-Type': 'application/json'
}

# Function to authenticate and get the token
def authenticate():
    response = requests.post(auth_url, headers=auth_headers)
    if response.status_code == 200:
        return response.json()['tokenInfo']['tokenValue']
    else:
        print('Authentication failed')
        return None

# Function to list models
def list_models(token):
    headers = {
        'Authorization': 'AuthToken ' + token,
        'Content-Type': 'application/json'
    }
    response = requests.get(base_url + workspace_id + '/models', headers=headers)
    if response.status_code == 200:
        models = response.json()['models']
        for model in models:
            print(f"Model ID: {model['id']}, Name: {model['name']}")
    else:
        print('Failed to fetch models:', response.text)

# Authenticate and list models
token = authenticate()
if token:
    list_models(token)
