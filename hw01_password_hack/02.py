import hashlib
import bcrypt
import utils

pwd = b"1et-m3-c00k"

def log(algo: str, count: float):
    print(f"{algo}: {count} hash/s")    

log("MD-5", utils.metric(lambda : hashlib.md5(pwd).hexdigest()))
log("SHA-1", utils.metric(lambda : hashlib.sha1(pwd).hexdigest()))
log("bcrypt", utils.metric(lambda : bcrypt.hashpw(pwd, bcrypt.gensalt())))

