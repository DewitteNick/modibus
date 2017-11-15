from options import Options
import plcActions


def showMenu():
    menuOptions = "\t0)\tExit"  #TODO create for loop, and put options in an array.
    menuOptions += "\n\t1)\tRead outputs\n\t2)\tWrite outputs\n\t3)\tRead registers\n\t4)\tWrite registers"
    menuOptions += "\n\n\tPlease select:\t"
    userSelection = input(menuOptions)
    return userSelection


def executeOption(option):  #Returns 0 if user executed an valid option, 1 otherwise.
    if option == Options.READPORTS.value:
        plcActions.readPorts()
        return 0
    elif option == Options.WRITEPORTS.value:
        plcActions.writePorts()
        return 0
    elif option == Options.READREGISTERS.value:
        plcActions.readRegister()
        return 0
    elif option == Options.WRITEREGISTERS.value:
        plcActions.writeRegister()
        return 0
    else:
        return 1


def main():
    # plcActions.selectTarget()
    option = eval(showMenu())
    while option != 0:
        exitCode = executeOption(option)
        if(exitCode == 1):
            print('\n\tInvalid option, exitcode: ' + str(exitCode) + '\n')
        option = eval(showMenu())
    plcActions.closeTarget()


main()