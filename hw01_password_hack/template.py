import hashlib
import bcrypt

# SHA1
m=hashlib.sha1(b"Chulalongkorn").hexdigest()
print(m)

# MD5
m=hashlib.md5(b"Chulalongkorn").hexdigest()
print(m)

# BCRYPT
salt = bcrypt.gensalt()
m=bcrypt.hashpw(b"Chulalongkorn", salt)
print(m)