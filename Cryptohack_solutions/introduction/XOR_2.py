from pwn import *
key1 ="a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2_key1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_key3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_everything = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key1_bytes = bytes.fromhex(key1)
key2_key1_bytes = bytes.fromhex(key2_key1)
key2_key3_bytes = bytes.fromhex(key2_key3)
flag_bytes = bytes.fromhex(flag_everything)

key2_true = xor(key2_key1_bytes, key1_bytes)
key3_true = xor(key2_key3_bytes, key2_true)
key4_true = xor(key2_key1_bytes, key3_true)
flag = xor(flag_bytes, key4_true)

print(flag)