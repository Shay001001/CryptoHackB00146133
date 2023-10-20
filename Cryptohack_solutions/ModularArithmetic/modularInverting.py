for x in range(1, 13):
    if(((3 % 13) * (x % 13)) % 13 == 1):
        answer = x
print(answer)