import hashlib
import utils

target = "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7"
pwd_dict = utils.get_pwd_dict()

def insert_char(txt: str, char: str, idx: int) -> str:
    chars = list(txt)
    chars.insert(idx, char)
    return "".join(chars)

found = False
def recur(idx: int, pwd: str):
    global found
    if found:
        return

    if idx == len(pwd):
        if hashlib.sha1(pwd.encode("utf-8")).hexdigest() == target:
            print(pwd)
            found = True
    else:
        recur(idx+1, insert_char(pwd, pwd[idx].lower(), idx))
        recur(idx+1, insert_char(pwd, pwd[idx].upper(), idx))

        subs_dict = {"o":"0", "l": "1", "i": "1"}
        if pwd[idx] in subs_dict:
            recur(idx+1, insert_char(pwd, subs_dict[pwd[idx]], idx)) 

for pwd in pwd_dict:
    recur(0, pwd)    
