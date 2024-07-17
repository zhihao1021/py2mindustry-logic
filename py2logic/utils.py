counter = -1

def generateName() -> str:
    global counter

    counter += 1
    return f"__tmp{counter}"
