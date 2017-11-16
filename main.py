from options import Options
import plcActions


def showMenu():
    menuString = ""
    #TODO enumerate Options directly?
    menuOptions = {Options.EXIT.value: "Exit", Options.READCOILS.value: "Read outputs", Options.WRITECOILS.value: "Write outputs", Options.READREGISTERS.value: "Read registers", Options.WRITEREGISTERS.value: "Write registers", Options.READINPUTS.value: "Read inputs"}
    for option in menuOptions:
        menuString += "\n\t" + str(option) + ")\t" + menuOptions[option]
    menuString += "\n\n\tPlease select:\t"
    userSelection = input(menuString)
    return userSelection


def executeOption(option):  #Returns 0 if user executed an valid option, 1 otherwise.
    if option == Options.READCOILS.value:
        plcActions.readPorts()
        return 0
    elif option == Options.WRITECOILS.value:
        plcActions.writePorts()
        return 0
    elif option == Options.READREGISTERS.value:
        plcActions.readRegister()
        return 0
    elif option == Options.WRITEREGISTERS.value:
        plcActions.writeRegister()
        return 0
    elif option == Options.READINPUTS.value:
        plcActions.readInputs()
        return 0
    else:
        return 1


def main():
    # plcActions.selectTarget()
    option = eval(showMenu())
    while option != Options.EXIT.value:
        exitCode = executeOption(option)
        if(exitCode == 1):
            print('\n\tInvalid option, exitcode: ' + str(exitCode) + '\n')
        option = eval(showMenu())
    plcActions.closeTarget()


main()