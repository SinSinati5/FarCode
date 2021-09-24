


##############################
"""
Creating Functions
Features In Different Function
"""
##############################


def iD(tabChooser):
    tabChooser.destroy()
    import turtle
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(0)
    w = int(input("Width: "))
    d = int(input("Depth : "))
    h = int(input("Height : "))


    def move(length):
        for i in range(2):
            t.forward(length)
            t.left(120)
        t.right(60)



    def dFX(length):
        t.pendown()
        t.forward(length)
        t.forward(-1 * length)
        t.left(120)
        t.forward(length)
        t.forward(-1 * length)

    def dTHT():
        if 1==1:
            t.pensize("5")
            t.left(30)
            for i in range(3):
                dFX(50)
            t.penup()
            move(50)
            dFX(50)
            t.right(120)
            move(50)
            t.right(120)
            t.pendown()
            move(50)
            move(50)
            t.right(120)
            move(50)
            move(50)
    for i in range(w):
        dTHT()
        t.forward(50)
        t.right(150)
    t.goto(0,0)
    while d > 1:
        t.left(30)
        t.penup()
        t.forward(d*25)
        t.right(30)
        for i in range(w):
            t.pendown()
            dTHT()
            t.forward(50)
            t.right(150)
        d-=1
    t.goto(0,-50)
    while h > 1:
        for i in range(w):
            t.pendown()
            dTHT()
            t.forward(50)
            t.right(150)
        t.penup()
        t.left(90)
        t.forward(50)
        t.right(90)

def oF(tabChooser):
    tabChooser.destroy()
    tFFP = input("1 : Saved Files One\n")
    oF1FT = open("Saved_Data_1File1.txt" , "r")
    oF1FT1 = oF1FT.read()
    lOF1FT = len(oF1FT1)
    if lOF1FT == 0:
        bFN = str(input("Both File Names : "))
        fDW = str(input("Original File Destination : "))
        fTYWTBU = str(input("Updated File Destination : "))
        oF1FT = open("Saved_Data_1File1.txt" , "w")
        oF1FT1 = open("Saved_Data_1File2.txt" , "w")
        oF1FT1s = open("Saved_Data_1File3.txt" , "w")
        oF1FT.write(fDW)
        oF1FT1.write(fTYWTBU)
        oF1FT1s.write("\\" + bFN)
        oF1FT.close()
        oF1FT1.close()
        oF1FT1s.close()
        s1t829 = input("Data Saved")
    elif lOF1FT > 0:
        oF1FT23 = open("Saved_Data_1File1.txt" , "r")
        oF1FT123 = open("Saved_Data_1File2.txt" , "r")
        oF1FT123s = open("Saved_Data_1File3.txt" , "r")
        fromD = oF1FT23.read()
        dis1 = oF1FT123.read()
        dis1c = oF1FT123s.read()
        for sina123455 in range(10):
            in1234 = input("Press Enter To Update // ")
            import os
            sin23t = str(dis1.rstrip("\\")) + str(dis1c)
            os.remove(sin23t)
            import shutil
            sin23t = str(fromD.rstrip("\\")) + str(dis1c)
            shutil.copy(sin23t , dis1)
            print("File Is Updated // ")

def tTT(tabChooser):
    tabChooser.destroy()
    import turtle
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(0)
    for i in range(1000):
        tC = input("")
        tC1 = tC[0]
        if tC=="f":
            tC2 = int(tC[1:])
            t.forward(tC2)

