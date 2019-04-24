# napiši program, ki izpiše prvih 200 praštevil

def je_praštevilo(n):
    for i in range(2, n):
        if n % 1 == 0:
            return False
        return True

for x in range(2, 201):
    if je_praštevilo(x):
        print(x)