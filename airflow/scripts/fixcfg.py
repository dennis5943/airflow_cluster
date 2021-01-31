import re
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--filename', '-f', type=str, required=True, help='需要修改的檔案名稱')
parser.add_argument('--search', '-s', type=str, required=True, help='搜尋字串，支援正規表示法')
parser.add_argument('--replacement', '-r', type=str, required=True, help='要取代的字串')

args = parser.parse_args()

print(args.filename)

def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print('"{old_string}" not found in {filename}.'.format(**locals()))
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        print('Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
        #s = s.replace(old_string, new_string)
        s = re.sub(old_string, new_string, s)
        f.write(s)

inplace_change(args.filename,args.search,args.replacement)