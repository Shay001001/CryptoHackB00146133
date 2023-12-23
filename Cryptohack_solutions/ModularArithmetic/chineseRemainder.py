linCons = [(2,5), (3,11), (5,17)]
modulus = 1
pleaseWork = 0
for cons in linCons:
    modulus = modulus * cons[1]

for cons in linCons:
    conRes, conMod = cons
    modDiv = modulus // conMod
    modInverse = pow(modDiv, -1, conMod)
    pleaseWork = pleaseWork + conRes * modDiv * modInverse 
print(pleaseWork % modulus)
