import sys , os
import shlex

#support

commands = []


def tokenize(command):
    return shlex.split(command)

def shell():
    status = True
    while status == True :
        sys.stdout.write('> ')
        sys.stdout.flush()
        string = sys.stdin.readline()
        commands = tokenize(string)
        status = execute(commands)

def execute(commands) :

    # child process check
    processid = os.fork()

    if processid == 0:
        os.execvp(commands[0],commands)
    else:
        #parent
        while True :
            wpid , status = os.waitpid(processid,0)

            if os.WIFEXITED(status)  or os.WIFSIGNALED(status):
                break
    return True

if __name__ == '__main__' :
    print(">> Welcome to Shell")
    shell()
