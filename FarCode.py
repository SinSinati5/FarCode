#####################################
##############Main Code##############
#####################################

#####################################
"""
Main Code
Importing All The Functions And Features From Function.py
The Importing Is Imported As "x"
"""
#####################################
"""
Importing Function.py
Features And Functions Contained
Create Functions For Each Function
To Be Used In Tkinter
"""
#####################################
import Function as x

def FUNCTION1():
    x.farCodeTranslator(tabChooser)
def FUNCTION2():
    x.copi(tabChooser)
def FUNCTION3():
    x.pTE(tabChooser)
def FUNCTION4():
    x.tTT(tabChooser)
def FUNCTION5():
    x.oF(tabChooser)
def FUNCTION6():
    x.iD(tabChooser)
#####################################




"""
Create The Tkinter
Make Buttons
Call Functions As Buttons
"""




if 1==1:  
    print("Welcome To Far Code".center(150))
    import os.path
    from os import path
    ifExists = str(path.exists("User_Data_Name019247.txt"))
    openFile2 = open("User_Data_Name019247.txt" , "r")
    usernameSaved = openFile2.readline()
    openFile2.close()
    lOC = int(len(usernameSaved))
    if ifExists=="True":
        if lOC==0:
            askingUsername = input("Create Username : ")
            askingPassword = input("Create Password : ")
            openFile = open("User_Data_Name019247.txt" , "w")
            openFile1 = open("Pass_Data_Code019247.txt" , "w")
            openFile.write(askingUsername)
            openFile1.write(askingPassword)
            openFile.close()
            openFile1.close()
            closingStatement = input("The Username and Password have been saved !!!/Press Enter To Exit !!! ")
    if ifExists=="True":
        if lOC>0:
            username = input("Username : ")
            if 1==1:
                openFile2 = open("User_Data_Name019247.txt" , "r")
                openFile3 = open("Pass_Data_Code019247.txt" , "r")
                usernameSaved = openFile2.readline()
                passwordSaved = openFile3.readline()
                openFile2.close()
                openFile3.close()
                if username==usernameSaved:
                    password = input("Password : ")
                    if password==passwordSaved:
                        import tkinter

                        tabChooser = tkinter.Tk()

                        B = tkinter.Button(tabChooser, text ="Translator", command = FUNCTION1 )
                        B.pack()

                        B1 = tkinter.Button(tabChooser, text ="Copi", command = FUNCTION2 )
                        B1.pack()

                        B2 = tkinter.Button(tabChooser, text ="PyToEXE", command = FUNCTION3 )
                        B2.pack()

                        B3 = tkinter.Button(tabChooser, text ="Sython Turtl", command = FUNCTION4 )
                        B3.pack()

                        B4 = tkinter.Button(tabChooser, text ="One File", command = FUNCTION5 )
                        B4.pack()

                        B5 = tkinter.Button(tabChooser, text ="Iso", command = FUNCTION6 )
                        B5.pack()


                        tabChooser.mainloop()
