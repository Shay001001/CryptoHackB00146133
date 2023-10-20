stringVal = "label"
loopVal = ""
flagVal = ""
stringUni = [ord(c) for c in stringVal]
stringXor = [13 ^ i for i in stringUni]
flagVal = "".join(chr(o) for o in stringXor)
print(flagVal)
