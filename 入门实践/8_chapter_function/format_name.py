def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print('please tell me your name')
    print("(enter 'q' ant any time to quit)")
    f_name = input('First Name: ')
    if f_name == 'q':
        break
    l_name = input('listname: ')
    if l_name == 'q':
        break
    format_name = get_formatted_name(f_name, l_name)
    print('Hello, ' + format_name + '!')

# 位置实参传值
musician = get_formatted_name('haster', 'harry')

print(musician)
