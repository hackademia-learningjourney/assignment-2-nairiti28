import json

def dumping(data):
    with open('info.json','w') as file:
        json.dump(data,file)

def loading():
    try:
        with open('info.json','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return{}

print('Press 1 to Sign Up and 2 to Sign In')
reply=int(input('Enter your option: '))
if reply==1:
    print('SIGN UP')
    username=input('Enter your username: ')
    password=input('Enter your password: ')
    mobile=int(input('Enter your mobile number: '))
    data = loading()
    data[username]={'password': password, 'mobilenum':mobile}
    dumping(data)
elif reply==2:
    print('SIGN IN')
    username=input('Enter your username: ')
    password=input('Enter your password: ')
    data=loading()
    if(username in data and data[username]['password']==password):
            print("Welcome to the Program")
            print("Your mobile number: ", data[username]['mobilenum'])
    else:
        print('Invalid credentials')
else:
    print('Enter 1 or 2 only')
