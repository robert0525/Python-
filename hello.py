first_name = input("What's is your first name?  ")
print("Hello", first_name)
if first_name == "Robert":
    print(first_name, "is learning Python")
elif first_name == "Maxi":
    print(first_name, " is learning with fellow students in the Comunity! Me too!")
else: 
    print("You should totally learn Python, {}!".format(first_name))
print("Have a greate day {}!".format(first_name))
       