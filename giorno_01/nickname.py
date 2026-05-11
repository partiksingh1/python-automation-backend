
# 1. input name and year
# 2. add edge cases to check name and year
# 3. create a list for suffix, example ["_pro", "_99", "_dev", "_x"]
# 4. generate a random number from 0 to number of elements in the list 
# 5. add the random°th element of the list to the end of the name as a suffix with the anno
# 6. return the list and print each nickname from the list

import random

def nicknameHelper():
    # Input name
    nome = input("come ti chiami?")

    # Edge cases for nome
    if not nome:
        print("Entra un nome perf")
        return
    if len(nome)<3:
        print("Devi entrare un nome actuale con lungezza di almeno 3 charrateri !")
        return
        
    if nome.isdigit():
        print("nome devi essere un string ! ")
        return
    
    # Edge cases for ann
    anno = input("anno di nascita?")
    if not anno : 
        print("Entera un anno bro")
        return
    
    if int(anno)>2026:
        print("Entra un anno vero per favore ! ")
        return
    
    if not nome or not anno:
        print("nome e anno sono obligatore")
        return 

    # List of suffixes 
    suffisi = ["_pro", "_99", "_dev","_master", "_x","_pollo","_bollo"]

    # List of final nicknames to be return
    nomi_finale = []

    # Loop to generate a random number and append to the final list
    for i in range (3):
        r = random.randint(0,len(suffisi)-1)
        nome_random = nome+suffisi[r]
        nomi_finale.append(nome_random + "_" + anno)

    return nomi_finale

# call the helper func and store the list

nicknames = nicknameHelper()
if nicknames : 
    print("Ecco la tua 3 nicknames randomica")
    for nickname in nicknames:
        print(nickname)

else : 
    print("Finito con un errore")
