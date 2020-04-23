# def greet_user():
#     """显示简单的问侯语"""
#     print("Hello!")
# greet_user()
# def greet_user(username):
#     """显示简单的问侯语"""
#     print("Hello!, "+username.title()+"!")
#
#
# greet_user('tom')

def greet_user(names):
    """向列表中的每位用户发出简单的问候"""
    for name in names:
        msg = "Hello, "+name.title()+"!"
        print(msg)

usernames = ['hannah','ty','margot']
greet_user(usernames)