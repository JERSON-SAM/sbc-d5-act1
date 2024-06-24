#initialize a empty list 
list = []
#loop to get the 5 numbers from user input and append them to list
for i in range(5):
    numbers = (input("Enter Number:")) #promt user to enter a number 
    list.append(numbers) # add the entered number to the list

#User make a choices 0 if available 1 if not available
print("0 if naa 1 if nothing")
boss = int(input("Naa ang Boss?"))

#Handle user's choices 
if boss == 0:
    list.pop(0)#Remove the first element from the list 
    print(list)

elif boss == 1:#Remove the last Element of the list      
    list.pop()
    print(list)
    for i in range(2):# Prompt user twice to enter new numbers and append them to list 
        list.append(input("Enter Number:"))
        print("insert to add,",list)
else:
    print("Pag Utro oyyy hahha") 
    #Handle invalid input 

