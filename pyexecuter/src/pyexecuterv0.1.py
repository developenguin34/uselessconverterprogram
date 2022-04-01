import os

def linux():
    directoryl=input("Enter the path of your python file that you want to execute :")
    os.system("sudo -S python"+' '+directoryl)
def windows():
    directoryw=input("Enter the path of your pyhton file that you want to execute :")
    os.system("python"+' '+directoryw)

def checkos():
    whatisyouros = input("Select your operating system. If you use Linux, type L.\n If you use Windows, type W.")
    if whatisyouros == "L":
        linux()

    if whatisyouros == "W":
        windows()

    else:
        checkos()

checkos()
