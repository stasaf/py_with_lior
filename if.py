x=5
if (x<7):
    print("x<7")
x=9
if (x<7):
    print("should no be prented")

x=32
if(x>0):
    if(x>100):
        if(x!=1):
            if(x*x<1000):
                if(x!=6):
                    print("OK")
print ("goodbye!")

#we use elif for the other if after thefirst if in order to not test the other if if we found one , first it found not continue to check.
color = input("enter a color:\n")
if(color == "blue"):
    print("color is blue")
elif(color == "pink"):
    print("color is pink")
elif(color == "red"):
    print("color is red")
elif(color == "black"):
    print("color is black")
else:
    print("color",color," not in the list.....")