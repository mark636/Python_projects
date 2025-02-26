try:
    file = open("dataaaa.txt")
except FileNotFoundError:
    file = open("dataaaa.txt","w")
