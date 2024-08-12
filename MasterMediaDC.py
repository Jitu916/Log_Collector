import Connection as conn
import time
from Credentials import *


class MasterMediaDataCollect:
    # Default constructor 
    def __init__(self):
        pass

    # Function for triggering commands to interactive shell
    def executeCommands(self,PATH):
        try:
            # Invoking interactive shell
            shell = conn.client.invoke_shell()
            ch=input("For advanced logs press 1 else press 2....\n")
            cd=""
            s=0
            if ch=='1':
                cd="/usr/openv/netbackup/bin/support/nbcplogs {}logsOutput/$(date +%Y-%m-%d)-$(hostname -s)-nbcplogs-$(date +%s) --tmpdir=$(pwd) --nbsu --bundle --duration 1h".format(PATH)
                s=300
            else:
                cd="/usr/openv/netbackup/bin/support/nbcplogs {}logsOutput/$(date +%Y-%m-%d)-$(hostname -s)-nbcplogs-$(date +%s) --tmpdir=$(pwd) --no-nbsu --bundle --duration 1h".format(PATH)
                s=50

            command = ["sudo su",
                    "rm -rf {}logsOutput/".format(PATH),
                    "mkdir {}logsOutput/".format(PATH),
                    cd,
                    "exit",            
                    "ls -la {}logsOutput/".format(PATH)
                    ]

            for cmd in command:          # sends commands to interactive shell   
                shell.send(cmd + "\n")
                if cmd == cd:   
                    time.sleep(10)
                    shell.send("y\n") 
                    time.sleep(s)                 # time for execution of command in seconds
            
                elif cmd == "sudo su":
                    shell.send("{}\n".format(PASSWORD))
                    time.sleep(1)

                else:
                    time.sleep(5)
                    
                out = shell.recv(650000000)  
                print(out.decode(), end='')
                    

        except Exception:
            print("Unable to connect")

        finally:
            conn.client.close()
            