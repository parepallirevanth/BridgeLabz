# 1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
# a. I/P ­> Take User Name as Input. Ensure UserName has min 3 char
# b. Logic ­> Replace <<UserName>> with the proper name
# c. O/P ­> Print the String with User Name
# ------------------------------------------------------------------------------
# Function to print welcome msg with username
def WelcomeUser(UserName):
    if len(UserName) >= 3:  # Ensures UserName has min 3 char
        print("\"Hello " + UserName + ", How are you?\"")
    else:
        print("Enter Username atleast 3 characters")


if __name__ == '__main__':
    UserName = input("Enter Username: ")
    WelcomeUser(UserName)  # Function call
