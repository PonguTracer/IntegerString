user_string = input('enter string: ')

is_integer = True  # Assume it's an integer until proven otherwise

for char in user_string:
    if not char.isdigit():
        is_integer = False  # If a non-digit character is found, it's not an integer
        break  # Exit the loop early

if is_integer:
    print('Yes')
else:
    print('No')
