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

if __name__ == '__main__':
    print('Welcome to search interface. Please insert desired keys for search: ')
    newKeys = input('You can add multpile keys split by spaces: ')
    for nKey in newKeys.split(' '):
        print(nKey+search(nKey))
