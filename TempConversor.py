def StrTempOptions(option):
    temp = ['Celcius (C)', 'Fahrenheit (F)', 'Kelvin']

    match option:
        case 1:
            return temp[0]
        case 2:
            return temp[1]
        case 3:
            return temp[2]


def TempDictionary(opt_unit_1, opt_unit_2, unit_1):
    match opt_unit_1:
        case 1:
            #Add an option to round it only to 2 decimals
            print(unit_1, StrTempOptions(opt_unit_1) , 'converted to' , StrTempOptions(opt_unit_2), 'is: ',CelciusDictionary(opt_unit_2, unit_1), StrTempOptions(opt_unit_2))
        case 2:
            print(unit_1, StrTempOptions(opt_unit_1) , 'converted to' , StrTempOptions(opt_unit_2), 'is: ',FahrenheitDictionary(opt_unit_2, unit_1), StrTempOptions(opt_unit_2))
        case 3:
            print(unit_1, StrTempOptions(opt_unit_1) , 'converted to' , StrTempOptions(opt_unit_2), 'is: ',KelvinDictionary(opt_unit_2, unit_1), StrTempOptions(opt_unit_2))
    input('Press any key to continue...')

def CelciusDictionary(opt_unit_2, unit_1):
    match opt_unit_2:
        case 2: #Fahrenheit
            return (unit_1 * 9/5) + 32
        case 3: #Kelvin
            return unit_1 + 273.15

def FahrenheitDictionary(opt_unit_2, unit_1):
    match opt_unit_2:
        case 1: #Celcius
            return (unit_1 - 32) * (5/9)
        case 3: #Kelvin
            return (unit_1 - 32) * (5/9) + 273.15

def KelvinDictionary(opt_unit_2, unit_1):
    match opt_unit_2:
        case 1: #Celcius
            return unit_1 - 273
        case 2: #Fahrenheit
            return (unit_1 - 273.15) * (9/5) + 32