'''
# TODO
similarities/diffs to Java...
'''

class Client:

    def __init__(self, name, email, dependents):
        self.name = name
        self.email = email
        self.dependents = dependents
    def to_csv(self):
        return self.name + ',' + self.email + ',' + str(self.dependents)
    def __str__(self):
        return f"Name: {self.name}, email: {self.email}, dependents: {self.dependents}"
    
client1 = Client("dave", "dave@gmail.com", ("Dave jnr", "davina"))
print(client1) # <__main__.Client object at 0x104d1e450>
# run parent method
print(client1.to_csv())

#  have a child class that inherits from Client
class RegisteredClient(Client):
    # there is little point in sub-classing without differentiation
    # diff is to do a NEW thing, or do a same thing DIFFERENTLY
    def __init__(self, id=0, name="New registered client", email="no email provided", dependents=("no dependents")):
        # self.name = name
        # self.email = email
        # self.dependents = dependents
        # super().__init__(name, email, *dependents)
        super().__init__(name, email, dependents)
        # the above DOES NOT make an object of the parent class!!
        # extra item of state (do something new)
        self.id = id

    # overridden method (do something differently)
    def __str__(self):
        return f"ID: {self.id}, name: {self.name}, email: {self.email}, dependents: {self.dependents}"
    
reg_client1 = RegisteredClient(id=1, name="Fred", email="fred@gmail.com", dependents=("Alfredo", "Frida"))
# TypeError: RegisteredClient.__init__() got an unexpected keyword argument 'dependents'
print(reg_client1)
# run parent class method in an instance of the child
# parent - child
# super - sub
# base - derived are all interchangeable
print(reg_client1.to_csv())




