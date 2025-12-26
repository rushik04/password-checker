from getpass import getpass
password=getpass("enter password:")

upper=False
lower=False
digit=False
special=False
if  len(password) >= 6 and len(password) <= 10:
    for ch in password: 
        if ch.isupper():
            upper=True
        elif ch.islower():
            lower=True
        elif ch.isdigit():
            digit=True
        elif not ch.isalnum():
            special=True
    if upper and lower and digit and special:
        print("valid and strong password")    
    else :
        print("valid but weak")
else :
    print("invalid password\n Erore:password must be 6 to 10 character long")
