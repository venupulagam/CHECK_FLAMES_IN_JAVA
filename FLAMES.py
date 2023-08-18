def doflames() :
    
    print("\nEnter the names")
    
    name1 = input("\nMay I know your name please : ")
    name = name1
    
    while len(name1) == 0:
        print("! INVALID NAME !")
        name1 = input("PLEASE ENTER A VALID NAME : ")
        
    name2 = input("Whom do you want to check FLAMES with ? : ")
    
    while len(name2) == 0:
        print("! INVALID NAME !")
        name2 = input("PLEASE ENTER THE NAME OF DESIRED PERSON : ")
    
    name1 = name1.lower()
    name2 = name2.lower()
    
    length = len(name1) + len(name2)
    
    flames = "flames"
    
    for i in name1 :
        for j in name2 :
            if i == j :
                length = length - 2
    
    dif = length
    
    while dif > len(flames):
        if dif > 0 :
            dif = dif - len(flames)
            
    letter = flames[dif-1]
    
    print("")
    
    if length != 0:
        if letter == flames[0] :
            print("Hola ! You both are FRIENDS !!")
        elif letter == flames[1]:
            print("Congo ",name," your relation is called LOVE <3")
        elif letter == flames[2]:
            print("AFFECTION, But please dont get affected by the output ;)")
        elif letter == flames[3] :
            print("You better stay single." + name2 + "will MARRY you soon (hopefully).")
        elif letter == flames[4]:
            print("Get yourself a shield, your ENEMY is already in the battlefield !!")
        elif letter == flames[5]:
            print("April 10 is your day. Dont google its the SIBLINGs day :) ")

    
doflames()

    