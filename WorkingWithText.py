filenames = ['1.txt', '2.txt', '3.txt']

file_list = {}
for filename in filenames:
    with open(filename, encoding='utf-8') as f:
        content = f.readlines()
        count = len(content)
        file_list[count] = f'{filename}\n{count}\n{''.join(content)}\n'

with open('result.txt', 'w', encoding='utf-8') as file_write:
    for key in sorted(file_list.keys()):
        file_write.write(file_list[key])
