#! python3
n = int(input("GIMME A NOMBERE\n"))
b = n + 1
a = 0
for x in range(1,b):
    a = a + int("1" * x)
print("the sum of the series is " + str(a))