def pTE(tabChooser):
    tabChooser.destroy()
    def fLFYM():
        if aF=="1":
            if 1==1:
                if 1==1:
                    if 1==1:
                        if 1==1:
                            if 1==1:
                                if 1==1:
                                    if oFOD=="2":
                                        hMF = str(input("How Many Files (Limit 5) : "))
                                        if hMF=="1":
                                            fN12 = fN[:-3]
                                            oAOF = str(pFL) + "\\dist\\" + str(fN12)
                                            aFL = str(input("File Location : "))
                                            aFLS = str(aFL) + "\\"
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            end = input("Progress -%100- / Your exe file is ready in the .py folder / Press enter to log out !!! ").title()
                                        if hMF=="2":
                                            fN12 = fN[:-3]
                                            oAOF = str(pFL) + "\\dist\\" + str(fN12)
                                            aFL = str(input("File Location : "))
                                            aFLS = str(aFL) + "\\"
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            end = input("Progress -%100- / Your exe file is ready in the .py folder / Press enter to log out !!! ").title()
                                        if hMF=="3":
                                            fN12 = fN[:-3]
                                            oAOF = str(pFL) + "\\dist\\" + str(fN12)
                                            aFL = str(input("File Location : "))
                                            aFLS = str(aFL) + "\\"
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            end = input("Progress -%100- / Your exe file is ready in the .py folder / Press enter to log out !!! ").title()
                                        if hMF=="4":
                                            fN12 = fN[:-3]
                                            oAOF = str(pFL) + "\\dist\\" + str(fN12)
                                            aFL = str(input("File Location : "))
                                            aFLS = str(aFL) + "\\"
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            end = input("Progress -%100- / Your exe file is ready in the .py folder / Press enter to log out !!! ").title()
                                        if hMF=="5":
                                            fN12 = fN[:-3]
                                            oAOF = str(pFL) + "\\dist\\" + str(fN12)
                                            aFL = str(input("File Location : "))
                                            aFLS = str(aFL) + "\\"
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            end = input("Progress -%100- / Your exe file is ready in the .py folder / Press enter to log out !!! ").title()
                                    if oFOD=="1":
                                        hMF = str(input("How Many Files (Limit 5) : "))
                                        if hMF=="1":
                                            fN12 = fN[:-3]
                                            oAOF = str(pFL) + "\\dist"
                                            aFL = str(input("File Location : "))
                                            aFLS = str(aFL) + "\\"
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            end = input("Progress -%100- / Your exe file is ready in the .py folder / Press enter to log out !!! ").title()
                                        if hMF=="2":
                                            fN12 = fN[:-3]
                                            oAOF = str(pFL) + "\\dist"
                                            aFL = str(input("File Location : "))
                                            aFLS = str(aFL) + "\\"
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            end = input("Progress -%100- / Your exe file is ready in the .py folder / Press enter to log out !!! ").title()
                                        if hMF=="3":
                                            fN12 = fN[:-3]
                                            oAOF = str(pFL) + "\\dist"
                                            aFL = str(input("File Location : "))
                                            aFLS = str(aFL) + "\\"
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            end = input("Progress -%100- / Your exe file is ready in the .py folder / Press enter to log out !!! ").title()
                                        if hMF=="4":
                                            fN12 = fN[:-3]
                                            oAOF = str(pFL) + "\\dist"
                                            aFL = str(input("File Location : "))
                                            aFLS = str(aFL) + "\\"
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            end = input("Progress -%100- / Your exe file is ready in the .py folder / Press enter to log out !!! ").title()
                                        if hMF=="5":
                                            fN12 = fN[:-3]
                                            oAOF = str(pFL) + "\\dist"
                                            aFL = str(input("File Location : "))
                                            aFLS = str(aFL) + "\\"
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            aFNS1 = input("File Name : ")
                                            fAFN1 = str(aFLS) + str(aFNS1)
                                            import shutil
                                            shutil.copy(fAFN1 , oAOF)
                                            end = input("Progress -%100- / Your exe file is ready in the .py folder / Press enter to log out !!! ").title()
    if 1==1:
       if 1==1:
           if 1==1:
               if 1==1:
                   if 1==1:
                        pFL = str(input("Py File Location : "))
                        fN = str(input("Py File Name : "))
                        aI = str(input("1 : Add Icon\n2 : No Icon\n"))
                        aF = str(input("1 : Add File\n2 : No File\n"))
                        if aI=="1":
                            iFN = str(input("Icon File Name : "))
                            oFOD = str(input("1 : One EXE File\n2 : One Directory\n"))
                            if oFOD=="1":
                                wCOWO = str(input("1 : Without Console\n2 : With Console\n"))
                                if wCOWO=="1":
                                    import os
                                    fC = "\npyinstaller --icon=" + str(iFN) + " --onefile --windowed " + str(fN)
                                    cPF = "cd " + str(pFL)
                                    print(str(fC))
                                    print("\nCopy the code above^^ and paste down belowvv / Type exit in the second command line")
                                    os.system('cmd /k "{}"'.format(cPF))
                                    fLFYM()
                                if wCOWO=="2":
                                    import os
                                    fC = "\npyinstaller --icon=" + str(iFN) + " --onefile " + str(fN)
                                    cPF = "cd " + str(pFL)
                                    print(str(fC))
                                    print("\nCopy the code above^^ and paste down belowvv / Type exit in the second command line")
                                    os.system('cmd /k "{}"'.format(cPF))
                                    fLFYM()
                            if oFOD=="2":
                                wCOWO = str(input("1 : Without Console\n2 : With Console\n"))
                                if wCOWO=="1":
                                    import os
                                    fC = "\npyinstaller --icon=" + str(iFN) + " --onedir --windowed " + str(fN)
                                    cPF = "cd " + str(pFL)
                                    print(str(fC))
                                    print("\nCopy the code above^^ and paste down belowvv / Type exit in the second command line")
                                    os.system('cmd /k "{}"'.format(cPF))
                                    fLFYM()
                                if wCOWO=="2":
                                    import os
                                    fC = "\npyinstaller --icon=" + str(iFN) + " --onedir " + str(fN)
                                    cPF = "cd " + str(pFL)
                                    print(str(fC))
                                    print("\nCopy the code above^^ and paste down belowvv / Type exit in the second command line")
                                    os.system('cmd /k "{}"'.format(cPF))
                                    fLFYM()
                                    
                        if aI=="2":
                            oFOD = str(input("1 : One EXE File\n2 : One Directory\n"))
                            if oFOD=="1":
                                wCOWO = str(input("1 : Without Console\n2 : With Console\n"))
                                if wCOWO=="1":
                                    import os
                                    fC = "\npyinstaller --onefile --windowed " + str(fN)
                                    cPF = "cd " + str(pFL)
                                    print(str(fC))
                                    print("\nCopy the code above^^ and paste down belowvv / Type exit in the second command line")
                                    os.system('cmd /k "{}"'.format(cPF))
                                    fLFYM()
                                if wCOWO=="2":
                                    import os
                                    fC = "\npyinstaller --onefile " + str(fN)
                                    cPF = "cd " + str(pFL)
                                    print(str(fC))
                                    print("\nCopy the code above^^ and paste down belowvv / Type exit in the second command line")
                                    os.system('cmd /k "{}"'.format(cPF))
                                    fLFYM()
                            if oFOD=="2":
                                wCOWO = str(input("1 : Without Console\n2 : With Console\n"))
                                if wCOWO=="1":
                                    import os
                                    fC = "\npyinstaller --onedir --windowed " + str(fN)
                                    cPF = "cd " + str(pFL)
                                    print(str(fC))
                                    print("\nCopy the code above^^ and paste down belowvv / Type exit in the second command line")
                                    os.system('cmd /k "{}"'.format(cPF))
                                    fLFYM()
                                if wCOWO=="2":
                                    import os
                                    fC = "\npyinstaller --onedir " + str(fN)
                                    cPF = "cd " + str(pFL)
                                    print(str(fC))
                                    print("\nCopy the code above^^ and paste down belowvv / Type exit in the second command line")
                                    os.system('cmd /k "{}"'.format(cPF))
                                    fLFYM()

