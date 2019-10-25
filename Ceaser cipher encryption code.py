def encrypt(message,key):
    result = ""
    for i in range(len(message)):
      char = message[i]
      #for uppercase
      if (char.isupper()):
         result += chr((ord(char) + key-65) % 26 + 65)
      # for lowercase
      elif (char.islower()):
         result += chr((ord(char) + key - 97) % 26 + 97)
      #no intention to encrypt otherwise
      else:
         result += char
    return result
message=input("Message:")
key=int(input("key:"))
print("encrypted message:" + encrypt(message,key))
