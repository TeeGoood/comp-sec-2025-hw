import hashlib
import time
from typing import Callable
import bcrypt

pwd = "1et-m3-c00k"

def metric(algo: str, fn: Callable[[str], str]):
    count = 0
    start = time.time()
    
    while True:
        duration = time.time() - start
        if duration >= 1:
           break

        count +=1
        fn(pwd)
    
    print(f"{algo}: {count} hash/sec")

metric("MD5", lambda x: hashlib.md5(x.encode("utf-8")).hexdigest())
metric("SHA-1", lambda x: hashlib.sha1(x.encode("utf-8")).hexdigest())
metric("bcrypt", lambda x: bcrypt.hashpw(x.encode("utf-8"), bcrypt.gensalt()))
    