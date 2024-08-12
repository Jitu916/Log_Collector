import time
from Credentials import *
import Connection as conn


class NBUClient:

    def __init__(self):
        pass

    def executeCommands(self, PATH):
        try:
            # Invoking flex interactive shell
            shell = conn.client.invoke_shell()

            commands = [ 
            "sudo su", 
            "cd /usr/openv/netbackup/bin/support/", 
            "rm -rf {}logsOutput/".format(PATH),
            "mkdir {}logsOutput/".format(PATH),
            "./nbcplogs {}logsOutput/".format(PATH),
            "cd {}logsOutput/".format(PATH),
            "ls -la",
            "exit"]

            for command in commands:
                shell.send(command + "\n")                # sends commands to interactive shell      
            
                if command == 'sudo su':
                    time.sleep(5)
                    shell.send("{}\n".format(PASSWORD))
                    time.sleep(5)

                elif command == "./nbcplogs {}logsOutput/".format(PATH):
                    time.sleep(5)
                    shell.send("y\n")
                    time.sleep(250)

                else :
                    time.sleep(5)

                out = shell.recv(6500000)                   # receive output
                print(out.decode(), end='')

        except:
            print("Unable to execute commands...!")

        finally:
            conn.client.close()
        
