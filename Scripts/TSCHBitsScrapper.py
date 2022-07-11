def removeAllTailingWhitespaces():
    bits = ""
    with open("..\Files/TextFiles/100packetsWithId65535.txt", "r") as f:
        for line in f:
            line = line.rstrip('\r\n')
            bits += line

    return bits
    
bits = removeAllTailingWhitespaces()

startOfFrameDelimeter = "01000001000000000001000001010100"

print("Liczba znalezionych SFD:", bits.count(startOfFrameDelimeter))