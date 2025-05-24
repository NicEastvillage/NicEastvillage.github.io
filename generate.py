import os
import re

my_name = 'Nicolaj Østerby Jensen'


def resolve_file(file):
    with open(file, 'r') as f:
        content = f.read()

        start = 0
        balance = 0
        braces=[]
        while match := re.search(r'\{\{|\}\}', content[start:], flags=re.MULTILINE):
            s = match.group()
            if s == '{{':
                braces.append(match.span())
                balance += 1
            elif s == '}}':
                braces.append(match.span())
                balance -= 1
                assert balance >= 0
            if balance == 0:
                code = content[braces[0][1]:start + braces[-1][0]].strip()
                globals()['out'] = ''
                exec(code, globals())
                content = content[:braces[0][0]] + str(globals().get('out', '')) + content[start + braces[-1][1]:]
                # Restart
                start = 0
                braces = []
            else:
                start += match.span()[1]
        assert balance == 0, 'Unbalanced braces'
        return content


def generate_file(file, base):
    content = resolve_file(base)
    print(content)


generate_file('index.html', '_meta/index.html')
for f in os.listdir('_posts'):
    print(f)
