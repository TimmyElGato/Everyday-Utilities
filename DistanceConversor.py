def StrDistanceOptions(option):
    distance = ['meter(s)',  'cm(s)', 'Km(s)', 'mile(s)', 'foot(s)', 'inch(es)']
    match option:
        case 1:
            return (distance[0])
        case 2:
            return (distance[1])
        case 3:
            return (distance[2])
        case 4:
            return (distance[3])
        case 5:
            return (distance[4])
        case 6:
            return (distance[5])        
        
def DistanceDictionary(opt_unit_1, opt_unit_2, unit_1):
    match opt_unit_1:
        case 1:
            #Add an option to round it only to 2 decimals
            print(unit_1, StrDistanceOptions(opt_unit_1) , 'converted to' , StrDistanceOptions(opt_unit_2), 'is: ',MeterDictionary(opt_unit_2, unit_1), StrDistanceOptions(opt_unit_2))
        case 2:
            print(unit_1, StrDistanceOptions(opt_unit_1) , 'converted to' , StrDistanceOptions(opt_unit_2), 'is: ',CentimeterDictionary(opt_unit_2, unit_1), StrDistanceOptions(opt_unit_2))
        case 3:
            print(unit_1, StrDistanceOptions(opt_unit_1) , 'converted to' , StrDistanceOptions(opt_unit_2), 'is: ',KilometerDictionary(opt_unit_2, unit_1), StrDistanceOptions(opt_unit_2))
        case 4:
            print(unit_1, StrDistanceOptions(opt_unit_1) , 'converted to' , StrDistanceOptions(opt_unit_2), 'is: ',MileDictionary(opt_unit_2, unit_1), StrDistanceOptions(opt_unit_2))
        case 5:
            print(unit_1, StrDistanceOptions(opt_unit_1) , 'converted to' , StrDistanceOptions(opt_unit_2), 'is: ',FootDictionary(opt_unit_2, unit_1), StrDistanceOptions(opt_unit_2))
        case 6:
            print(unit_1, StrDistanceOptions(opt_unit_1) , 'converted to' , StrDistanceOptions(opt_unit_2), 'is: ',InchDictionary(opt_unit_2, unit_1), StrDistanceOptions(opt_unit_2))
        case _:
            print('Error 404')
    input('Press any key to continue...')

def MeterDictionary(opt_unit_2, unit_1):
    match opt_unit_2:
        case 2: #Centimeters
            return(unit_1 * 100)
        case 3: #Kilometrers
            return(unit_1 / 1000)
        case 4: #Miles
            return(unit_1 * 1609.344)
        case 5: #Foot
            return(unit_1 * 3.2808399)
        case 6: #Inches
            return(unit_1 * 39.3700787)


def CentimeterDictionary(opt_unit_2, unit_1):
    match opt_unit_2:
        case 1: #Meters
            return (unit_1 / 100)
        case 3: #Kilometers
            return (unit_1 / 100000)
        case 4: #Miles
            return (unit_1 / 160934.4)
        case 5: #Foot
            return (unit_1 / 30.48)
        case 6: #Inches
            return (unit_1 / 2.54)

    
def KilometerDictionary(opt_unit_2, unit_1):
    match opt_unit_2:
        case 1: #Meters
            return(unit_1 * 1000)
        case 2: #Centimeters
            return(unit_1 * 1000000)
        case 4: #Miles
            return(unit_1 * 1.609344)
        case 5: #Foot
            return(unit_1 * 3280.8399)
        case 6: #Inches
            return(unit_1 * 39370.0787)
        
def MileDictionary(opt_unit_2, unit_1):
    match opt_unit_2:
        case 1: #Meters
            return(unit_1 * 1609.344)
        case 2: #Centimeters
            return(unit_1 * 160934.4)
        case 3: #Kilometers
            return(unit_1 * 1.609344)
        case 5: #Foot
            return(unit_1 * 5280)
        case 6: #Inches
            return(unit_1 * 63360)
        
def FootDictionary(opt_unit_2, unit_1):
    match opt_unit_2:
        case 1: #Meters
            return(unit_1 * 0.3048)
        case 2: #Centimeters
            return(unit_1 * 30.48)
        case 3: #Kilometers
            return(unit_1 * 0.0003048)
        case 4: #Miles
            return(unit_1 * 0.000189394)
        case 6: #Inches
            return(unit_1 * 12)

def InchDictionary(opt_unit_2, unit_1):
    match opt_unit_2:
        case 1: #Meters
            return(unit_1 * 0.0254)
        case 2: #Centimeters
            return(unit_1 * 2.54)
        case 3: #Kilometers
            return(unit_1 * 0.0000254)
        case 4: #Miles
            return(unit_1 * 0.0000157828)
        case 5: #Foot
            return(unit_1 * 0.0833333) 
        
