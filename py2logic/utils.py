# from os import urandom
# from random import randint

# variableNames = []
counter = -1

def generateName() -> str:
    global counter
    # result = f"{chr(97 + randint(0, 25))}{urandom(6).hex()}"
    # while result in variableNames:
    #     result = f"{chr(97 + randint(0, 25))}{urandom(6).hex()}"
    # variableNames.append(result)
    counter += 1
    return f"__tmp{counter}"
