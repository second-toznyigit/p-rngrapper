import os
import sys
import random

address = "/media/Bravo/NotDeleted"
key = input("Search: ")

def search(key):
    for i in range(1,5):
        for j in os.listdir(address+"/"+str(i)):
            if j == key: return True
    return False


print(search(key))
