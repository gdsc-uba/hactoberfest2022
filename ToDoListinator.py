print("WELCOME! THIS IS A PROGRAM WHICH HELPS YOU CREATE A 'TO-DO LIST'!!!")
date=input("Enter date for which you want to create a To-Do List(dd/mm/yyyy):")
loop=int(input("Enter number of of To-Do Items:"))
l1=list()
for i in range(loop):
    a=input("Enter To-Do Item name:")
    l1.append(a)
print("Your To-Do List for",date,'are:')
for i in range(loop):
    print("-->",l1[i])
ask=input("\nDo you want to perform functions on your To-Do list(like add new item, delete old item,etc.)?[yes/no]")
if (ask=='yes' or ask=='Yes'):
    print("Functions which you can perform on your To-Do List are:")
    print("    (1)Add item which is to the To-Do List.")   #append
    print("    (2)Check if an item is present in your To-Do List.")   #in/not in
    print("    (3)Check for the position of a list item in a To-Do List.")   #index
    print("    (4)Add multiple items in the To-Do List.")   #extend
    print("    (5)Find how many items are present in ypur To-Do List.")   #len
    print("    (6)Work completed, remove item from your To-Do List.(By position)")   #pop
    print("    (7)Work completed, remove item from your To-Do List.(By item name)")   #remove
    print("    (8)Order your To-Do List.")   #sort/reverse-sort
    print("    (9)Copy your To-Do List.")    # import copy(copy.copy(l1))
    print("    (10)Enter Item ,above another item, which has greater importance.")   #insert
    
elif(ask=='no' or ask=='No'):
    print("Ok, This is your To-Do List :(")
    for i in range(loop):
        print("-->",l1[i])
else:
    print("Stop messin' with me!!")
while True:
    input1=int(input("Enter choice for fucntion:"))
    if (input1==1):                                                 #append
        add=input("Enter Item which is to be added:")
        l1.append(add)
        print("The new To-Do list with added item is",l1)
    if (input1==2):                                                 #in
        check=input("Enter item name whose presence is to be checked in your To-Do List:")
        if(check in l1):
            print("Item Found!!!! :)")
        else:
            print("Item not Found!!  :(")
    if (input1==3):                                                 #index
        c=input("Enter element whose position is to be checked in the To-Do List:")
        print("Position of",c,'is',(l1.index(c))+1)
    if (input1==4):                                                 #extend
        l2=eval(input("Enter list of items which you want to add in your To-Do List:\n(please enter item name in double courts)"))
        l1.extend(l2)
        print("Updated To-Do List is",l1)
    if (input1==5):                                                 #len
        print("The number of To-Do items are",len(l1))
    if (input1==6):                                                 #pop  
        rem=input("Enter item name which is to be removed:")
        print("The updated To-Do List is",l1.pop(rem))
    if (input1==7):                                                 #remove
        remo=input("Enter item name(s) which is/are to be removed:")
        print("The updated To-Do List is",l1.remove(remo))
    if (input1==8):
        choose=input("Do you want to see the To-Do list in ascending/descending order?(y-ascending/n-descending)")
        if(choose=='y'):                                            #sort
            print("Ok...The given To-do List in ascending order is\n",l1.sort())
        elif(choose=='n'):                                          #reverse sort
            print("Ok...The given To-Do List in descending order is\n",l1.sort(reverse=True))
        else:
            print("Stop messin'...Enter valid input!!!")
    if (input1==9):                                                 #import copy
        import copy
        print("Copying your To-Do List...")
        l2=copy.copy(l1)
        print("To-Do List copired succesfully...\n",l2)
    if (input1==10):                                               #insert
        z=input("Enter Item name:")
        y=int(input("Enter position for insertion of item in To-Do List:"))
        l1.insert((y-1),z)
        print("The new list is",l1)
    run=input("Do you want to run the program again?(y/n)")
    if (run=='n'):
        print("BYEE!!! NICE MEETING YOU...")
        break
