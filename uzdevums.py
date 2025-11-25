while True:
    lives = 7
    words = ["pievienot","vienkāršs", "pietiekami","ievērojams","atteikties","instruments","policija","vilciens","izgatavot","problēma","pilsētiņa","komēdija", "tādējādi","raksturot","aktieris", "priekštecis","tirdzniecība", "speciāls", "zinātnieks", "funkcija", "kandidāts"]
    target = words[int(input("Vārda skailtlis "))]
    targetArr = list(target)
    targetArr2 = targetArr.copy();
    for i in range(len(targetArr2)): 
        targetArr2[i] = "_"
    while lives>=0:
        if lives < 7:
            print("   +---+")
            if lives == 0:
                print("   |   |")
            else: 
                print("       |")
            if lives <= 5:
                print("   O   |")
            else: 
                print("       |")
            if lives <= 2:
                print("  /|\  |")
            elif lives <= 3:
                print("  / \  |")
            elif lives <= 4:
                print("  /    |")
            else: 
                print("       |")
            if lives <= 0: 
                print("  / \  |")
            elif lives <= 1: 
                print("  /    |")
            else: 
                print("       |")
            print("       |")
            print("=========")
        if lives == 0: 
            break;#after ^^^, so its printed on game-over
        print("Jums ir ",lives," dzīvības")
        print("Minē:" +"".join(targetArr2))
        
        inp = input("Burts: ")
        if inp=="ii": inp ="ī"# Hacks for https://www.online-python.com/
        if inp=="ee": inp ="ē"
        if inp=="aa": inp ="ā"
        if inp=="uu": inp ="ū"
        if inp=="ss": inp ="š"
        if inp=="kk": inp ="ķ"
        if inp=="ll": inp ="ļ"
        if inp=="cc": inp ="č"
        if inp=="zz": inp ="ž"
        if inp=="nn": inp ="ņ"
        if inp=="gg": inp ="ģ"
        
        complete = True
        good = False
        for i in range(len(targetArr)):
            if targetArr[i]==inp:
                targetArr2[i] = targetArr[i]
                good = True
            if targetArr2[i]=="_": 
                complete = False
        if complete: 
            break;
        if not good: 
            lives -= 1;
    if lives == 0: 
        print("💀 : "+target)
    else: 
        print("Pareizi: "+target)