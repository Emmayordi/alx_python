# . Inventing is a combination of brains and materials. The more brains you use, the less material you need
for i in range(10):
    for j in range(i + 1, 10):
        print("{}{}".format(i, j), end='')
        if i < 8:
            print(", ", end='')

print("\n")