def weight_converter(weight):
    try:
        weight = float(weight)
    except ValueError:
        print('Your input is not a number. Please enter a valid Number!')
    output = weight
    if isinstance(weight, float):
        output = weight
        unit = input('(L)bs or (K)g: ')
        unit = unit.lower()
        if unit == 'l':
            output = weight * 0.45
            print(f'You are {output:.1f} Kg.')
        elif unit == 'k':
            output = weight / 0.45
            print(f'You are {output:.1f} Lbs.')
        else:
            print('Please enter only "L" or "K"!')
    return output


def num_check(number):
    try:
        number = float(number)
    except ValueError:
        print('Your input is not a number. Please enter a valid Number!')
    return number


def lbs_converter(weight):
    weight_kg = weight * 0.45
    return weight_kg


def kg_converter(weight):
    weight_lbs = weight / 0.45
    return weight_lbs