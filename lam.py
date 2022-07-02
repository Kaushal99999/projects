# def square(num):return num*num

# square2= lambda num: num*num

# add=lambda a,b: a+b
# # print(square2(7))
# # print(add(3,10))

# print(square.__name__)
# print(square2.__name__)
# print(add.__name__)python3

users=[
{"username":"samuel","tweets":["I love cake","I love pie"]},
{"username":"katie","tweets":["I love my cat"]},
{"username":"jeff","tweets":[]},
{"username":"bob123","tweets":[]},
{"username":"dogo_luvr","tweets":["dogs are bets","I love dogs"]},
{"username":"voilon_luvr","tweets":[]}]

# inactive_users=list(
# print(inactive_users)

# usernames=list(map(lambda user:user["username"].upper(),filter(lambda u:not u['tweets'],users)))
# print(usernames)
# names=["lambda",'Colt','Rusty']
# print([f"Your instructor is {name}"for name in names if len(name)<5])

inactive=[user["username"].upper() for user in users if not user["tweets"]]
print(inactive)