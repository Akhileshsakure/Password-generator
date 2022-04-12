# Password Generator
import generator


if __name__ == '__main__':
    lowCase = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'x', 'y', 'z')
    upCase = (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'X', 'Y', 'Z')
    numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    specialChar = ('£', '$', '&', '(', ')', '*', '+', '[', ']', '@', '#', '^', '-', '_', '!', '?')

    pass_len = int(input('Length of the password: '))
    lowCase_choice = input('Should it contain a lower case letter? (Y/N): ')
    upCase_choice = input('Should it contain a upper case letter? (Y/N): ')
    numbers_choice = input('Should it contain a number? (Y/N): ')
    specialChar_choice = input('Should it contain a special character? (Y/N): ')

    charGroup = []

    if lowCase_choice in ['Y', 'y']:
        charGroup.append(lowCase)
    if upCase_choice in ['Y', 'y']:
        charGroup.append(upCase)
    if numbers_choice in ['Y', 'y']:
        charGroup.append(numbers)
    if specialChar_choice in ['Y', 'y']:
        charGroup.append(specialChar)

    password = generator.Generator(pass_len, charGroup)

    print(f'Your password is:\n{password}')