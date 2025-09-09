#This function has the user enter their username
def get_username():
    username = input("Enter your username: ")
    username = username.strip()
    print("Your username is:", username.upper())

#This calls the function
get_username()

rows = 10
columns = 10

for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        product = i * j
        print(f"{i} x {j} = {product}")
    print()