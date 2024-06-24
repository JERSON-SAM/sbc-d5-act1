list = []

for i in range(5):
    numbers = (input("Enter Number:"))
    list.append(numbers)

print("0 if naa 1 if nothing")
boss = int(input("Naa ang Boss?"))

if boss == 0:
    list.pop(0)
    print(list)

elif boss == 1:
    list.pop()
    print(list)
    for i in range(2):
        list.append(input("Enter Number:"))
        print("insert to add,",list)
else:
    print("Pag Utro oyyy hahha")

