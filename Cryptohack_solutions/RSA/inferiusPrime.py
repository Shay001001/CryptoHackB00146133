from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

e = 3

n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373

#used factordb.com to get f1 and f2 from n
p = 752708788837165590355094155871
q = 986369682585281993933185289261
#copy and pasted from the inferius.py file provided by the cryptohack challenge
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
print(decrypted)