import random

res = []
for i in range(12):
    res.append(random.choice('_.0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))

print(res)
