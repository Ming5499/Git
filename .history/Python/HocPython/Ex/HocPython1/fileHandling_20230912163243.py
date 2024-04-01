try:
    with open('Python\HocPython\Ex\HocPython1\s3.txt',  'r') as file:

        data = file.read()
        print(data)
except FileNotFoundError as e:
    print('ERROR', e)
-----------------------------------------------------------------------

with open('Python\HocPython\Ex\HocPython1\s3.txt', 'a') as file:
    file.writelines(['\nThis is new line!!!!', '\nThis is 2nd line'])
    