#! python3
n = (input("NAME PLZ\n")).strip()
p = ("Lebron","Kobe","Michale","Shaq","Dennis")
for x in p:
    if n == x:
        print("That name is on the list")
if n not in p:
    print("That name is not on the list")