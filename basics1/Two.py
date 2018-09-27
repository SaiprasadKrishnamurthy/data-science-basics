l = [10, 20, 30, 40]
p = 1
index = 0
while index < len(l):
    p = p * l[index]
    index += 1
else:
    print(index)
print("Product is: {}".format(p))

# prime number
n = int(input("Enter the number: "))
i = 2
canBeDivided = False
while 2 <= i <= n - 1 and not canBeDivided:
    if n % i == 0:
        canBeDivided = True
    i += 1

print("IS {} a prime number? {}".format(n, not canBeDivided))
