def removeAllTailingWhitespaces():
    
    bits = ""
    
    with open("..\Files/TextFiles/6TSCH_1000packets_ID123.txt", "r") as f:
        for line in f:
            line = line.rstrip('\r\n')
            bits += line

    return bits
    
def removeCharactersOnOddIndexes(bits):
    
    returnString = ""
    for i in range(len(bits)):
        if i % 2 != 0:
            returnString += bits[i]
    
    return returnString

bits = removeAllTailingWhitespaces()
bits = removeCharactersOnOddIndexes(bits)

text_file = open("..\Files/OutputFiles/6TSCH_1000packets_ID123.txt", "w")
n = text_file.write(bits)
text_file.close()

startOfFrameDelimeter = "1001000001001110"

print("Liczba znalezionych SFD:", bits.count(startOfFrameDelimeter))