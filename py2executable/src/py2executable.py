import os

def linux():
    scriptnamelinux=input("Enter the path of script :")
    os.system('sudo -S python'+' '+scriptnamelinux)

def windows():
    scriptnamewindows=input("Enter the path of script :")
    os.system('python'+' '+scriptnamewindows)
