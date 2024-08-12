import getpass



print("\nSelect Product:\n\n1 -> Flex\n2 -> NBU Master\n3 -> NBU Media\n4 -> NBU Client / Workload Client\n")
i=int(input("Enter your choice: "))


HOST = input("Enter Host: ")
USER = input("Enter Username: ")
PASSWORD = getpass.getpass()
PORT = 22

