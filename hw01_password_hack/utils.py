import time
from typing import Callable


def get_pwd_dict() -> list[str]:
    with open("pwd_dict.txt", "r") as f:
        return [x.strip("\n") for x in f.readlines()]

def metric(fn: Callable[[], str]) -> float:
    count = 0
    start = time.time()
    
    while True:
        duration = time.time() - start
        if duration >= 1:
           break

        count +=1
        fn()

    return round(count / duration, 2)   