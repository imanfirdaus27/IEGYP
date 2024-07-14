def main():
    string = input()
    for char in string:
        if string.count(char) == 1:
            print(char)
            break
    else:
        print("#")

if __name__ == "__main__":
    main()