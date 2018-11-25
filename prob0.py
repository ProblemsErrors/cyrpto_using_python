import hashlib
import sha3
sk = sha3.shake_128() 
sk.update(b'')
print([sk.squeeze(512)])
