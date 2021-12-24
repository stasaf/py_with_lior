x = 5
y = 2

resultA = x & y
resultB = x | y
resultC = ~x
resultD = x ^ y
resultE = x >> 2
resultF = x << 2

print(bin(x)[2:].zfill(8))
print(bin(y)[2:].zfill(8))
print("--------------")
print(bin(resultA)[2:].zfill(8))
print(bin(resultB)[2:].zfill(8))
print(bin(resultC)[2:].zfill(8))
print(bin(resultD)[2:].zfill(8))
print(bin(resultE)[2:].zfill(8))
print(bin(resultF)[2:].zfill(8))



