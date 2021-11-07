import fire


def main_(phrase: str):
    res = phrase[::-1]
    return res
    

if __name__ == "__main__":
    fire.Fire(main_)