USERS = {'user1': 'password1', 'user2': 'password2'}

name_input = input("Enter your username: ")
pass_input = input("Enter your password: ")

if name_input in USERS and USERS[name_input] == pass_input:
    print(f" Welcome Back , {name_input} ! ")
else:
    print("Wrong username or password!!")