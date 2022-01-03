maxcount = int(input("enter # to maximum calculate:\n"))
x = 0
total = 0

while x < maxcount:
    x += 1
    if x%2!=0:
        continue
    total += x

print("Total sum of double numbers in range 0 -", maxcount, "is" , total)