print("WELCOME!!! THIS A PROGRAM WHICH HELPS YOU TO FORMAT,EDIT N PERFORM VARIOUS FUNCTIONS ON A GIVEN PEICE OF TEXT...")
n=input("Enter your name:")
print("HI",n,'!!')
ask=input("""Do you want to use your name for text formating?\nOr do you want to enter another word/sentence to be edited?
Enter choice(name/new input):""")

if(ask=='name'):
    print("The word/sentence which is going to be used is","'",n,"'")
else:
    sen=input("Enter new word/sentence:")
    print("The word/sentence which is going to be used is","'",sen,"'")
    
print("(1)Do you want to check the position of each letter of you word given for Text Formatting?") #slicing
print("(2)Do you want to check if a letter or a part of word is present in the word/sentece entered by you?")  #in
print("(3)Do you want to make your word/sentence look like a title?")  #title
print("(4)Do you want to covnert your word/sentence to Upper case?")  #upper
print("(5)Do you want to convert your word/sentence to Lower case?")  #lower
print("(6)Do you want to simultaneously change the current capital to small and the current small to capital letters?")  #swapcase
print("(7)Do you want to count the occurence of a particular letter in the given word/sentence?")  #count
print("(8)Do you want to check if the given word/sentence starts or ends with a given letter/word?")  #startswith/endswith
print("(9)Do you want to remove extra spacing from the right n left bfrom word/sentence?")  # strip
print("(10)Do you want to replace particular letter with another letter/word?")  #replace
print("(11)Do you want to separate the word/sentence by a symbol/word?")  #join
print("(12)Do you want to divide a given sentece into independent words?")  #split

while True:

    input1=int(input("Enter function to be performed:"))
    if (input1==1):
        j=len(sen)
        for i in range(j):
            print(i,":",sen[i])
    if (input1==2):
        check=input("Enter word or letter to be checked:")       #in
        if(check in sen):
            print("FOUND!!!!  :)")
        else:
            print("Not Found....  :(")
    if (input1==3):                                            #title
        print("The new sentence/word in title is",sen.title())   
    if(input1==4):                                             #upper
        print("The new sentence/word in Upper case is",sen.upper())
    if (input1==5):                                            #lower
        print("The new sentence/word in Lower case is",sen.lower())
    if (input1==6):                                            #swapcase
        print("The new sentence/word with Interchanged upper n lower case is",sen.swapcase())
    if (input1==7):                                            #count
        z=input("Enter letter/word which is to be checked in the word/sentence:")
        print(z,"occurs",z.count(),"in the word/sentence.")
    if (input1==8):                                            #startswith/endswith
        a1=int(input("Do you want to check from starting(1)/end(2):(1/2)"))
        if(a1=='1'):
            v=input("Enter letter/word to be checked:")
            sen.startswith(v)
        else:
            v=input("Enter letter/word to be checked:")
            sen.endswith()
    if (input1==9):                                            #strip
        print("The new sentence/word without extra spacing is",sen.strip())            
    if (input1==10):                                           #replace
        m=input("Enter word which will replace:")
        b=input("Enter word/letter to be replaced:")
        print("The new sentence/word after replacement is",sen.replace(b,m))
    if (input1==11):                                            #join
        l=input("Enter connecting letter/symbol/number:")
        print("The new sentence/word after connecting with letter/symbol/word is",l.join(sen))
    if (input1==12):                                            #split
        print("The new sentence/word after spliting is",sen.split())
    s=input("Do you want to run the program again? y/n")
    if(s=='n'):
        break
