import random

print("""
   _____ _____  _        ____         ___  
  / ____|  __ \| |      |___ \       / _ \ 
 | |  __| |__) | |        __) |     | | | |
 | | |_ |  ___/| |       |__ <      | | | |
 | |__| | |    | |____   ___) |  _  | |_| |
  \_____|_|    |______| |____/  (_)  \___/                                                 

Password Generator, version 1.0 (x86_x64)
Licence GPLv3+ : GNU GPL version 3 <https://www.gnu.org/licenses/gpl-3.0.html>
copyright (C) 2022 BatuHanHub 

This is free software; You are free to modify and redistribute it.
NO WARRANTY to the fullest extent permitted by law.\n""")

Big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Small = "abcdefghijklmnopqrstuvwxyz"
Character = "!#$%\"*+,-./:=?@\_"
Nums = "1234567890"

while True:

    Length = int(input("How long is your password? (recommend 8,14)"))

    if Length <= 8:
        print("password length is short so it`s not secure.")
        pass

    elif Length < 0:
        print("ERROR:please write pozitive numbers (exp:1,2,3,4)")
        continue

    elif Length >= 8:
        print("this is STRONG PASSWORD!")

    else:
        print("ERROR:please write number.")

    break

String = Big + Small + Character + Nums

password = "".join(random.sample(String,Length))

print(f'Your password:\t"{password}"\nDO NOT SHARE WİTH ANYONE!!!')

input("press a key to exit.")
