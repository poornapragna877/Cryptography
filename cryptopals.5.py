def repeated_cip(ct, key):
    decrypted=""
    key="ICE"*((len(ct))//3)
    for a,b in zip(ct,key):
        decrypted+=chr(ord(a) ^ ord(b))
    return(decrypted)

def main():
    ct=input()
    key="ICE"
    print(repeated_cip(ct, key))
main()

