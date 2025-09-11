
def get_peer_node(username): **function name is get_peer_node**
    n = Pyre(username)
    #n.set_header("CHAT_Header1","example header1")
    #n.set_header("CHAT_Header2","example header2")
    n.start()
    return n

# **username: This is most likely the users inputted name**

# **Returns n. n seems to be an alias for Pyre**

def join_group(node, group): #function name is join_group 
    node.join(group)
    print(f"Joined group: {group}") #function name is join_group

# **No parameters**

# **Returns nothing. it seems to join the user into a group and prints that they joined into the group.**

def chat_task(ctx, pipe, n, group): **function name is chat_task** 
    poller = zmq.Poller()
    poller.register(pipe, zmq.POLLIN)
    # print(n.socket())
    poller.register(n.socket(), zmq.POLLIN)
    # print(n.socket())
    while(True):
        items = dict(poller.poll())
        # print(n.socket(), items)
        if pipe in items and items[pipe] == zmq.POLLIN:
            message = pipe.recv()
            # message to quit
            if message.decode('utf-8') == "$$STOP":
                break
            print(f"YOU: {message.decode('utf-8')}")
            n.shouts(group, message.decode('utf-8'))
        else:
            cmds = n.recv()
            msg_type = cmds.pop(0).decode('utf-8')
            peer_id = uuid.UUID(bytes=cmds.pop(0))
            peer_username = cmds.pop(0).decode('utf-8')
            match msg_type:
                case "SHOUT":
                    intended_group = cmds.pop(0).decode('utf-8')
                    if intended_group == group:
                        # print(f"{peer_username}({peer_id}): {cmds}")
                        print(f"{peer_username}: {cmds.pop(0).decode('utf-8')}")
                case "ENTER":
                    headers = json.loads(cmds.pop(0).decode('utf-8'))
                    # print(f"NODE_MSG HEADERS: {headers}")
                    # for key in headers:
                    #    print("key = {0}, value = {1}".format(key, headers[key]))
                    # print( f"{peer_username}({peer_id}): is now connected." )
                    print( f"{peer_username}: is now connected." )
                case "JOIN":
                    #print( f"{peer_username}({peer_id}): joined {cmds.pop(0).decode('utf-8')}." )
                    print( f"{peer_username}: joined {cmds.pop( 0 ).decode( 'utf-8' )}." )
            # print(f"NODE_MSG CONT: {cmds}")
    n.stop()


# ctx: Unsure

# pipe: Unsure

# n: It looks like it stops the loop 

# group: The group selected to join

# It does not return anything. It probably makes the chat system work.

def get_channel(node, group): **function name is get_channel**
    ctx = zmq.Context()
    return zhelper.zthread_fork(ctx, chat_task, n=node, group=group)

# node: Another Alias for n?

# group: The selected group

# It returns zhelper.zthread_fork(ctx, chat_task, n=node, group=group)

# My best guess is that it finds the correct channel to be in