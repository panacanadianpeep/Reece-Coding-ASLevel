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
        AllParentData = super().__init__(username, password)
        self.mCanChangeOtherAccountDetails = True
    def toString(self):
        temp = super().toString()
        temp = temp + "\n password" + str(self.mCanChangeOtherAccountDetails)

account = Account("Reece", "Draper")
print(account.toString())

admin = Admin("Sebastian", "Williamson")
print(admin.toString())