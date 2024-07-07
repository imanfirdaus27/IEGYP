def Passport(x):
    passports = []

    for i in range(x):
        print(f"Enter the details of  the client {i+1}")
        clientdetails = []
        for j in range(3):
            clientdetails.append(input())
        passports.append(clientdetails)

    search_passport = input("Enter the passport number of the client to be searched\n")
    client_found = None
    for client in passports:
        if client[2] == search_passport:
            client_found = client
            break
    
    if client_found:
        print("Client Details")
        print(f"{client_found[0]}--{client_found[1]}--{client_found[2]}")
    else:
        print("Client not found")

x = int(input("Enter the number of clients\n"))
Passport(x)