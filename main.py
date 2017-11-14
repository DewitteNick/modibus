from pymodbus3.client.sync import ModbusTcpClient



clientIP = str(input('Target IP? '))
client = ModbusTcpClient(clientIP)
client.connect()


def writePorts():
    data = [False] * 16
    portSelected = int(input("Select a coil to enable. Others are disabled by default. Press 0 to submit "))
    while portSelected != 0:
        dataChosen = eval(input("Select data to be written. Bools begin with a capital, strings are with quotes "))
        data[portSelected - 1] = dataChosen
        portSelected = int(input("Select a coil to enable. Others are disabled by default. Press 0 to submit "))
    client.write_coils(1, data)


def showMenu():
    menuOptions = "\t0)\tExit\n\t1)\tRead outputs\n\t2)\tWrite outputs\n\n\tPlease select:\t"
    userSelection = input(menuOptions)
    return userSelection

def executeOption(option):
    if option == 1:
        readPorts()
        return 0
    elif option == 2:
        writePorts()
        return 0
    else:
        return 1

def readPorts():
    ports = int(input('how many coils should be scanned? '))
    for position in range(0, ports):
        result = client.read_coils(position, 1)
        plcPort = '%Qx' + str(position // 8) + '.' + str(position % 8)
        print('Port ' + str(plcPort), result.bits[0])



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