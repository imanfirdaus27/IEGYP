def main():
    message = input()
    split_char = input()
    message = message.split(split_char)
    print("Strings after splitting")
    for i in range(len(message)):
        message[i] = message[i].capitalize()
        print(message[i])

if __name__ == "__main__":
    main()