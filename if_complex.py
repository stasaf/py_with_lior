user_name = input("enter your name:\n")
user_age = int(input("enter your age:\n"))
password = input("enter the password:\n")

if(user_name == "" or password == ""):
    print("user didnt enter name or password")
elif(user_age < 18 or user_age > 120):
    print("user age is not good.....")
elif(password != "pa$$word"):
    print("wrong password!")
else:
    print("user",user_name, "OK to enter program...")
    print("program is running....")