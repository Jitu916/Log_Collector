'''Data collection in Flex'''

import Connection as conn
import time

class FlexDataCollect:   
    # Default constructor 
    def __init__(self):
        pass
    
    # Function for triggering commands to interactive shell
    def executeCommands(self):
        try:
            # Invoking flex interactive shell
            shell = conn.client.invoke_shell()

            # List of commands to be executed on shell
            commands = [ 
            "support data-collect list",
            "support data-collect", 
            "support data-collect list",
            ]


            for command in commands:
                # sending commands to interactive shell 
                shell.send(command + "\n")                
            
                if command == "support data-collect":
                    time.sleep(190)               
                                          
            
                elif command == "support elevate":
                    time.sleep(5)
                    shell.send("P@ssw0rdpassword\n")
                    time.sleep(10)
                
                elif command == "support data-collect list":  
                    time.sleep(20)
                else:
                    time.sleep(10) 
                
                # Receiving output from shell
                out = shell.recv(65000)               
                print(out.decode(), end='')

        except:
            print("Unable to execute commands...!")

        finally:
            conn.client.close()
        

