from Crypto.Cipher import AES
	
def AES_encrypt(pt, key):
	cipher = AES.new(key, AES.MODE_ECB)	
	ct=cipher.encrypt(pt)
	return(ct)


def AES_decrypt(ct, key):
	cipher = AES.new(key, AES.MODE_ECB)	
	pt=cipher.decrypt(ct)
	return(pt)

def main():
	key = "YELLOW SUBMARINE"
	pt  = "aaaaaaaaaaaaaaaa"
	ct=AES_encrypt(pt, key)
	print(ct)  #encrypted
	
	check_pt = AES_decrypt(AES_encrypt(pt, key), key) #decrypted
	print(check_pt)
	
main()


