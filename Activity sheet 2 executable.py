import time
from colorama import Fore
from colorama import Style

name1 = input("What is your name?")
print("Thank you", name1, "very cool!")
time.sleep(1.5)
fav_lang1 = input("What is your favourite programming language, " + name1 + "?")
print("Thank you, " + name1 + ". Your details have been saved.")
time.sleep(2)
print(chr(27) + "[2J")
name2 = input("Subject 2.\nWhat is your name?")
fav_lang2 = input("What is your favourite programming language, " + name2 + "?")
print("Thank you, " + name2 + ". Your details have NOT been saved.")
print(chr(27) + "[2J")
time.sleep(1.5)

if name1[-1]=="s" and name2[-1]=="s":
    print(f'{Fore.RED}{name1}{Style.RESET_ALL}' + "' favourite programming language is " + 
    f'{Fore.RED}{fav_lang1}{Style.RESET_ALL}' + ".\n" + f'{Fore.BLUE}{name2}{Style.RESET_ALL}' + 
    "' favourite programming language is " + f'{Fore.BLUE}{fav_lang2}{Style.RESET_ALL}' + ".")
elif name1[-1]=="s" and name2[-1]!="s":
    print(f'{Fore.RED}{name1}{Style.RESET_ALL}' + "' favourite programming language is " + 
    f'{Fore.RED}{fav_lang1}{Style.RESET_ALL}' + ".\n" + f'{Fore.BLUE}{name2}{Style.RESET_ALL}' + 
    "'s favourite programming language is " + f'{Fore.BLUE}{fav_lang2}{Style.RESET_ALL}' + ".")
elif name1[-1]!="s" and name2[-1]=="s":
    print(f'{Fore.RED}{name1}{Style.RESET_ALL}' + "'s favourite programming language is " + 
    f'{Fore.RED}{fav_lang1}{Style.RESET_ALL}' + ".\n" + f'{Fore.BLUE}{name2}{Style.RESET_ALL}' + 
    "' favourite programming language is " + f'{Fore.BLUE}{fav_lang2}{Style.RESET_ALL}' + ".")
else: 
    print(f'{Fore.RED}{name1}{Style.RESET_ALL}' + "'s favourite programming language is " + 
    f'{Fore.RED}{fav_lang1}{Style.RESET_ALL}' + ".\n" + f'{Fore.BLUE}{name2}{Style.RESET_ALL}' + 
    "'s favourite programming language is " + f'{Fore.BLUE}{fav_lang2}{Style.RESET_ALL}' + ".")

#Testing branches
