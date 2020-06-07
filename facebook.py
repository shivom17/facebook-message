
import fbchat 
from getpass import getpass 
username = str(raw_input("User: "))
client = fbchat.Client(username, getpass()) 
no_of_friends = int(raw_input("Number of friends: ")) 
for i in xrange(no_of_friends): 
    name = str(raw_input("Name: ")) 
    friends = client.getUsers(name)
    friend = friends[0] 
    msg = str(raw_input("Hello world"))
    sent = client.send(friend.uid, msg) 