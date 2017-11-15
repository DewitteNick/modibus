from pymodbus3.client.sync import ModbusTcpClient


def selectTarget():
    clientIP = str(input('Target IP? '))
    client = ModbusTcpClient(clientIP)
    client.connect()
    return client


def readPorts():
    ports = int(input('how many coils should be scanned? '))
    for position in range(0, ports):
        result = client.read_coils(position, 1)
        plcPort = '%Qx' + str(position // 8) + '.' + str(position % 8)
        print('Port ' + str(plcPort), result.bits[0])


def writePorts():
    data = [False] * 16
    portSelected = int(input("Select a coil to enable. Others are disabled by default. Press 0 to submit "))
    while portSelected != 0:
        dataChosen = eval(input("Select data to be written. Bools begin with a capital, strings are with quotes "))
        data[portSelected - 1] = dataChosen
        portSelected = int(input("Select a coil to enable. Others are disabled by default. Press 0 to submit "))
    client.write_coils(1, data)


# Holding registers are the most universal 16-bit register,
# may be read or written, and may be used for a variety of things
# including inputs, outputs, configuration data, or any requirement for "holding" data.

def readRegister():
    starting_adress = int(input('Starting adress? '))
    adress_count = int(input('How many adressess should be scanned? '))
    unit = 1 #TODO scan for units?
    data = client.read_holding_registers(starting_adress, adress_count, unit)
    print(data)


def closeTarget():
    client.close()




client = selectTarget()


