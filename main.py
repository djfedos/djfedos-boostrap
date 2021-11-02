import fire


def main_(name: str):
    print(f"Hello, {name}")

if __name__ == "__main__":
    fire.Fire(main_)
    