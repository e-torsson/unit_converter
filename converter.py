CONV_FACTOR_FEET = 3.28084
CONV_FACTOR_F = 9/5
CONV_FACTOR_LBS = 2.20462
CONV_FACTOR_GAL = 0.264172

def check_input(prompt: str) -> float:
    while True:
        user_value = input(prompt)
        try:
            if '.' in user_value:
                return float(user_value)
            else:
                return int(user_value)
        except ValueError:
            print('Invalid input. Please enter a numerical value.')

def len_converter(input_len):
    value = input_len * CONV_FACTOR_FEET
    return value, 'Meters to feet'


def temp_converter(input_temp):
    value = (input_temp * CONV_FACTOR_F) + 32
    return value, 'Celcius to Fahrenheit'

def weight_converter(input_weight):
    value = input_weight * CONV_FACTOR_LBS
    return value, 'Kilograms to pounds'

def other_converter(input_vol):
    value = input_vol * CONV_FACTOR_GAL
    return value, 'Liters to gallons'


def option_menu():
    print('''
          1. Length (m -> feet)
          2. Temperature (C -> F)
          3. Weight (Kg -> lbs)
          4. Other (Liter to gallons)
          ''')

def main():
    conversion_options = {
        1: len_converter,
        2: temp_converter,
        3: weight_converter,
        4: other_converter
    }
    while True:
        print('''
              1. Select Conversion Type
              2. Exit
              ''')
        user_input = check_input('Please select what you wish to do:\n')
        
        if user_input == 1:
            option_menu()
            conversion_type = check_input('Enter your choice:\n')
            if conversion_type in conversion_options:
                user_value = check_input('Enter the value to convert:\n')
                converted_value, convsersion_description = conversion_options[conversion_type](user_value)
                print(f'Converted value: {converted_value} ({convsersion_description})')
                
            else:
                print('Invalid option, please try again')
                
        elif user_input == 2:
            print("Exiting...")
            break
        
        else:
            print('Unknown input, please try again')
            
    


if __name__ == '__main__':
    main()