path = input("Path of cc file: ")
cc = open(rf"{path}")
listOfCC = []
numCC = 0

global validCC
validCC = 0

def isValid(line):
    global validCC
    line = list(line)

    if line[4] == '-' or line[4] == ' ':
        del line[4]
        del line[8]
        del line[12]
    
    try:
        line = list(map(int, line))
    except:
        return False
    
    if len(line) != 16:
        return False
    
    if line[0] not in range(4,8):
        return False
    
    for i in range(0,16,2):
        line[i] = line[i]*2
        if line[i] >9:
            line[i] = sum(map(int, list(str(line[i]))))

    if sum(line)%10 == 0:
        validCC = validCC + 1
        return True
    else:
        return False


for line in cc:
    line = line.strip("\n")
    check = isValid(line)
    listOfCC.append(f"{line} : {check}")
    numCC = numCC +1

print(listOfCC)
print(f"Number of CCs: {numCC}")
print(f"Valid: {validCC}")
      