def copi(tabChooser):
    tabChooser.destroy()
    if 1==1:
        if 1==1:
            if 1==1:
                if 1==1:
                    if 1==1:
                        w = str(input("1 : External Hard Drive\n2 : Destination\n"))
                        if w=="1":
                            sRC = input("Drive Code : ").title()
                            dST = input("Folder Name : ")
                            oSRC = str(sRC , ":" , sep ="")
                            import shutil
                            shutil.copytree( oSRC, dST)
                        if w=="2":
                            sRC = input("Drive Destination : ")
                            dST = input("Folder Name : ")
                            import shutil
                            shutil.copytree( sRC, dST)

def farCodeTranslator(tabChooser):
    def ifFarCode():
        if x=="59826284":
            print("A" , end = "")
        if x=="51884187":
            print("B" , end = "")
        if x=="14214548":
            print("C" , end = "")
        if x=="72927242":
            print("D" , end = "")
        if x=="47926152":
            print("E" , end = "")
        if x=="41957457":
            print("F" , end = "")
        if x=="25862645":
            print("G" , end = "")
        if x=="68249524":
            print("H" , end = "")
        if x=="31714911":
            print("I" , end = "")
        if x=="73249752":
            print("J" , end = "")
        if x=="31295761":
            print("K" , end = "")
        if x=="47662197":
            print("L" , end = "")
        if x=="34179545":
            print("M" , end = "")
        if x=="30415765":
            print("N" , end = "")
        if x=="28961594":
            print("O" , end = "")
        if x=="72495725":
            print("P" , end = "")
        if x=="72417545":
            print("Q" , end = "")
        if x=="25659542":
            print("R" , end = "")
        if x=="93869237":
            print("S" , end = "")
        if x=="22384028":
            print("T" , end = "")
        if x=="32832003":
            print("U" , end = "")
        if x=="82377874":
            print("V" , end = "")
        if x=="73457829":
            print("W" , end = "")
        if x=="62347935":
            print("X" , end = "")
        if x=="42837556":
            print("Y" , end = "")
        if x=="32083234":
            print("Z" , end = "")
        if x=="29657514":
            print("a" , end = "")
        if x=="21587461":
            print("b" , end = "")
        if x=="37267127":
            print("c" , end = "")
        if x=="84145454":
            print("d" , end = "")
        if x=="15418561":
            print("e" , end = "")
        if x=="32652323":
            print("f" , end = "")
        if x=="45632165":
            print("g" , end = "")
        if x=="15616411":
            print("h" , end = "")
        if x=="21561351":
            print("i" , end = "")
        if x=="61351311":
            print("j" , end = "")
        if x=="51121211":
            print("k" , end = "")
        if x=="51654564":
            print("l" , end = "")
        if x=="65465151":
            print("m" , end = "")
        if x=="51545442":
            print("n" , end = "")
        if x=="92467937":
            print("o" , end = "")
        if x=="98724793":
            print("p" , end = "")
        if x=="68461464":
            print("q" , end = "")
        if x=="54215645":
            print("r" , end = "")
        if x=="51341521":
            print("s" , end = "")
        if x=="54548453":
            print("t" , end = "")
        if x=="54125113":
            print("u" , end = "")
        if x=="65413135":
            print("v" , end = "")
        if x=="51315415":
            print("w" , end = "")
        if x=="65351311":
            print("x" , end = "")
        if x=="54131542":
            print("y" , end = "")
        if x=="55121512":
            print("z" , end = "")
        if x=="65151321":
            print(" " , end = "")
        if x=="13184154":
            print("." , end = "")
        if x=="54151521":
            print("/" , end = "")
        if x=="64655113":
            print("," , end = "")
        if x=="13135113":
            print("?" , end = "")
        if x=="54151121":
            print("(" , end = "")
        if x=="65413135":
            print(")" , end = "")


            
    def ifFarText():
        if x=="A":
            print("59826284" , end = "")
        if x=="B":
            print("51884187" , end = "")
        if x=="C":
            print("14214548" , end = "")
        if x=="D":
            print("72927242" , end = "")
        if x=="E":
            print("47926152" , end = "")
        if x=="F":
            print("41957457" , end = "")
        if x=="G":
            print("25862645" , end = "")
        if x=="H":
            print("68249524" , end = "")
        if x=="I":
            print("31714911" , end = "")
        if x=="J":
            print("73249752" , end = "")
        if x=="K":
            print("31295761" , end = "")
        if x=="L":
            print("47662197" , end = "")
        if x=="M":
            print("34179545" , end = "")
        if x=="N":
            print("30415765" , end = "")
        if x=="O":
            print("28961594" , end = "")
        if x=="P":
            print("72495725" , end = "")
        if x=="Q":
            print("72417545" , end = "")
        if x=="R":
            print("25659542" , end = "")
        if x=="S":
            print("93869237" , end = "")
        if x=="T":
            print("22384028" , end = "")
        if x=="U":
            print("32832003" , end = "")
        if x=="V":
            print("82377874" , end = "")
        if x=="W":
            print("73457829" , end = "")
        if x=="X":
            print("62347935" , end = "")
        if x=="Y":
            print("42837556" , end = "")
        if x=="Z":
            print("32083234" , end = "")
        if x=="a":
            print("29657514" , end = "")
        if x=="b":
            print("21587461" , end = "")
        if x=="c":
            print("37267127" , end = "")
        if x=="d":
            print("84145454" , end = "")
        if x=="e":
            print("15418561" , end = "")
        if x=="f":
            print("32652323" , end = "")
        if x=="g":
            print("45632165" , end = "")
        if x=="h":
            print("15616411" , end = "")
        if x=="i":
            print("21561351" , end = "")
        if x=="j":
            print("61351311" , end = "")
        if x=="k":
            print("51121211" , end = "")
        if x=="l":
            print("51654564" , end = "")
        if x=="m":
            print("65465151" , end = "")
        if x=="n":
            print("51545442" , end = "")
        if x=="o":
            print("92467937" , end = "")
        if x=="p":
            print("98724793" , end = "")
        if x=="q":
            print("68461464" , end = "")
        if x=="r":
            print("54215645" , end = "")
        if x=="s":
            print("51341521" , end = "")
        if x=="t":
            print("54548453" , end = "")
        if x=="u":
            print("54125113" , end = "")
        if x=="v":
            print("65413135" , end = "")
        if x=="w":
            print("51315415" , end = "")
        if x=="x":
            print("65351311" , end = "")
        if x=="y":
            print("54131542" , end = "")
        if x=="z":
            print("55121512" , end = "")
        if x==" ":
            print("65151321" , end = "")
        if x==".":
            print("13184154" , end = "")
        if x=="/":
            print("54151521" , end = "")
        if x==",":
            print("64655113" , end = "")
        if x=="?":
            print("13135113" , end = "")
        if x=="(":
            print("54151121" , end = "")
        if x==")":
            print("65413135" , end = "")
    
    tabChooser.destroy()
    if 1==1:
        if 1==1:
            if 1==1:
                if 1==1:
                    if 1==1:
                        choose = input("1 : Receive\n2 : Send\n")
                        if choose=="2":
                            textCode = input("Enter your text : ")
                            print(textCode , " = " , sep = "" , end = "")
                            tCL = len(textCode)
                            if tCL>20:
                                print("The text limit is 20.")
                            if tCL<=20:
                                if tCL==1:
                                    tCL1 = textCode[0]
                                    x = tCL1
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()

                                if tCL==2:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()

                                if tCL==3:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()

                                if tCL==4:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()

                                if tCL==5:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()

                                if tCL==6:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    tCL6 = textCode[5]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    x = tCL6
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()
                                if tCL==7:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    tCL6 = textCode[5]
                                    tCL7 = textCode[6]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    x = tCL6
                                    ifFarText()
                                    x = tCL7
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()
                                if tCL==8:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    tCL6 = textCode[5]
                                    tCL7 = textCode[6]
                                    tCL8 = textCode[7]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    x = tCL6
                                    ifFarText()
                                    x = tCL7
                                    ifFarText()
                                    x = tCL8
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()
                                    
                                if tCL==9:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    tCL6 = textCode[5]
                                    tCL7 = textCode[6]
                                    tCL8 = textCode[7]
                                    tCL9 = textCode[8]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    x = tCL6
                                    ifFarText()
                                    x = tCL7
                                    ifFarText()
                                    x = tCL8
                                    ifFarText()
                                    x = tCL9
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()
                                if tCL==10:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    tCL6 = textCode[5]
                                    tCL7 = textCode[6]
                                    tCL8 = textCode[7]
                                    tCL9 = textCode[8]
                                    tCL10 = textCode[9]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    x = tCL6
                                    ifFarText()
                                    x = tCL7
                                    ifFarText()
                                    x = tCL8
                                    ifFarText()
                                    x = tCL9
                                    ifFarText()
                                    x = tCL10
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()
                                if tCL==11:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    tCL6 = textCode[5]
                                    tCL7 = textCode[6]
                                    tCL8 = textCode[7]
                                    tCL9 = textCode[8]
                                    tCL10 = textCode[9]
                                    tCL11 = textCode[10]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    x = tCL6
                                    ifFarText()
                                    x = tCL7
                                    ifFarText()
                                    x = tCL8
                                    ifFarText()
                                    x = tCL9
                                    ifFarText()
                                    x = tCL10
                                    ifFarText()
                                    x = tCL11
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()
                                if tCL==12:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    tCL6 = textCode[5]
                                    tCL7 = textCode[6]
                                    tCL8 = textCode[7]
                                    tCL9 = textCode[8]
                                    tCL10 = textCode[9]
                                    tCL11 = textCode[10]
                                    tCL12 = textCode[11]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    x = tCL6
                                    ifFarText()
                                    x = tCL7
                                    ifFarText()
                                    x = tCL8
                                    ifFarText()
                                    x = tCL9
                                    ifFarText()
                                    x = tCL10
                                    ifFarText()
                                    x = tCL11
                                    ifFarText()
                                    x = tCL12
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()
                                if tCL==13:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    tCL6 = textCode[5]
                                    tCL7 = textCode[6]
                                    tCL8 = textCode[7]
                                    tCL9 = textCode[8]
                                    tCL10 = textCode[9]
                                    tCL11 = textCode[10]
                                    tCL12 = textCode[11]
                                    tCL13 = textCode[12]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    x = tCL6
                                    ifFarText()
                                    x = tCL7
                                    ifFarText()
                                    x = tCL8
                                    ifFarText()
                                    x = tCL9
                                    ifFarText()
                                    x = tCL10
                                    ifFarText()
                                    x = tCL11
                                    ifFarText()
                                    x = tCL12
                                    ifFarText()
                                    x = tCL13
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()
                                if tCL==14:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    tCL6 = textCode[5]
                                    tCL7 = textCode[6]
                                    tCL8 = textCode[7]
                                    tCL9 = textCode[8]
                                    tCL10 = textCode[9]
                                    tCL11 = textCode[10]
                                    tCL12 = textCode[11]
                                    tCL13 = textCode[12]
                                    tCL14 = textCode[13]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    x = tCL6
                                    ifFarText()
                                    x = tCL7
                                    ifFarText()
                                    x = tCL8
                                    ifFarText()
                                    x = tCL9
                                    ifFarText()
                                    x = tCL10
                                    ifFarText()
                                    x = tCL11
                                    ifFarText()
                                    x = tCL12
                                    ifFarText()
                                    x = tCL13
                                    ifFarText()
                                    x = tCL14
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()
                                if tCL==15:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    tCL6 = textCode[5]
                                    tCL7 = textCode[6]
                                    tCL8 = textCode[7]
                                    tCL9 = textCode[8]
                                    tCL10 = textCode[9]
                                    tCL11 = textCode[10]
                                    tCL12 = textCode[11]
                                    tCL13 = textCode[12]
                                    tCL14 = textCode[13]
                                    tCL15 = textCode[14]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    x = tCL6
                                    ifFarText()
                                    x = tCL7
                                    ifFarText()
                                    x = tCL8
                                    ifFarText()
                                    x = tCL9
                                    ifFarText()
                                    x = tCL10
                                    ifFarText()
                                    x = tCL11
                                    ifFarText()
                                    x = tCL12
                                    ifFarText()
                                    x = tCL13
                                    ifFarText()
                                    x = tCL14
                                    ifFarText()
                                    x = tCL15
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()
                                if tCL==16:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    tCL6 = textCode[5]
                                    tCL7 = textCode[6]
                                    tCL8 = textCode[7]
                                    tCL9 = textCode[8]
                                    tCL10 = textCode[9]
                                    tCL11 = textCode[10]
                                    tCL12 = textCode[11]
                                    tCL13 = textCode[12]
                                    tCL14 = textCode[13]
                                    tCL15 = textCode[14]
                                    tCL16 = textCode[15]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    x = tCL6
                                    ifFarText()
                                    x = tCL7
                                    ifFarText()
                                    x = tCL8
                                    ifFarText()
                                    x = tCL9
                                    ifFarText()
                                    x = tCL10
                                    ifFarText()
                                    x = tCL11
                                    ifFarText()
                                    x = tCL12
                                    ifFarText()
                                    x = tCL13
                                    ifFarText()
                                    x = tCL14
                                    ifFarText()
                                    x = tCL15
                                    ifFarText()
                                    x = tCL16
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()
                                if tCL==17:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    tCL6 = textCode[5]
                                    tCL7 = textCode[6]
                                    tCL8 = textCode[7]
                                    tCL9 = textCode[8]
                                    tCL10 = textCode[9]
                                    tCL11 = textCode[10]
                                    tCL12 = textCode[11]
                                    tCL13 = textCode[12]
                                    tCL14 = textCode[13]
                                    tCL15 = textCode[14]
                                    tCL16 = textCode[15]
                                    tCL17 = textCode[16]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    x = tCL6
                                    ifFarText()
                                    x = tCL7
                                    ifFarText()
                                    x = tCL8
                                    ifFarText()
                                    x = tCL9
                                    ifFarText()
                                    x = tCL10
                                    ifFarText()
                                    x = tCL11
                                    ifFarText()
                                    x = tCL12
                                    ifFarText()
                                    x = tCL13
                                    ifFarText()
                                    x = tCL14
                                    ifFarText()
                                    x = tCL15
                                    ifFarText()
                                    x = tCL16
                                    ifFarText()
                                    x = tCL17
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()
                                if tCL==18:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    tCL6 = textCode[5]
                                    tCL7 = textCode[6]
                                    tCL8 = textCode[7]
                                    tCL9 = textCode[8]
                                    tCL10 = textCode[9]
                                    tCL11 = textCode[10]
                                    tCL12 = textCode[11]
                                    tCL13 = textCode[12]
                                    tCL14 = textCode[13]
                                    tCL15 = textCode[14]
                                    tCL16 = textCode[15]
                                    tCL17 = textCode[16]
                                    tCL18 = textCode[17]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    x = tCL6
                                    ifFarText()
                                    x = tCL7
                                    ifFarText()
                                    x = tCL8
                                    ifFarText()
                                    x = tCL9
                                    ifFarText()
                                    x = tCL10
                                    ifFarText()
                                    x = tCL11
                                    ifFarText()
                                    x = tCL12
                                    ifFarText()
                                    x = tCL13
                                    ifFarText()
                                    x = tCL14
                                    ifFarText()
                                    x = tCL15
                                    ifFarText()
                                    x = tCL16
                                    ifFarText()
                                    x = tCL17
                                    ifFarText()
                                    x = tCL18
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()
                                if tCL==19:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    tCL6 = textCode[5]
                                    tCL7 = textCode[6]
                                    tCL8 = textCode[7]
                                    tCL9 = textCode[8]
                                    tCL10 = textCode[9]
                                    tCL11 = textCode[10]
                                    tCL12 = textCode[11]
                                    tCL13 = textCode[12]
                                    tCL14 = textCode[13]
                                    tCL15 = textCode[14]
                                    tCL16 = textCode[15]
                                    tCL17 = textCode[16]
                                    tCL18 = textCode[17]
                                    tCL19 = textCode[18]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    x = tCL6
                                    ifFarText()
                                    x = tCL7
                                    ifFarText()
                                    x = tCL8
                                    ifFarText()
                                    x = tCL9
                                    ifFarText()
                                    x = tCL10
                                    ifFarText()
                                    x = tCL11
                                    ifFarText()
                                    x = tCL12
                                    ifFarText()
                                    x = tCL13
                                    ifFarText()
                                    x = tCL14
                                    ifFarText()
                                    x = tCL15
                                    ifFarText()
                                    x = tCL16
                                    ifFarText()
                                    x = tCL17
                                    ifFarText()
                                    x = tCL18
                                    ifFarText()
                                    x = tCL19
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()
                                if tCL==20:
                                    tCL1 = textCode[0]
                                    tCL2 = textCode[1]
                                    tCL3 = textCode[2]
                                    tCL4 = textCode[3]
                                    tCL5 = textCode[4]
                                    tCL6 = textCode[5]
                                    tCL7 = textCode[6]
                                    tCL8 = textCode[7]
                                    tCL9 = textCode[8]
                                    tCL10 = textCode[9]
                                    tCL11 = textCode[10]
                                    tCL12 = textCode[11]
                                    tCL13 = textCode[12]
                                    tCL14 = textCode[13]
                                    tCL15 = textCode[14]
                                    tCL16 = textCode[15]
                                    tCL17 = textCode[16]
                                    tCL18 = textCode[17]
                                    tCL19 = textCode[18]
                                    tCL20 = textCode[19]
                                    x = tCL1
                                    ifFarText()
                                    x = tCL2
                                    ifFarText()
                                    x = tCL3
                                    ifFarText()
                                    x = tCL4
                                    ifFarText()
                                    x = tCL5
                                    ifFarText()
                                    x = tCL6
                                    ifFarText()
                                    x = tCL7
                                    ifFarText()
                                    x = tCL8
                                    ifFarText()
                                    x = tCL9
                                    ifFarText()
                                    x = tCL10
                                    ifFarText()
                                    x = tCL11
                                    ifFarText()
                                    x = tCL12
                                    ifFarText()
                                    x = tCL13
                                    ifFarText()
                                    x = tCL14
                                    ifFarText()
                                    x = tCL15
                                    ifFarText()
                                    x = tCL16
                                    ifFarText()
                                    x = tCL17
                                    ifFarText()
                                    x = tCL18
                                    ifFarText()
                                    x = tCL19
                                    ifFarText()
                                    x = tCL20
                                    ifFarText()
                                    print("\n")
                                    end = input("Copy the code/press enter to log out !!! ").title()
                                    
                    

                        if choose=="1":
                            farCode = input("Enter the Far code : ").replace(" " , "")
                            print(farCode , " = " , sep = "" , end = "")
                            farCodeLength = len(farCode)
                            fCL = farCodeLength/8
                            if 1==1:
                                if fCL==1:
                                    x = farCode
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title()
                                    
                              
                                if fCL==2:
                                    fCL1 = binaryCode[0:8]
                                    fCL2 = binaryCode[8:16]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title()
                                    
                                        
                                if fCL==3:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title

                                    
                                if fCL==4:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title


                                if fCL==5:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title


                                if fCL==6:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    fCL6 = farCode[40:48]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    x = fCL6
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title


                                if fCL==7:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    fCL6 = farCode[40:48]
                                    fCL7 = farCode[48:56]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    x = fCL6
                                    ifFarCode()
                                    x = fCL7
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title


                                if fCL==8:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    fCL6 = farCode[40:48]
                                    fCL7 = farCode[48:56]
                                    fCL8 = farCode[56:64]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    x = fCL6
                                    ifFarCode()
                                    x = fCL7
                                    ifFarCode()
                                    x = fCL8
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title

                                
                                if fCL==9:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    fCL6 = farCode[40:48]
                                    fCL7 = farCode[48:56]
                                    fCL8 = farCode[56:64]
                                    fCL9 = farCode[64:72]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    x = fCL6
                                    ifFarCode()
                                    x = fCL7
                                    ifFarCode()
                                    x = fCL8
                                    ifFarCode()
                                    x = fCL9
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title
                                

                                if fCL==10:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    fCL6 = farCode[40:48]
                                    fCL7 = farCode[48:56]
                                    fCL8 = farCode[56:64]
                                    fCL9 = farCode[64:72]
                                    fCL10 = farCode[72:80]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    x = fCL6
                                    ifFarCode()
                                    x = fCL7
                                    ifFarCode()
                                    x = fCL8
                                    ifFarCode()
                                    x = fCL9
                                    ifFarCode()
                                    x = fCL10
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title
                                
                                

                                if fCL==11:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    fCL6 = farCode[40:48]
                                    fCL7 = farCode[48:56]
                                    fCL8 = farCode[56:64]
                                    fCL9 = farCode[64:72]
                                    fCL10 = farCode[72:80]
                                    fCL11 = farCode[80:88]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    x = fCL6
                                    ifFarCode()
                                    x = fCL7
                                    ifFarCode()
                                    x = fCL8
                                    ifFarCode()
                                    x = fCL9
                                    ifFarCode()
                                    x = fCL10
                                    ifFarCode()
                                    x = fCL11
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title
                                

                                if fCL==12:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    fCL6 = farCode[40:48]
                                    fCL7 = farCode[48:56]
                                    fCL8 = farCode[56:64]
                                    fCL9 = farCode[64:72]
                                    fCL10 = farCode[72:80]
                                    fCL11 = farCode[80:88]
                                    fCL12 = farCode[88:94]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    x = fCL6
                                    ifFarCode()
                                    x = fCL7
                                    ifFarCode()
                                    x = fCL8
                                    ifFarCode()
                                    x = fCL9
                                    ifFarCode()
                                    x = fCL10
                                    ifFarCode()
                                    x = fCL11
                                    ifFarCode()
                                    x = fCL12
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title
                                


                                if fCL==13:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    fCL6 = farCode[40:48]
                                    fCL7 = farCode[48:56]
                                    fCL8 = farCode[56:64]
                                    fCL9 = farCode[64:72]
                                    fCL10 = farCode[72:80]
                                    fCL11 = farCode[80:88]
                                    fCL12 = farCode[88:94]
                                    fCL13 = farCode[88:94]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    x = fCL6
                                    ifFarCode()
                                    x = fCL7
                                    ifFarCode()
                                    x = fCL8
                                    ifFarCode()
                                    x = fCL9
                                    ifFarCode()
                                    x = fCL10
                                    ifFarCode()
                                    x = fCL11
                                    ifFarCode()
                                    x = fCL12
                                    ifFarCode()
                                    x = fCL13
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title
                                

                                if fCL==14:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    fCL6 = farCode[40:48]
                                    fCL7 = farCode[48:56]
                                    fCL8 = farCode[56:64]
                                    fCL9 = farCode[64:72]
                                    fCL10 = farCode[72:80]
                                    fCL11 = farCode[80:88]
                                    fCL12 = farCode[88:94]
                                    fCL13 = farCode[88:94]
                                    fCL14 = farCode[88:94]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    x = fCL6
                                    ifFarCode()
                                    x = fCL7
                                    ifFarCode()
                                    x = fCL8
                                    ifFarCode()
                                    x = fCL9
                                    ifFarCode()
                                    x = fCL10
                                    ifFarCode()
                                    x = fCL11
                                    ifFarCode()
                                    x = fCL12
                                    ifFarCode()
                                    x = fCL13
                                    ifFarCode()
                                    x = fCL14
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title
                                if fCL==15:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    fCL6 = farCode[40:48]
                                    fCL7 = farCode[48:56]
                                    fCL8 = farCode[56:64]
                                    fCL9 = farCode[64:72]
                                    fCL10 = farCode[72:80]
                                    fCL11 = farCode[80:88]
                                    fCL12 = farCode[88:94]
                                    fCL13 = farCode[88:94]
                                    fCL14 = farCode[88:94]
                                    fCL15 = farCode[94:102]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    x = fCL6
                                    ifFarCode()
                                    x = fCL7
                                    ifFarCode()
                                    x = fCL8
                                    ifFarCode()
                                    x = fCL9
                                    ifFarCode()
                                    x = fCL10
                                    ifFarCode()
                                    x = fCL11
                                    ifFarCode()
                                    x = fCL12
                                    ifFarCode()
                                    x = fCL13
                                    ifFarCode()
                                    x = fCL14
                                    ifFarCode()
                                    x = fCL15
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title
                                if fCL==16:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    fCL6 = farCode[40:48]
                                    fCL7 = farCode[48:56]
                                    fCL8 = farCode[56:64]
                                    fCL9 = farCode[64:72]
                                    fCL10 = farCode[72:80]
                                    fCL11 = farCode[80:88]
                                    fCL12 = farCode[88:94]
                                    fCL13 = farCode[88:94]
                                    fCL14 = farCode[88:94]
                                    fCL15 = farCode[94:102]
                                    fCL16 = farCode[102:110]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    x = fCL6
                                    ifFarCode()
                                    x = fCL7
                                    ifFarCode()
                                    x = fCL8
                                    ifFarCode()
                                    x = fCL9
                                    ifFarCode()
                                    x = fCL10
                                    ifFarCode()
                                    x = fCL11
                                    ifFarCode()
                                    x = fCL12
                                    ifFarCode()
                                    x = fCL13
                                    ifFarCode()
                                    x = fCL14
                                    ifFarCode()
                                    x = fCL15
                                    ifFarCode()
                                    x = fCL16
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title
                                if fCL==17:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    fCL6 = farCode[40:48]
                                    fCL7 = farCode[48:56]
                                    fCL8 = farCode[56:64]
                                    fCL9 = farCode[64:72]
                                    fCL10 = farCode[72:80]
                                    fCL11 = farCode[80:88]
                                    fCL12 = farCode[88:94]
                                    fCL13 = farCode[88:94]
                                    fCL14 = farCode[88:94]
                                    fCL15 = farCode[94:102]
                                    fCL16 = farCode[102:110]
                                    fCL17 = farCode[110:118]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    x = fCL6
                                    ifFarCode()
                                    x = fCL7
                                    ifFarCode()
                                    x = fCL8
                                    ifFarCode()
                                    x = fCL9
                                    ifFarCode()
                                    x = fCL10
                                    ifFarCode()
                                    x = fCL11
                                    ifFarCode()
                                    x = fCL12
                                    ifFarCode()
                                    x = fCL13
                                    ifFarCode()
                                    x = fCL14
                                    ifFarCode()
                                    x = fCL15
                                    ifFarCode()
                                    x = fCL16
                                    ifFarCode()
                                    x = fCL17
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title
                                if fCL==18:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    fCL6 = farCode[40:48]
                                    fCL7 = farCode[48:56]
                                    fCL8 = farCode[56:64]
                                    fCL9 = farCode[64:72]
                                    fCL10 = farCode[72:80]
                                    fCL11 = farCode[80:88]
                                    fCL12 = farCode[88:94]
                                    fCL13 = farCode[88:94]
                                    fCL14 = farCode[88:94]
                                    fCL15 = farCode[94:102]
                                    fCL16 = farCode[102:110]
                                    fCL17 = farCode[110:118]
                                    fCL18 = farCode[118:126]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    x = fCL6
                                    ifFarCode()
                                    x = fCL7
                                    ifFarCode()
                                    x = fCL8
                                    ifFarCode()
                                    x = fCL9
                                    ifFarCode()
                                    x = fCL10
                                    ifFarCode()
                                    x = fCL11
                                    ifFarCode()
                                    x = fCL12
                                    ifFarCode()
                                    x = fCL13
                                    ifFarCode()
                                    x = fCL14
                                    ifFarCode()
                                    x = fCL15
                                    ifFarCode()
                                    x = fCL16
                                    ifFarCode()
                                    x = fCL17
                                    ifFarCode()
                                    x = fCL18
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title
                                if fCL==19:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    fCL6 = farCode[40:48]
                                    fCL7 = farCode[48:56]
                                    fCL8 = farCode[56:64]
                                    fCL9 = farCode[64:72]
                                    fCL10 = farCode[72:80]
                                    fCL11 = farCode[80:88]
                                    fCL12 = farCode[88:94]
                                    fCL13 = farCode[88:94]
                                    fCL14 = farCode[88:94]
                                    fCL15 = farCode[94:102]
                                    fCL16 = farCode[102:110]
                                    fCL17 = farCode[110:118]
                                    fCL18 = farCode[118:126]
                                    fCL19 = farCode[126:134]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    x = fCL6
                                    ifFarCode()
                                    x = fCL7
                                    ifFarCode()
                                    x = fCL8
                                    ifFarCode()
                                    x = fCL9
                                    ifFarCode()
                                    x = fCL10
                                    ifFarCode()
                                    x = fCL11
                                    ifFarCode()
                                    x = fCL12
                                    ifFarCode()
                                    x = fCL13
                                    ifFarCode()
                                    x = fCL14
                                    ifFarCode()
                                    x = fCL15
                                    ifFarCode()
                                    x = fCL16
                                    ifFarCode()
                                    x = fCL17
                                    ifFarCode()
                                    x = fCL18
                                    ifFarCode()
                                    x = fCL19
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title
                                if fCL==20:
                                    fCL1 = farCode[0:8]
                                    fCL2 = farCode[8:16]
                                    fCL3 = farCode[16:24]
                                    fCL4 = farCode[24:32]
                                    fCL5 = farCode[32:40]
                                    fCL6 = farCode[40:48]
                                    fCL7 = farCode[48:56]
                                    fCL8 = farCode[56:64]
                                    fCL9 = farCode[64:72]
                                    fCL10 = farCode[72:80]
                                    fCL11 = farCode[80:88]
                                    fCL12 = farCode[88:94]
                                    fCL13 = farCode[88:94]
                                    fCL14 = farCode[88:94]
                                    fCL15 = farCode[94:102]
                                    fCL16 = farCode[102:110]
                                    fCL17 = farCode[110:118]
                                    fCL18 = farCode[118:126]
                                    fCL19 = farCode[126:134]
                                    fCL20 = farCode[134:142]
                                    x = fCL1
                                    ifFarCode()
                                    x = fCL2
                                    ifFarCode()
                                    x = fCL3
                                    ifFarCode()
                                    x = fCL4
                                    ifFarCode()
                                    x = fCL5
                                    ifFarCode()
                                    x = fCL6
                                    ifFarCode()
                                    x = fCL7
                                    ifFarCode()
                                    x = fCL8
                                    ifFarCode()
                                    x = fCL9
                                    ifFarCode()
                                    x = fCL10
                                    ifFarCode()
                                    x = fCL11
                                    ifFarCode()
                                    x = fCL12
                                    ifFarCode()
                                    x = fCL13
                                    ifFarCode()
                                    x = fCL14
                                    ifFarCode()
                                    x = fCL15
                                    ifFarCode()
                                    x = fCL16
                                    ifFarCode()
                                    x = fCL17
                                    ifFarCode()
                                    x = fCL18
                                    ifFarCode()
                                    x = fCL19
                                    ifFarCode()
                                    x = fCL20
                                    ifFarCode()
                                    print("\n")
                                    end = input("Copy the text/press enter to log out !!! ").title
