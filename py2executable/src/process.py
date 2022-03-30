import py2executable
from py2executable import linux
from py2executable import windows

whatisyouros = input("Select your operating system. If you use Linux, type L.\n If you use Windows, type W.")
if whatisyouros == "L":
    linux()

if whatisyouros == "W":
    windows()
