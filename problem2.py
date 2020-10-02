#! python3
n = int(input("NOMBER\n"))
N = str(n)
for x in range(1,n):
    n = n * x
print(N + "! is " + n)