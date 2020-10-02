#! python3
w = int(input("Width\n"))
h = int(input("Height\n"))
for y in range(h):
    for x in range(w):
        print("*", end="")
    print("")