#continue is break point in the loop when if condition didnt full.

maxcount = int(input("enter # to maximum calculate:\n"))
x = 0
total = 0

while x < maxcount:
    x += 1
    if x%2!=0: # using Modolu to check if x is "mispar e-zugi"
        continue
    total += x #sum all the "Misparin Zugiim" in the renge.

print("Total sum of double numbers in range 0 -", maxcount, "is" , total)