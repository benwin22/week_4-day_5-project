class Property:

    def __init__(self):
        self.name ="" 
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
        self.roi = print("Lets calculate your Return on Investment (ROI) ")
        self.roi = (self.income - self.expenses)*12/self.investments*100
        print(f"You ROI is{self.roi}%")
class User:

    def __init__(self, name):
        self.username = name
        self.properties = {}

    def __repr__(self):
        return f"<User {self.username}>"
    
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
            self.user.append((user))
            print(f"{user} account has been created! ")
        
    def choose_user(self):
        username = input("choose user: ")
        user = next((u for u in self.user if u.username == username), None)
        if user is None:
            print("user not found. add account")
        else:
            self.current_user = user
            print(f"This is {self.current_user}'s account ")
            return user

    def add_property(self,user):
        property_name = input("add your property name ")
        if property_name in user.properties:
             print("property is defined ")
        else:
             
             prop = Property()
             prop.name = property_name
             prop.calculate_roi()
             user.add_properties(prop)
             print(f"This is {property_name} owned by {user.username}")
 
    def show_property(self):
        property_name = input("which property do you want to view? ")
        if property_name in self.current_user.properties:
             property = self.current_user.properties[property_name]
             print(f"Property name: {property.name} ")
             print(f" Total Income: {property.income} ")
             print(f"Total Expenses: {property.expenses} ")
             print(f"Total Investments: {property.investments} ")
             print(f"ROI: {property.roi}% ")
        else:
             print("Property not found.")


    def run(self):         
        while True:
                response = input("What would you like to do? (add user, choose user, add property, view property)")
                if response.lower() == 'add user':
                    self.add_user()
                elif response.lower() == 'choose user':
                    user = self.choose_user()
                elif response.lower() == 'add property':
                    if self.current_user is not None:
                        self.add_property(self.current_user)
                    else:
                        print("Please choose a user ")
                elif response.lower() == 'view property':
                    self.show_property()
                elif response == 'quit':
                     break
                else:
                    print("invalid response")

my_program = ROI()
my_program.run()