import re

def main():
    text = input()
    names = re.findall(r'[A-Z](?:\.[A-Z])?[a-zA-Z]*(?: [A-Z](?:\.[A-Z])?[a-zA-Z]+)*', text)
    for name in names:
        print(name)

if __name__ == "__main__":
    main()