from pymodbus3.client.sync import ModbusTcpClient
import options
import plcActions


clientIP = str(input('Target IP? '))
client = ModbusTcpClient(clientIP)
client.connect()


def showMenu():
    menuOptions = "\t0)\tExit\n\t1)\tRead outputs\n\t2)\tWrite outputs\n\n\tPlease select:\t"
    userSelection = input(menuOptions)
    return userSelection


def executeOption(option):  #Returns 0 if user executed an valid option, 1 otherwise.
    if option == options.READPORTS:
        plcActions.readPorts()
        return 0
    elif option == options.WRITEPORTS:
        plcActions.writePorts()
        return 0
    else:
        return 1


def shutdown():
    client.close()



def main():
    option = eval(showMenu())
    while option != 0:
        exitCode = executeOption(option)
        if(exitCode == 1):
            print('\n\tInvalid option, exitcode: ' + str(exitCode) + '\n')
        option = eval(showMenu())


main()