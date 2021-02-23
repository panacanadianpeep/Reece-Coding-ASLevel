class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def username_attach(self, username):
        self.username = username
    
    def password_attach(self, password):
        self.password = password

    def validate_username(self, username):
        if len(username > 8):
            return True
        else:
            return False

    def hasNumbers(self, inputString):
        return any(char.isdigit() for char in inputString)

    def validate_password(self, password):
        if len(password) > 8 and self.hasNumbers(password):
            return True
        else:
            return False

    def toString(self):
        return "\nUsername: " + self.username + \
                "\nUsername Length: " + str(len(self.username)) + \
                "\nPassword: " + self.password + \
                "\nPassword Length: " + str(len(self.password))

class Admin(Account):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.mCanChangeOtherAccountDetails = True

    def toString(self):
        temp = super().toString()
        temp += "\nCan Change Accounts: " + str(self.mCanChangeOtherAccountDetails)
        return temp

class User(Account):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.mCanChangeOtherAccountDetails = True

    def toString(self):
        temp = super().toString()
        temp += "\nCan Change Accounts: " + str(self.mCanChangeOtherAccountDetails)
        return temp

account = Account("Reece", "Draper")
print(account.toString())

admin = Admin("Sebastian", "Williamson")
print(admin.toString())

# This works in python!
accountsList = [account, admin]

# Polymorphism
# If you create a variable or collection and define it with the base class you can add any children
# Specifically in languages that have type declaration (C, C#, C++, Java)
Admin myList = [account, admin] # This will error
Account myList = [account, admin] # This will not error