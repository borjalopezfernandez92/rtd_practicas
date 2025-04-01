import requests, json

with open('headers.txt', 'r') as f:
    xChallengerCode = f.read().strip()
    
headers = {
    "X-Challenger": xChallengerCode
}

def menu():
    menuInput = input(f"Select challenge: (1)New Challenge\n(2)Check challenge Challenge\n(3)Get \\todos\n(4)Get todos id\n(5)Get Done\n(6)Post new Todo")

    if int(menuInput) == 1:
        newChallenge()
    elif int(menuInput) == 2:
        getChallenges()
    elif int(menuInput) == 3:
        getTodos()
    elif int(menuInput) == 4:
         getTodosId()
    elif int(menuInput) == 5:
         getDone()
    elif int(menuInput) == 6:
         postTodo()
         
        
def newChallenge():
    headers_dict = {}

    json_headers = ['Report-To', 'Nel']

    url = "https://apichallenges.eviltester.com/challenger"
    response = requests.post(url)

    xChallenger = response.headers['X-Challenger']
    with open('headers.txt', 'w') as f:
        f.write(xChallenger)
        f.close()
    print(f"Obtenido y grabado código xChallenger -->{xChallenger} en headers.txt")

def getChallenges():

    url = "https://apichallenges.eviltester.com/challenges"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
            print(response.json())
    else:
        raise Exception(f"Failed request: {response.status_code}")
    
def getTodos():
    url = 'https://apichallenges.eviltester.com/todos'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
            print(response.json())
    else:
        raise Exception(f"Failed request: {response.status_code}")

def getTodosId():
    id = input(f"Inserta el id que quieras comprobar: ")
    url = f'https://apichallenges.eviltester.com/todos/{id}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
            print(response.json())
    else:
        raise Exception(f"Failed request: {response.status_code}")

def getDone():
    url = "https://apichallenges.eviltester.com/todos?doneStatus=False"
    response = requests.get(url, headers=headers)

    
    if response.status_code == 200:
            print(response.json())
    else:
        raise Exception(f"Failed request: {response.status_code}")

def postTodo():
    id = input("Id a modificar: ")
    url =f"https://apichallenges.eviltester.com/todos/{id}"

    headers = {
         "Content-Type": "application/json",
         "X-Challenger": "1c02fb12-8abf-4ab4-9b84-638edd252ffa"
    }
    data = {
        'title': "THIS",
        'doneStatus': False,
        'description': "Test Description"
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
            print(response.json())
    else:
        raise Exception(f"Failed request: {response.status_code}")
    
menu()