encrypted=input()
import binascii
nums = binascii.unhexlify(encrypted)
for key in range(256):
   dec=" "
   for i in range(len(nums)):
       dec+=chr(nums[i]^key)
   print(dec)
                
       
