name = input("Enter your name: ")
sname = input("Enter your name: ")
x = "abcd"
y = input("Enter the password: ")

while x!= y:
    print("Enter the Correct Password")
    y = input("Enter the password: AGAIN ")

message = "Hi %s %s your Password accepted!!" % (name,sname)
print(message)
