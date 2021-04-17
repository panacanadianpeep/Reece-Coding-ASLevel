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
        temp = temp + "\n AdminAccess: " + str(self.mCanChangeOtherAccountDetails)
        return temp

class Teacher(Account):
    def __init__(self, username, password, subject):
        super().__init__(username, password)
        self.subject = subject
        if subject == "Math" and subject == "Maths":
            self.username = username + "Math"
        if subject == "English":
            self.username = username + "English"

    def toString(self):
        temp = super().toString()
        temp = temp + "\n Subject: " + str(self.subject)
        return temp

TeacherList = []

for i in range(3):
    username = input("Enter a username")
    password = input("Enter a password")
    subject = input("Enter a subject")
    teacher = Teacher(username, password, subject)
    TeacherList.append(teacher)
    print(teacher.toString())

for teacher in TeacherList:
    print(teacher.toString())