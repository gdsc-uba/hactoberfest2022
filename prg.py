print("HI! WELCOME TO MY PROGRAM. THIS PROGRAM HELPS YOU CREATE,DELETE,EDIT,ADD,etc A TIMETABLE!!")
print("But first, Lets create a Timetable!")
z=int(input("Enter number of inputs:"))
d={}
for k in range(z):
    a=input("Enter Time for Timetable:")
    b=input("Enter Activity Name:")
    d[a]=b
print(d)
print("Functions which this program allows you to perform on your Timetable:")
print("    (1)Check for Activity in your Timetable.")
print("    (2)Check Time and Activity name.")
print("    (3)Change Activity for a given Time.")
print("    (4)Add Activity to Timetable.")
print("    (5)Delete Activity from Timetable.")
print("    (6)Check presence of the Time of an Activity.")
print("    (7)Check Activity name.")
print("    (8)To retrive Activity name.")
print("    (9)Add a new Timetable to the old Timetable.")
print("    (10)Add the same Activities to all Time slots.")

while True:
    input1=int(input("Enter Function which is to be performed on this Timetable:"))

    
    if(input1==1):
        x=input("Enter time for which you want to check activity:")    #(1)Check for Activity in your Timetable.
        print(d[x])
        
    if(input1==2):
        v=input("Do you want to check your time and activity name? 1(for time)/2(for activity)")  #(2)Check Time and Activity name.
        if(v=='1'):
            print(d.keys())
        elif(v=='2'):
            print(d.values())
        else:
            print("Enter valid input.")

    if(input1==3):        
        c=input("Do you want to change activity for a given time? y/n")   #(3)Change activity for a given time.
        if (c=='y'):
            n=input("Enter time of activity:")
            m=input("Enter new name for activity:")
            d[n]=m
            print("The new timings for the day are:  ",d)
            
    if(input1==4):        
        s=input("Do you want to add an activity? y/n")   #(4)Add Activity to Timetable.
        if(s=='y'):
            n=input("Enter time of activity:")
            f=input("Enter new ativity:")
            d[n]=f
            print(d)
            
    if(input1==5):
        g=input("Do you want to delete Activity? y/n")   #(5)Delete Activity from Timetable.
        if(g=='y'):
            n=input("Enter time of activity:")
            del d[n]   #Alternatively (del d[n])can also be written as (d,pop(n)), which will perform the same function as delete.
            print("The new timings are: ",d)
            
    if(input1==6):        
        h=input("Do you want to check for the presence of a timed activity? y/n")   #(6)Check presence of the Time of an Activity.
        if(h=='y'):
            j=input("Enter time to be checked:")
            if(j in d):
                print("Time present in timetable.")
            else:
                print("Time not present in timetable.")
                
    if(input1==7):            
        l=input("Do you want to check for activity name? y/n")   #(7)Check Activity name.
        if(l=='y'):
            q=input("Enter Activity to be checked:")
            if(l in d):
                print("Activity present in timetable.")
            else:
                print("Activity not present in timetable.")

    if(input1==8):
        w=input("Do you want to retrive particular actitivity name? y/n")   #(8)To retrive Activity name.
        if(w=='y'):
            t=input("Enter time of activity whoose activity you want to retrive:")
            w=d.get(t)
            print(w)
            
    if(input1==9):
        u=input("Do you want to add a new timetable in your old timetable & update it? y/n")   #(9)Add a new Timetable to the old Timetable.
        if(u=="y"):
            d1=dict()
            print("Creating a new empty dictionary...  ",d1)
            p=input("Enter Time(s) for new timetable:")
            o=input("Enter Activity(s) for new timetable:")
            d1[p]=o
            print("The new timetable is...",d1)
            d.update(d1)

    if(input1==10):        
        ask=input("Do you want same activities at all times in a new timetable? y/n")   #(10)Add the same Activities to all Time slots.
        if (ask=='y'):
            nd2=int(input("Enter number of times you want to see same activity:"))
            for mn in range(nd2):
                n_keys=input("Enter time(s) for same activity:")
                n_values=input("Enter an activity which you want to see at all times in your timetable:")
                d2=dict.fromkeys(n_keys,n_values)
                print(d2)
    ch=input("DO YOU WANT TO RUN THE PROGRAM AGAIN? yes/no")
    if(ch=='no'):
        break
