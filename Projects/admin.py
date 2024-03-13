#Project 1:
dict={}
stud={}
ques=[]

while True:
    print()
    print("- - - - - - - - - - - - -")
    print("|Enter 1: For Teacher   |")
    print("|Enter 2: For Student   |")
    print("|Enter 0: To EXIT       |")
    print("- - - - - - - - - - - - -")

    a=int(input("Enter the CHoiCe:"))

    if a!=0:
        if a==1:
            print("\t ||Welcome Teacher||")
            print()
            while True:
                print("\t- - - - - - - - - - - - -")
                print("\t|Enter 1: To Register   |")
                print("\t|Enter 2: To Login      |")
                print("\t|Enter 0: To Go Back    |")
                print("\t- - - - - - - - - - - - -")
            
                b=int(input("\t Enter the choice:"))
                
                if b!=0:
                    if b==1:
                        print("To Register")
                        x=input("Enter the Email Address:")
                        y=input("Enter the Password:")
                        dict[x]=y                      
                        print("Thank you for Register")
                    elif b==2:
                        print("To Login")
                        x=input("Enter the Email Address:")
                        '''p=dict.keys()
                        for i in p:
                            if i==x:
                                if dict[i]==y:
                                    print("Login successful")
                                else :
                                    print("Password Does not Match")
                                
                                break
                        else :
                            print("Email Not Found")'''
                        for i in dict.items():
                            if i[0]==x:
                                y=input("Enter the Password:")
                                if i[1]==y:
                                    print("Login Successful")
                                    print()
                                    while True:
                                        print("\t- - - - - - - - - - - - -")
                                        print("\t|Enter 1: Add Ques      |")
                                        print("\t|Enter 2: Remove Ques   |")
                                        print("\t|Enter 3: Update Ques   |")
                                        print("\t|Enter 4: To Display    |")
                                        print("\t|Enter 0: To go back    |")
                                        print("\t- - - - - - - - - - - - -")

                                        c=int(input("\t Enter the choice:"))
                                        
                                        if c!=0:
                                            if c==1:
                                                print("Add Question:\n")                                                                                            
                                                que=input("Question:")
                                                q={}
                                                opt=[]
                                                q["q"]=que
                                                print("Enter the four option")
                                                for i in range(4):
                                                    v=input()
                                                    opt.append(v)
                                                while True:
                                                    flag=1
                                                    ans=input("Enter the correct answer:")
                                                    for i in opt:
                                                        if i == ans:
                                                            flag=2
                                                            opt.append(ans)
                                                            break
                                                    else :
                                                        print("Invalid ans")                        
                                                    if flag==2:
                                                        break
                                                q["option"]=opt                                                
                                                ques.append(q)
                                            elif c==2:
                                                print("Remove Question:\n")
                                                if len(ques)==0:
                                                    print("No Questions found")
                                                else :                                                
                                                    while True:
                                                        flag=1
                                                        que=input("Question:")
                                                        for i in ques:
                                                            if i["q"]==que:
                                                                flag=2
                                                                ques.remove(i)
                                                                break
                                                        else :
                                                            print("Question not matched")                                                                                                         
                                                        if flag==2:
                                                            break                                                
                                            elif c==3:
                                                print("Update Question:\n")
                                                if len(ques)==0:
                                                    print("No Questions found")
                                                else :
                                                    que=input("Question to update:")
                                                    for i in ques:
                                                        if i["q"]==que:
                                                            new=input("New Question:")
                                                            i["q"]=new
                                                            opt.clear()
                                                            print("Enter the four option")
                                                            for i in range(4):
                                                                v=input()
                                                                opt.append(v)
                                                            while True:
                                                                flag=1
                                                                ans=input("Enter the correct answer:")
                                                                for i in opt:
                                                                    if i == ans:
                                                                        flag=2
                                                                        opt.append(ans)
                                                                        break
                                                                else :
                                                                    print("Invalid ans")
                                                                if flag==2:
                                                                    break                                                        
                                                            break
                                                    else :
                                                        print("Question not Found")
                                            elif c==4:
                                                print("Display:\n")
                                                if len(ques)==0:
                                                    print("No Questions found")
                                                else :
                                                    for i in ques:
                                                        print("Question:",i["q"])
                                                        print("Options:",end="")
                                                        k=i["option"]                                                                                                   
                                                        print(k[:4],end="  ")
                                                        print("\nCorrect Answer:",k[4])
                                                        print()
                                            else :
                                                print("Invalid choice")
                                        else :
                                            break
                                else :
                                    print("Password does not match")
                                    
                                break
                        else :
                            print("Email Not Found")
                    else :
                        print("Invalid Choice")
                else :
                    break
        elif a==2:
            print("\t ||Welcome Student||")
            print()
            while True:
                print("\t- - - - - - - - - - - - -")
                print("\t|Enter 1: To Register   |")
                print("\t|Enter 2: To Login      |")
                print("\t|Enter 0: To Go Back    |")
                print("\t- - - - - - - - - - - - -")
                
                f=int(input("\t Enter the choice:"))
                
                if f!=0:
                    if f==1:
                        print("To Register")
                        x=input("Enter the Email Address:")
                        y=input("Enter the Password:")
                        stud[x]=y
                        print("Thank you for Register")
                    elif f==2:
                        print("To Login")
                        x=input("Enter the Email Address:")
                        for i in stud.items():
                            if i[0]==x:
                                y=input("Enter the Password:")
                                if i[1]==y:
                                    print("Login Successful")
                                    print()
                                    score = 0                                        
                                    print("\t- - - - - - - - - - - - - - - - - -")
                                    print("\t ||Answer The Following Questions||")
                                    if len(ques)==0:
                                        print("No Questions RightNow")
                                    else :
                                        for i in ques:
                                            print("Question:",i["q"])                                            
                                            k=i["option"]                                                                                                   
                                            for j in k[:4]:                                                
                                                print("Option:",j)
                                            print()
                                            g=input("Enter the Right Answer From the Option:")                                                     
                                            if g == k[4]:
                                                score = score + 1
                                        marks=score
                                        total=len(ques)
                                        print("Your score :",marks,"out of",total)
                                        perc=(marks/total)*100
                                        print("Percentage:",perc)
                                else :
                                    print("Password does not match")
                                    
                                break
                        else :
                            print("Email Not Found")
                    else :
                        print("Invalid Choice")
                else :
                    break
        else :
            print("**InvAlid ChoiCe**")
    else :
        print("THank YoU!!!")
        break