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

account = Account("Bob", "Bobloves")

print(account.username)
print(account.password)

newPassword = "BobLoves1"

if account.validate_password(newPassword) == True:
    account.password_attach(newPassword)
else:
    print("Couldn't change password")