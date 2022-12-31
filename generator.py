#Libs
import random
from datetime import datetime

#Errors

##Number error
def errorNUM():
    print("errorNUM:please write number")

print("""
   _____ _____  _        ____         ___  
  / ____|  __ \| |      |___ \       / _ \ 
 | |  __| |__) | |        __) |     | | | |
 | | |_ |  ___/| |       |__ <      | | | |
 | |__| | |    | |____   ___) |  _  | |_| |
  \_____|_|    |______| |____/  (_)  \___/                                                 

Password Generator, version 2.0 (x86_x64)
Licence GPLv3+ : GNU GPL version 3 <https://www.gnu.org/licenses/gpl-3.0.html>
copyright (C) 2023 BatuHanHub 

This is free software; You are free to modify and redistribute it.
NO WARRANTY to the fullest extent permitted by law.\n""")

#Chars
Big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Small = "abcdefghijklmnopqrstuvwxyz"
Character = "!#$%\"*+,-./:=?@\_"
Nums = "1234567890"

while True:
    date = datetime.now() #this is date code (.now:for the present)
    
    application = str(input("write the name of the application:")) #app name 
    
    try:
        Length = int(input("How long is your password? (recommend 8,14)")) #password length

        if Length < 8:
            print("password length is short so it`s not secure.")
            
        elif Length < 0:
            print("ERROR:please write pozitive numbers (exp:1,2,3,4)")
            continue
        
        elif Length >= 8:
            print("this is STRONG PASSWORD!")  
                
    except:
        errorNUM

    String = Big + Small + Character + Nums #password chars

    password = "".join(random.sample(String,Length)) #password writting

    print(f"\npassword writing file name:{date}.txt")
    
    file = open(f"{date}.txt","a")#'a' is makes an addition

    file.write(f"{date}\n{application}={password} \n")#app name + password

    file.close() #if program closed file writting stoped
