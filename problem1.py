#! python3
w = int(input("WIDTH\n"))
h = int(input("HEIGHT\n"))
for y in range(h):
    for x in range(w):
        print("*", end="")
    print("")