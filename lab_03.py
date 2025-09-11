#This function has the user enter their username
def get_username():
    username = input("Enter your username: ")
    username = username.strip()
    print("Your username is:", username.upper())
    return username
#This function gets the group name inputted by the user
def get_group():
    group_name = input("Enter your group name: ")
    group = group_name.strip()
    print("Your group name is:", group.upper())
    return group_name
#This function gets a message inputted by the user
def get_message():
    message = input("Enter your message: ")
    message = message.strip()
    print("Your message is:", message)
    return message

#Calls the functions to start the program
#username = get_username()
#get_group()
#get_message()

import lab_chat as lc

def initialize_chat():
    username = get_username()
    group = get_group()
    node = lc.get_peer_node(username)
    lc.join_group(node, group)
    channel = lc.get_channel(node,group)
    return channel

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

start_chat()