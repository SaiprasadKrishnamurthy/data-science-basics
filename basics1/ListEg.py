l = [1, 2, 3, 4, 5]

print(l)

l.append(6)

l.insert(12, 0)
l.pop(3)
print(l)
c = l.__contains__(5)
print(c)

l = [i + 1 for i in range(10) if i < 5]

print(l)

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

transposed = []

for i in range(len(m)):
    row = []
    for x in m:
        row.append(x[i])
    transposed.append(row)

print(m)
print(transposed)
print([[r[i] for r in m] for i in range(len(m))])

t = tuple(range(0, 100)) + tuple(range(0, 100))
t = sorted(t, reverse=True)
print(t)
print(min(t))
print(sum(t))
print("Exists" if (97 in t) else "Not exists")

s = set()
s.update({1, 2, 3, 4})
print(s)

a = {1, 2, 4, 5}
b = {1, 3, 5, 6}

print(a & b)

print((a | b) - (a & b))

print(a.symmetric_difference(b))

d = dict([(2, "Kris")])
d[1] = "Sai"

print(d)

l = list(range(1, 128))
l = map(lambda v: (v, chr(v)), l)
l = filter(lambda tt: tt[0] >= 32, l)
l = list(l)
print(l)

m = {k: v for k, v in l}
print(m)

# reverse a string
s = "DennisAndEdnaSinned"
s = s.lower()
print(s)
print(s[::-1])
print("Palindrome" if s == s[::-1] else "Not a Palindrome")

print([h for h in range(2, 9 + 1) if (6 % h == 0 and 12 % h == 0)])
