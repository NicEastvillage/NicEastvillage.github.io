import os
import re

my_name = 'Nicolaj Østerby Jensen'


def braced(s):
    return '{{ ' + s + ' }}'

def resolve_file(file):
    with open(file, 'r') as f:
        content = f.read()
        print(content)
        while match := re.search(r'\{\{(.*?)\}\}', content, flags=re.MULTILINE):
            globals()['out'] = ''
            code = match.group(1).strip()
            exec(code, globals())
            content = re.sub(r'\{\{(.*?)\}\}', str(globals().get('out', '')), content, count=1, flags=re.MULTILINE)
            print(content)
        return content


def generate_file(file, base):
    content = resolve_file(base)


generate_file('index.html', '_meta/index.html')
for f in os.listdir('_posts'):
    print(f)
