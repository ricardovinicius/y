import subprocess
import sys
import Server

def startServer(HOST, PORT):
    server = Server()


def Main():
    
    # Checks if args are passed
    argsSize = len(sys.argv)

    if (argsSize != 4):
        sys.exit("Correct usage of program: python y.py EXEC_TYPE IP_ADDR PORT")

    # Checks the type of execution

    execType = sys.argv[1]

    if (execType == "-s"):

    elif (execType == "-c"):
        subprocess.run(["python", "./src/server/startClient.py"])
    else:
        sys.exit("EXEC_TYPE must be -s for server or -c for client")
    

if __name__ == '__main__':
    Main()