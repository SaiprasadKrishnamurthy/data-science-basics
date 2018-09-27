s = [1, 2, 4, 5]
print(s[0:len(s)])

s[1] = s[1] + 10
print(s)
s.append(100)

m = {1: "One", 2: "Two", 3: "Three"}

print(m)

print(m.__contains__(1))

x = int(input("Enter a number: "))

print(m)

print("Hello {}, How's it going today? Are you ".format("Sai"))

a, b = 10, 20

print(m.keys().__contains__(10))
if x in s:
    print("Contains")
elif (x not in s) and (m.keys().__contains__(x)):
    print(" Contains in MAP only")
else:
    print("Not found")
l = [3, 4, 1, 5, 7, 12, 311, 54]
l.sort(reverse=True)
print("Smallest of {}, is: {}".format(l, l[-1]))
