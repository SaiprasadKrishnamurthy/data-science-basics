import numpy as np

L = range(100)
b = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(b.shape)
print(b.argmin())

print(np.linspace(0, 1, 7))

print(np.diag(np.random.randn(4)))

print(np.arange(10)[0:9:2])

d = np.loadtxt("/Users/saikris/PycharmProjects/python1/populations.txt")
populations = d[:, 1:]
print(populations)
print(np.std(populations, axis=0))
print(np.mean(populations, axis=0))
print(np.median(populations, axis=0))
print(np.argmax(populations, axis=1))
z = np.array([1, 2, 3, 4])
print(z.reshape(2, 2))
print(z[:, np.newaxis])
print(np.arange(10).reshape(5, 2))
