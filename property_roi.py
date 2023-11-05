# I need to figure out where the code is breaking:
# I think it breaks from my if statements in my function inside the ROI class...
# I have the code ask me the first question "what do you want to do..."
# I have the code responding the several prompts
# the code breaks after that point
# I have not tested the calculate_roi yet bc my code breaks in the "add property" response


class Property:

    def __init__(self):
        self.expenses = 0
        self.income = 0
        self.investments = 0
        self.roi = 0

    def calculate_roi(self):
        self.income = float(input("What is your total income? "))
        if self.income >= 0:
            print(f"Your income is {self.income} ")
        else:
             print("You need to input your total income ")
        self.expenses = float(input("what is your total expenses? "))
        if self.expenses >= 0:
             print(f"Your expenses are {self.expenses} ")
        else:
             print("You need to input your total expenses. ")
        self.investments = float(input("What is your total investment?"))
        if self.investments >= 0:
             print(f"Your total investments are {self.investments} ")
        else:
             print("You need to input your total expenses")
        self.roi = input("Lets calculate your Return on Investment (ROI) ")
        self.roi = (self.income - self.expenses)*12/self.investments
        print(f"You ROI is{self.roi}")
class User:

    def __init__(self, name):
        self.username = {}
        self.properties = {}
        self.name = name

    def add_properties(self, property):
        self.properties[property.name] = property

class ROI:
    def __init__(self):
        self.user = []
        self.current_user = None
        
    
    def add_user(self):
        username = input("enter username: ")
        if any(user.name == username for user in self.user):
            print("user name taken. try again")
        else:
            user = User(username)
            self.user(user)
            print(f"{user} account has been created! ")
        
    def choose_user(self):
        username = input("choose user: ")
        if any(user.name == username for user in self.user):
            print("user not found. add account")
        else:
            user = User(username)
            self.name(user)
            print(f"This is {user}'s account ")

    def add_property(self):
        if any(self.properties == property.name for property in self.add_property):
             print("property not found ")
        else:
             property_name = input("add your property name ")
             property.calculate_roi()
             self.current_user.add_property(property)
             print(f"This is {property_name} owned by {self.current_user.username}")
 
    def show_property(self):
        property = input("which property do you want to view? ")
        if any(self.properties == property.name for property in self.show_property):
             print("property not found ")
        else:
             property = Property()
             self.show_property_property(property)
             print(f"This is {property} ")


    def run(self):         
        while True:
                response = input("What would you like to do? (add user, choose user, add property, view property)")
                if response.lower() == 'add user':
                    self.add_user()
                elif response.lower() == 'choose user':
                    self.choose_user()
                elif response.lower() == 'add property':
                    self.add_property()
                    new_response = input("Please provide your income ")
                    if new_response.lower() == 'add income':
                        self.income()
                    elif new_response.lower() == 'add expenses':
                        self.expenses()
                    elif new_response.lower() == 'add investment':
                        self.investment()
                    elif new_response.lower() == 'calculate roi':
                        self.calculate_roi()
                    else:
                        print("Please try again")
                elif response.lower() == 'view property':
                    self.show_property()
                elif response == 'quit':
                     break
                else:
                    print("invalid response")

my_program = ROI()
my_program.run()

        # self.login_user()

    # def login_user(self):
    #     username = input("What is  your username? ")

    #     for user in self.users:
    #         if user.username == username:
    #             self.current_user = user
    #             print(f"{user} has logged in")
    #             break
    #     else:
    #         print("Username is incorrect")
    
    # def logout(self):
    #     self.current_user = None
    #     print("You have succesfully been logged out!")