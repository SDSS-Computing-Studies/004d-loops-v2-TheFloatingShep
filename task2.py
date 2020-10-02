#! python3
n = (input("NAME PLZ\n")).strip()
p = ("Joe", "Joe2", "Joe3", "Ur mom lol", "Joe4")
for x in p:
    if n == x:
        print("That name is on the list")
if n not in p:
    print("That name is not on the list")