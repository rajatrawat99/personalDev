"""myfile = open("sample.txt")
content = myfile.read()
print(content)
myfile.seek(0)
print(myfile.read())"""

"""def find_the_Fruit(f):
    myfile = open("sample.txt")
    fruits = myfile.read()

    fruits = fruits.splitlines()
    for r in fruits:
        print(r)
    print(fruits)
    if f in fruits:
        return("fruit is present")
    else:
        return("fruit is not there")

print(find_the_Fruit("sdsds"))"""

"""
print("Write Function")

myfile = open("employee.txt", "w")
myfile.write("\n RAJAT \n piwi \n kmd \n imi")
myfile.close()

print("Append Function")
myfile = open("employee.txt", "a")
myfile.write("\n RAJAT \n piwi \n kmd \n imi")
myfile.close()


print("Append+Read Function")

myfile = open("employee.txt", "a+")
myfile.seek(0)
print(myfile.read())
myfile.write("\n RAJAT \n piwi \n kmd \n imi")
myfile.close()
"""

print(" dont have to close file as saves if automatucally")
with open("ex.txt", "w") as myfile:
    myfile.write("someone")
