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
    def ToString(self):
        return "\nUsername: " + self.username + \
                "\nLen of username: " + str(len(self.username)) + \
                "\nPassword: " + self.password + \
                "\nLen of password: " + str(len(self.password))
                

class Admin(Account):
    def __init__(self, username, password, var):
        super().__init__(username, password)
        self.AdminAccess = AdminAccess
    def 

AccountVar = Account("Bob", "Carl")
print(AccountVar.ToString())