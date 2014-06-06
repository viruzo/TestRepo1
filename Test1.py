def print_reverse_list(alist : list):
    blist = alist[:]
    blist.reverse()
    print(blist)

def say_hello(name):
    print("Hello, %s!" % name)

def copy_list(alist):
    return alist[:]


def main():
    try:
        say_hello("world")
        say_hello("user")
        alist = [2.5, 3.2, 1.8]
        print_reverse_list(alist)
        print(alist)
    except Exception as E:
        print(E)


if __name__ == "__main__":
    main()
