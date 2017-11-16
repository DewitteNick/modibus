import pip
try:
    from pymodbus3.client.sync import ModbusTcpClient
except Exception as e:
    print("installing required module: pymodbus3")
    pip.main(['install','pymodbus3'])


def selectTarget():
    clientIP = str(input('Target IP? '))
    client = ModbusTcpClient(clientIP)
    client.connect()
    return client


def readCoils():
    coils = int(input('How many coils should be scanned? '))
    for position in range(0, coils):
        result = client.read_coils(position, 1)
        plcPort = '%Qx' + str(position // 8) + '.' + str(position % 8)
        print('Port ' + str(plcPort), result.bits[0])


def writeCoils():   #TODO ask amount of coils
    coils = int(input('How many coils are present? '))
    data = [False] * coils
    portSelected = int(input("Select a coil to enable. Others are disabled by default. Press 0 to submit "))
    while portSelected != 0:
        dataChosen = eval(input("Select data to be written. Bools begin with a capital, strings are with quotes "))
        data[portSelected - 1] = dataChosen
        portSelected = int(input("Select a coil to enable. Others are disabled by default. Press 0 to submit "))
    client.write_coils(0, data)


# Holding registers are the most universal 16-bit register,
# may be read or written, and may be used for a variety of things
# including inputs, outputs, configuration data, or any requirement for "holding" data.

def readRegister():
    starting_adress = eval(input('Starting adress? '))
    adress_count = int(input('How many adressess should be scanned? (Max 125)'))
    data = client.read_holding_registers(starting_adress, adress_count)
    try:
        print(data.registers)
    except Exception as e:
        print(data)


def writeRegister():
    starting_adress = int(input('Starting adress? '))
    adress_count = int(input('How many adressess should be scanned? (total should be < 126) '))
    registers = [0x00] * adress_count
    registerSelected = eval(input('select register to write to. Others are 0x00 by default. Press 0 to submit'))
    while registerSelected != 0:
        dataChosen = int(input('Select data to be written. Should be an integer smaller >= 65535'))
        registers[registerSelected - 1] = dataChosen
        registerSelected = eval(input('select register to write to. Others are 0x00 by default. Press 0 to submit'))
    client.write_registers(0, registers)    #TODO replace 0 with starting_adress


def readInputs():
    starting_adress = eval(input('Starting input? '))
    adress_count = int(input('How many inputs should be scanned? '))
    data = client.read_discrete_inputs(starting_adress, adress_count)
    for position in range(0, len(data.bits)):
        plcInput = '%Ix' + str(position // 8) + "." + str(position % 8)
        print("Input " + plcInput, data.bits[position])





def closeTarget():
    client.close()




client = selectTarget()


