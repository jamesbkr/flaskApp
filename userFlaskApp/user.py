import uuid

class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.uuid = uuid.uuid4()
    def toString(self):
        return str(self.first_name) +  ' ' + str(self.last_name)
