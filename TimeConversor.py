readable_time = ['404', 'second/s', 'minute/s', 'hour/s', 'day/s', 'week/s', 'month/s', 'year/s']

def time_dictionary(selection_1, selection_2, value):
    Message(value, selection_1, selection_2)
    input('Enter any key to continue...')

def Message(value, selection_1, selection_2):
    func = 0
    match selection_1:
        case 1: 
            func = seconds_dictionary(selection_2, value)
        case 2: 
            func = minutes_dictionary(selection_2, value)
        case 3: 
            func = hours_dictionary(selection_2, value)
        case 4: 
            func = days_dictionary(selection_2, value)
        case 5: 
            func = weeks_dictionary(selection_2, value)
        case 6:
            func = months_dictionary(selection_2, value)
        case 7:
            func = year_dictionary(selection_2, value)

    print(f'{value} {readable_time[selection_1]} converted to {readable_time[selection_2]} is: {func:.2f}  {readable_time[selection_2]}')


def seconds_dictionary(selection_2, value):
    conversions = {
        2: value / 60,        # to minutes
        3: value / 3600,      # to hours
        4: value / 86400,     # to days
        5: value / 604800,    # to weeks
        6: value / 2.628e+6,  # to months (approx. 30.44 days)
        7: value / 3.154e+7   # to years (approx. 365.25 days)
    }
    return conversions.get(selection_2, "Invalid conversion")


def minutes_dictionary(selection_2, value):
    conversions = {
        1: value * 60,        # to seconds
        3: value / 60,        # to hours
        4: value / 1440,      # to days
        5: value / 10080,     # to weeks
        6: value / 43800,     # to months
        7: value / 525600     # to years
    }
    return conversions.get(selection_2, "Invalid conversion")


def hours_dictionary(selection_2, value):
    conversions = {
        1: value * 3600,      # to seconds
        2: value * 60,        # to minutes
        4: value / 24,        # to days
        5: value / 168,       # to weeks
        6: value / 730,       # to months
        7: value / 8760       # to years
    }
    return conversions.get(selection_2, "Invalid conversion")


def days_dictionary(selection_2, value):
    conversions = {
        1: value * 86400,     # to seconds
        2: value * 1440,      # to minutes
        3: value * 24,        # to hours
        5: value / 7,         # to weeks
        6: value / 30.44,     # to months
        7: value / 365.25     # to years
    }
    return conversions.get(selection_2, "Invalid conversion")


def weeks_dictionary(selection_2, value):
    conversions = {
        1: value * 604800,    # to seconds
        2: value * 10080,     # to minutes
        3: value * 168,       # to hours
        4: value * 7,         # to days
        6: value / 4.345,     # to months
        7: value / 52.143     # to years
    }
    return conversions.get(selection_2, "Invalid conversion")

def months_dictionary(selection_2, value):
    conversions = {
        1: value * 2.628e+6,  # to seconds
        2: value * 43800,     # to minutes
        3: value * 730,       # to hours
        4: value * 30.44,     # to days
        5: value * 4.345,     # to weeks
        7: value / 12         # to years
    }
    return conversions.get(selection_2, "Invalid conversion")

def year_dictionary(selection_2, value):
    conversions = {
        1: value * 3.154e+7,  # to seconds
        2: value * 525600,    # to minutes
        3: value * 8760,      # to hours
        4: value * 365.25,    # to days
        5: value * 52.143,    # to weeks
        6: value * 12         # to months
    }
    return conversions.get(selection_2, "Invalid conversion")
