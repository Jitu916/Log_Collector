import paramiko
import ipaddress

class Connection:
    
    def __init__(self):
        pass

    # Function for IP validation
    def checkValidIP(self, HOST):

        #Initializing variable
        self.HOST = HOST

        try:
            ip_input = ipaddress.ip_address(self.HOST)
            subnet = ipaddress.ip_network("10.85.24.0/21")

            # Condition : Entered IP should be present in given subnet
            if ip_input in subnet:
                print("IP accepted...!")

        except:
            print("Enter valid IP address")

    # Function for connecting to interactive shell
    def connectShell(self, HOST, PORT, USER, PASSWORD):
        
        # Initializing variables
        self.HOST = HOST
        self.PORT = PORT
        self.USER = USER
        self.PASSWORD =PASSWORD
 
        global client

        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()

            # Policy that SSHClient should use when the SSHServer's hostname 
            # is not in either system host keys or the application keys.
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # SSH connection with specified HOST.
            client.connect(self.HOST, self.PORT, self.USER, self.PASSWORD)
            print("Connected....!")
        
        except Exception:
            print("Unable to connect")

