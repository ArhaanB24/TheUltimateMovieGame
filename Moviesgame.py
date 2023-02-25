import random
print("""\nWelcome!!
To Movie Guesser 3000\n
Rules:
-You can make a maximun of 5 mistakes after that you are out!
-You can only guess 1 letter at a time
- Do not guess any special characters or numbers 
""")
nousers = int(input("Enter Number of Players: "))
usernamelst = []
scoretab = {}
if nousers == 1:
    username = input("Enter Name of Player: ")
    usernamelst.append(username)
else:
    for x in range(nousers):
        no = x + 1
        username = input(f"Enter Name of Player {no}-- ")
        usernamelst.append(username)
    print("The players are {} ".format(",".join(usernamelst)))    
def thegame():
    Movies = open("D:\PROFILE BACKUP\Desktop\Python Projects/MoviesHindi.csv","r")
    Movieslist = Movies.readlines()
    detailedlist = []
    for x in Movieslist:
        detailedlist.append(x.split(","))       
    listlength = random.randrange(1,len(detailedlist))
    #print(detailedlist[listlength][0])  #developer access only
    hints = {detailedlist[0][1] + ": ": detailedlist[listlength][1],(detailedlist[0][2]).strip("\n") + ": ": detailedlist[listlength][2].strip("\n")}
    randommovie = list(detailedlist[listlength][0]) 
    for x in range(len(randommovie)):
        randommovie[x] = str(randommovie[x]).upper()   
    global score
    ind = []
    inptlst = []
    correctguesses = []
    failedlist = []
    correctdict = {}
    blankspace = list(("_") * len(randommovie))
    specialchars = ["-", " ", "?","=","&",":",";","!","'","(",")",".","1","2","3","4","5","6","7","8","9","0","@"]
    for num,element in enumerate(randommovie):
        numele = num,element
        ind.append(numele)
    for i,j in ind:
        if j in specialchars:
            blankspace[i] = j 
    strlst = "".join(blankspace)
    print(strlst)
    count = 0
    while "_" in blankspace and count < 5:
      inpt = str(input("Enter Guess: ")).upper()       
      for i,j in ind:
        inptlst.append(inpt)
        if inpt == j:
            correctguesses.append(inpt)
            blankspace[i] = inpt
            strlst = "".join(blankspace)
            correctdict[inpt] = 0    
        if inpt not in randommovie: 
            if inpt in failedlist:
                print("You already guessed that!") 
                break
            else:    
                print("Wrong Guess Try Again!")
                count += 1
                print("You have {} mistakes left".format(5-count))
                failedlist.append(inpt)
                if count == 2:
                   hnts = list(hints.items())[0]
                   print("Hint -->" + " " + "".join(hnts))
                   break
                if count == 4:
                    hnts = list(hints.items())[1]
                    print("Hint -->" + " " + "".join(hnts))  
                    break
                break    
      if inpt in correctdict.keys():
        print("Correct Guess!!")
        print(strlst)          
    if count == 5:
        print("You Guessed Wrong 5 Times!! You Lose. The movie was -- {}".format(detailedlist[listlength][0]))  
        score = int((len(correctguesses)/len(detailedlist[listlength][0])) * 100)
        print("You guessed {}% of the movie".format(score))
        return score
    else:
        print("***You Win***")
        score = 100
        return score  
def gameloop():
    for x in range(len(usernamelst)):
        print(f"Currently playing: {usernamelst[x]}")
        thegame()
        print(f"{usernamelst[x]}'s score is {score}")
        scoretab[usernamelst[x] + ":"] = str(score)
    for x in (list(scoretab.items())):
        if len(usernamelst) > 1:
            print(" ".join((x)))
    again = 0
    while again == 0:
        playagain = str(input("Do you want to play again?  ").upper())
        if playagain == "YES":
            gameloop()
        else:
            print("Thank you for playing")
            again = 1       
gameloop()


