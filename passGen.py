import random as rd
from sys import argv
import pyperclip # pip install pyperclip 

# import over this line

script, userLenght = argv # unpacking

number = ("1","2","3","4","5","6","7","8","9","0") # number lib
special = ("!","@","#","$","%","?","&","*","(",")","-","_","=","+","/",".",","," ") # symbol lib 
alpha = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z") # alphabet 
alphaCap = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z") # alphabet upper case
lipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce blandit ultrices risus at bibendum. Duis porta interdum leo, 
            consectetur euismod purus aliquet eget. Aliquam nisl ex, vehicula ut massa a, sodales porttitor lacus. Phasellus ultricies mauris 
            aliquam magna tincidunt molestie. Sed nec elit metus. Vestibulum dictum sed augue in viverra. Nulla finibus, ante at hendrerit semper, 
            dui urna posuere augue, in euismod lacus dui sed justo. Vestibulum purus diam, dignissim eget risus non, feugiat blandit libero. Sed id 
            nulla vel turpis condimentum facilisis eget at nibh. Fusce ac mattis arcu. Sed eget eros eget justo ultricies varius sit amet vel urna. Nunc 
            vel vehicula sapien. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed at velit vel dui scelerisque 
            imperdiet. Phasellus pharetra tellus justo, eu vehicula purus molestie nec.""" # dummy text
passGen = [] # list init

# main var over this line

lenght = int(userLenght) # value from argv stored 

for i in range(lenght): # main loop 

    choice = rd.randrange(5) 

    #print(choice)  # for debug

    if choice == 0:
        passGen.append(number[rd.randrange(0, len(number))])
    elif choice == 1:
        passGen.append(special[rd.randrange(0, len(special))])
    elif choice == 2:
        passGen.append(alpha[rd.randrange(0, len(alpha))])
    elif choice == 3:
        passGen.append(alphaCap[rd.randrange(0, len(alphaCap))])
    elif choice == 4:
        passGen.append(lipsum.split()[rd.randrange(0, len(lipsum.split()))])

pw = "".join(passGen)

print("Done! password \"{}\" copied to clipboard".format(pw))

pyperclip.copy(pw)