# -*- coding: utf-8 -*-
"""
@author: JackSparr0w999
"""

#PROGETTO: sistema operativo

user1 = "Johnny"
user2 = "Tessa"

user = input(f"Choose a username: \n(1). {user1} \n(2). {user2} \n--> ")

if user == "1":
    print(f"Welcome back {user1}")
    
elif user == "2":
    print(f"Welcome back {user2}")



def pswdvar(pswd):
    # Controlla se la password è più lunga di 5 caratteri
    if len(pswd) < 6:
        return "Password must be longer (6 characters or more)"
    
    # Verifica se la password è alfanumerica (contiene almeno una lettera e un numero)
    has_lettera = False
    has_numero = False
    
    for char in pswd:
        if char.isalpha():
            has_lettera = True
        elif char.isdigit():
            has_numero = True
    
    if has_lettera and has_numero:
        return "Password saved!"
    else:
        return "La password deve contenere almeno una lettera e un numero."


def cambia_password():
    while True:
        pswd = input("Inserisci una nuova password: ")
        risultato = pswdvar(pswd)  # Controlla se la password è valida
        print(risultato)
        
        # Se la password è valida, la "salviamo" e usciamo dal ciclo
        if risultato == "Password saved!":
            print("La password è stata salvata correttamente!")
            return pswd  # Restituiamo la password salvata

pswd = cambia_password() # Senza questo la password non si salva


wtd = "What do you want to do now?"
todo = input(
    f"{wtd}\n"
    "(1). Change my password\n"
    "(2). Change my account\n"
    "(3). Change the name of this account\n"
    "(4). Apri motore di ricerca\n"
    "--> ")


if todo == "1":
    old = input("Scrivi la tua vecchia password \n--> ")
    if old != pswd:
        while old != pswd:
            print("Password errata. Riprova")
            old = input("--> ")
        else:
            print('Password riconosciuta')
            while True:
                pswd = input("Scrivi la tua nuova password \n--> ")
                risultato = pswdvar(pswd)  # Controlla se la password è valida
                print(risultato)
            
                # Se la password è valida, la "salviamo" e usciamo dal ciclo
                if risultato == "Password saved!":
                    print("La password è stata salvata correttamente!")
                    break

elif todo == "2":
    resp = input(f"Sure you wanna switch to {user2}? (Y)\(n) \n--> ")
    if resp == "Y":
        pswd2 = "Tessa123"
        pswd2var = input(f"Inserisci la password per {user2} \n--> ")
        
        def var(pswd2var):
            while pswd2var != pswd2:
                print("Password errata.")
                pswd2var = input("Try again \n--> ")
            else:
                print(f"Welcome back {user2}.")
        var(pswd2var)
        
elif todo == "3":
    trys = input("What username do you want to change?"
                 f" (1). {user1} or (2).{user2}?  \n--> ")
    if trys == "1":
        trys_01 = input(f"Write the password for {user1} \n--> ")
       
        while trys_01 != pswd:
            print("Password errata!")
            trys_01 = input("Try again \n--> ")
        else:
            print(f"Welcome back {user1}.")
        
        new_username1 = input("Write here your new username \n--> ")
        print(f"Perfect! {new_username1} has been saved succesfully!")
        user1 = new_username1
        
    elif trys == "2":
        trys_02 = input(f"Write the password for {user2} \n --> ")
        
        while trys_02 != pswd:
            print("Password errata!")
            trys_02 = input("Try again \n--> ")
        else:
            print(f"Welcome back {user2}.")
        
        new_username2 = input("Write here your new username \n--> ")
        print(f"Perfect! {new_username2} has been saved succesfully!")
        user1 = new_username2
        
elif todo == "4":
    l = ["Forno Roscioli", "Burger King", "Mille leghe sotto i mari", "Amazon"]
    k = []
    res = len(k)
    i = 1

    find = input("Cerca qualcosa qui \n --> ")

    for word in l:
        if find in word:
            k.append(word)

    print(f"Risultati trovati: {res}")

    for word in k:
        print(f"({i}) {word}")
        i += 1
        
    openf = input("Open ")
        
        
        
        
        
        
    
