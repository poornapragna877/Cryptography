encrypted=input()
decryption=""
for i in range (len(encrypted)):
        k=((i*(i+1))//2)
        if k<len(encrypted):
                decryption+=encrypted[k]
        else:
                break
print(decryption)        
