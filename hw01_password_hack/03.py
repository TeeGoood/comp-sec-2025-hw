import hashlib
import math
import string
import bcrypt
import utils

char_set = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits

def cal_pwd_size(hash_per_sec: float) -> int:
    return math.ceil(math.log(hash_per_sec * 60 * 60 * 24 * 365, len(char_set)))

def log(algo: str, count: int):
    print(f"{algo}: {count} char")    

pwd = b"1et-m3-c00k"

log("MD-5", cal_pwd_size(utils.metric(lambda : hashlib.md5(pwd).hexdigest())))
log("SHA-1", cal_pwd_size(utils.metric(lambda : hashlib.sha1(pwd).hexdigest())))
log("bcrypt", cal_pwd_size(utils.metric(lambda : bcrypt.hashpw(pwd, bcrypt.gensalt()))))



