from options import Options
import plcActions


def showMenu():
    menuArray = ["Exit", "Read outputs", "Write outputs", "Read registers", "Write registers"]  #TODO Add dictionary? now the program only works if strings are ordered right
    menuOptions = ""
    for i in range(0, len(menuArray)):
        menuOptions += "\n\t" + str(i) + ")\t" + menuArray[i]
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