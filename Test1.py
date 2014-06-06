def say_hello(name):
    print("Hello, %s!" % name)


def main():
    try:
        say_hello("world")
        say_hello("user")
    except Exception as E:
        print(E)


if __name__ == "__main__":
    main()
