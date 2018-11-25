import hashlib
import sha3
sk = sha3.shake_128() 
sk.update(b'')
print([sk.squeeze(512)])  

'''when i'm trying to run this code (in python 3) then it's throwing an error 
>>> print([sk.squeeze(512)])
AttributeError: '_pysha3.shake_128' object has no attribute 'squeeze'

'''

