import json,os
def my():
    user=(input("enter login or signup:-"))
    if user=="signup":
        u_name=input("enter the user_name:-")
        password=input("enter the password:-")
        p=len(password)
        numbers = "0123456789"
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        special_chr = "!@#$%^&*"
        n,l,u,s=0,0,0,0
        i=0
        while i<len(password):
            if password[i] in numbers:
                n=n+1
            if password[i] in lower_case:
                l=l+1
            if password[i] in upper_case:
                u=u+1
            if password[i] in special_chr:
                s=s+1
            i=i+1  
        if p>=5:
            if n>=1 and l>=1 and u>=1 and s>=1 :
                print("strong password")
            else:
                print("Simple  password")
        else:
            print("password shoud contain atleast 5 ")    
        password1=((input("Comfrom the your password :-")))
        if password==password1 :
                print("Comfrom your password ")
                dic={}
                l=[]
                d={}
                d1={}
                dic["username"]=u_name
                dic["password"]=password1
                d["description"]=input("enter the description:-")
                d["D.O.B"]=input("enter your D.O.B:-")
                d["Gender"]=input("enter your gender Female/Male:-")
                d["Hobbies"]=input("enter your hobbies:-")
                dic["Profile"]=d
                l.append(dic)
                d1["user"]=l
                file=open("Signup.json","w+")
                json.dump(d1,file ,indent=4)
                file.close()
                print("Signup Succesfully")        
        else:
            print("wrong password")  
    elif user=="login":
        a=open("Signup.json","r")                 
        f=json.load(a)
        d=input("Enter your user name for login:-")
        v=input("Enter your password for login:-")
        for i in f["user"]:
            if d==i['username']:
                if v==i['password']:
                    print(" your Login successful")
                    print(i)
                    break
                else:
                    print("Check your password")
            else:
                print("Check your username")
    else:
        print("Your enter wrong input ")       
my()