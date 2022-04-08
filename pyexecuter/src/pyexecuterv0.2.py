import os
import platform

def linux():
    pathl=input("Enter the path of your script:")
    os.system("sudo -S python"+' '+pathl)

def windows():
    pathw=input("Enter the path of your script:")
    os.system("python"+' '+pathw)
def run():
    print("Your OS:",platform.system())
    system=platform.system()
    if system=="Linux":
        linux()
    else:
        windows()
run()
