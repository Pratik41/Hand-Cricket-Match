import random

chance = int(input("Enter number of bowl (Greater than 0 and Not more than 6 bowls):"))            #Enter number of bowls not more than 6
if chance>0 and chance<=6:
    print(chance)
    scoreu = 0
    scorec = 0
    l = ['head', 'tail']
    l1 = ['bat', 'bowl']
    tc = random.choice(l)
    tu = input("what will you choose for toss head or tail? : ")                       #Enter head or tail in lower case
    if tu=="head" or tu=="tail":
        print(f"you choose {tu} ..........")
        print("................................")
        print("let's check result of toss......")

        if tc == tu:
            print("you won the toss........")
            print("now you can choose batting or bowling.........")
            gu = input("what will you do  batting or bowling? If you want to do batting please bat else type bowl : ")           #Enter bat or bowl in lower case
            print("you choose", gu, "........")
            if gu == 'bat':
                print("now,you can start your batting...")
                for i in range(chance):
                    fc = random.randint(1, 6)
                    fu = int(input("enter your number between (1 to 6): "))                       #Enter number greater than 0 and less than equal to 6
                    if fu>0 and fu<=6:
                        if fc != fu:
                            scoreu += fu
                            print("your score:", scoreu)
                        else:
                            print("sorry...you are out.....")
                            break

                    else:
                        print("Invalid number entered.Please enter the number between (1 to 6)")
                        continue
                print("your batting is complete......")
                print("your final score:", scoreu)
                print("now,it's time for bowling.......")

                for i in range(chance):
                    fc = random.randint(1, 6)
                    fu = int(input("enter your number: "))
                    if fc != fu:
                        scorec += fc
                        print("Computer score:", scorec)
                    else:
                        print("Computer final score:", scorec)
                        print("Yesssssssss")
                        print("computer is out...")
                        break
                print(".................................")
                print("let,s check the result......")
                if scoreu == scorec:
                    print("game is tieeee..........")
                if scoreu < scorec:
                    print("good try,but you lose the game.........")
                if scoreu > scorec:
                    print("congratulations,you won the game.........")
                print("game is over....")
            elif gu=='bowl':
                print("now,you can start your bowling....")
                for i in range(chance):
                    fc = random.randint(1, 6)
                    fu = int(input("enter your number: "))
                    if fu > 0 and fu <= 6:
                        if fc != fu:
                            scorec += fc
                            print("Computer score:", scorec)
                        else:
                            print("Computer final score:", scorec)
                            print("Yessssssssss")
                            print("computer is out...")
                            break
                    else:
                        print("Invalid number entered.Please enter the number between (1 to 6)")
                        continue
                print("your bowling is complete......")
                print("...............................")
                print("now,it's time for batting.......")

                for i in range(chance):
                    fc = random.randint(1, 6)
                    fu = int(input("enter your number: "))
                    if fu > 0 and fu <= 6:
                        if fc != fu:
                            scoreu += fu
                            print("your score:", scoreu)
                        else:
                            print("your final score:", scoreu)
                            print("sorry...you are out.....")
                            break
                    else:
                        print("Invalid number entered.Please enter the number between (1 to 6)")
                        continue
                print(".................................")
                print("let,s check the result......")
                if scoreu == scorec:
                    print("game is tieeee..........")
                if scoreu < scorec:
                    print("good try,but you lose the game.........")
                if scoreu > scorec:
                    print("congratulations,you won the game.........")
                print("game is over....")
            else:
                print("Please enter the valid input for batting type-->bat and for bowling type-->bowl")

        else:
            print("computer won the toss........")
            print("now,computer will choose its choice bat or bowl.....")
            gc = random.choice(l1)
            print("computer choose", gc, "........")
            if gc == 'bat':
                print("now,you can start your bowling...")
                for i in range(chance):
                    fc = random.randint(1, 6)
                    fu = int(input("enter your number: "))
                    if fu > 0 and fu <= 6:
                        if fc != fu:
                            scorec += fc
                            print("Computer score:", scorec)
                        else:
                            print("Computer final score:", scorec)
                            print("Yessssssssss")
                            print("computer is out...")
                            break
                    else:
                        print("Invalid number entered.Please enter the number between (1 to 6)")
                        continue

                print("your bowling is complete......")
                print("...............................")
                print("now,it's time for batting.......")

                for i in range(chance):
                    fc = random.randint(1, 6)
                    fu = int(input("enter your number: "))
                    if fu > 0 and fu <= 6:
                        if fc != fu:
                            scoreu += fu
                            print("your score:", scoreu)
                        else:
                            print("your final score:", scoreu)
                            print("sorry...you are out.....")
                            break
                    else:
                        print("Invalid number entered.Please enter the number between (1 to 6)")
                        continue
                print(".................................")
                print("let,s check the result......")
                print(".................................")
                if scoreu == scorec:
                    print("game is tieeee..........")
                if scoreu < scorec:
                    print("good try,but you lose the game.........")
                if scoreu > scorec:
                    print("Congratulations,you won the game.........")
                print("game is over....")

            else:
                print("now,you can start batting....")
                for i in range(chance):
                    fc = random.randint(1, 10)
                    fu = int(input("enter your number: "))
                    if fu > 0 and fu <= 6:
                        if fc != fu:
                            scoreu += fu
                            print("your score:", scoreu)
                        else:
                            print("your final score:", scoreu)
                            print("sorry...you are out.....")
                            break
                    else:
                        print("Invalid number entered.Please enter the number between (1 to 6)")
                        continue
                print("your batting is complete......")
                print("...............................")
                print("now,it's time for bowling.......")

                for i in range(chance):
                    fc = random.randint(1, 10)
                    fu = int(input("enter your number: "))
                    if fu > 0 and fu <= 6:
                        if fc != fu:
                            scorec += fc
                            print("Computer score:", scorec)
                        else:
                            print("Computer final score:", scorec)
                            print("Yessssssss")
                            print("computer is out...")
                            break
                    else:
                        print("Invalid number entered.Please enter the number between (1 to 6)")
                        continue

                print(".................................")
                print("let,s check the result......")
                if scoreu == scorec:
                    print("game is tieeee..........")
                if scoreu < scorec:
                    print("good try,but you lose the game.........")
                if scoreu > scorec:
                    print("Congratulations,you won the game.........")
                print("game is over....")
    else:
        print("invalid choice as you enter the input other than head or tail")

else:
    print("Invalid input as you entered number of bowls>6")
