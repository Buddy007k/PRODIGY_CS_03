import re

def passwd_complexity(passwd):
    score=0
    if len(passwd)<8:
        print("Password must be atleast 8 characters long")
        score+=1

    if not re.search(r"[A-Z]",passwd):
        print("Password should contain atleast 1 uppercase letter")
        score+=1
    
    if not re.search(r"[a-z]",passwd):
        print("Password should contain atleast 1 lowercase letter")
        score+=1
    
    if not re.search(r"[0-9]",passwd):
        print("Password should contain atleast 1 number")
        score+=1

    if not re.search(r"[!@#$%^&*(),./?~'\"\/}|<>`{]",passwd):
        print("Password should contain atleast 1 special charater")
        score+=1

    return score

if __name__=="__main__":
    passwd=input("Enter your password: ")
    comp=passwd_complexity(passwd)
    if comp==0:
        print("Strong Password")
    elif comp<3:
        print("Moderate Password")
    else:
        print("Weak Password")
