from randomuser import RandomUser
import pandas as pd
r= RandomUser()
# some_list = r.generate_users(10)
# print(some_list)
# name = r.get_full_name()
# print(name)
#
# for users in some_list:
#     print(users.get_full_name()," ", users.get_email())
#
# for users in some_list:
#     print(users.get_picture())

def get_users():
    users = []
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"State":user.get_state()})
    return pd.DataFrame(users)
print(get_users())

df1 = pd.DataFrame(get_users())