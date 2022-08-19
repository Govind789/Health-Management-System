print("HEALTH MANAGEMENT SYSTEM\n")
print("Type 0 to Lock and 1 to Retrieve")
toDo = int(input())

if toDo == 0 :

    print("What do you want to Lock ?, Enter 0 to lock Food and Enter 1 to lock Excercise")
    toLock = int(input())
    print("Type O for Rohan, 1 for Harry, 2 for Hammad")
    toWhom = int(input())

    if toLock == 0:
        def nameforfood(toWhom):

                if toWhom == 0:
                    with open("rohanfood.txt" , "w") as b:
                        b.write(input("what Rohan should eat today:\n"))

                    with open("rohanfood.txt","r") as b:
                        content1 = b.read()
                        print( content1 + " Locked to Rohan's Food Schedule")

                elif toWhom  == 1:
                    with open("harryfood.txt","w") as c:
                        c.write(input("what Harry should eat today:\n"))

                    with open("harryfood.txt","r") as c:
                        content2 = c.readline()
                        print( content2 + " Locked to Harry's Food Schedule")

                elif toWhom == 2:
                    with open("hammadfood.txt","w") as d:
                        d.write(input("what Hammad should eat today:\n"))

                    with open("hammadfood.txt","r") as d:
                        content3 = d.readline()
                        print( content3 + " Locked to Hammad's Food Schedule")


        nameforfood(toWhom)

    elif toLock == 1:
        def nameforexcercise(toWhom):

                if toWhom == 0:
                    with open("rohanexcercise.txt", "w") as e:
                        e.write(input("what Rohan should excercise today:  \n"))

                    with open("rohanexcercise.txt", "r") as e:
                        content4 = e.readline()
                        print(content4 + " Locked to Rohan's excersie Schedule")

                elif toWhom == 1:
                    with open("harryexcercise.txt", "w") as f:
                        f.write(input("what Harry should excercise today:\n"))

                    with open("harryexcercise.txt", "r") as f:
                        content5 = f.readline()
                        print(content5 + " Locked to Harry's excercise Schedule")

                elif toWhom == 2:
                    with open("hammadexcercise.txt", "w") as g:
                        g.write(input("what Hammad should excercise today:\n"))

                    with open("hammadexcercise.txt", "r") as g:
                        content6 = g.readline()
                        print(content6 + " Locked to Hammad's excercise Schedule")

        nameforexcercise(toWhom)


elif toDo == 1:

    print("What do you want to Retreive ?, Enter 0 to Retreive Food and Enter 1 to Retreive Excercise")
    toSee = int(input())
    print("Type O for Rohan, 1 for Harry, 2 for Hammad")
    toWhom = int(input())

    def getdate():
        import datetime
        return datetime.datetime.now()

    print(getdate(), end="\n")

    if toSee == 0:
                def nameforfood(toWhom):

                    if toWhom == 0:
                        with open("rohanfood.txt", "r") as b:
                            content1 = b.read()
                            print(content1)

                    elif toWhom == 1:
                        with open("harryfood.txt", "r") as c:
                            content2 = c.readline()
                            print(content2)

                    elif toWhom == 2:
                        with open("hammadfood.txt", "r") as d:
                            content3 = d.readline()
                            print(content3)

                nameforfood(toWhom)

    elif toSee == 1:
                def nameforExcercise(toWhom):
                    if toWhom == 0:
                        with open("rohanfood.txt", "r") as b:
                            content1 = b.read()
                            print(content1)

                    elif toWhom == 1:
                        with open("harryfood.txt", "r") as c:
                            content2 = c.readline()
                            print(content2)

                    elif toWhom == 2:
                        with open("hammadfood.txt", "r") as d:
                            content3 = d.readline()
                            print(content3)

                nameforExcercise(toWhom)

