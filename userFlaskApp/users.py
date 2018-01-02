from user import User


class Users():

    def __init__(self,users):
        self.users = users

    def toString(self):
        return_string = []
        for user in self.users:
            return_string.append(User.toString(self.users[user]))
        return ' \n'.join(return_string)

    def add_user(self,user):
        self.users[str(user.uuid)]=user
