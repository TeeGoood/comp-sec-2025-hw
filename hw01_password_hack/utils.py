def get_pwd_dict() -> list[str]:
    with open("pwd_dict.txt", "r") as f:
        return [x.strip("\n") for x in f.readlines()]
