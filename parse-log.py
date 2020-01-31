import re

def parse(filelog):
    with open(filelog, 'r') as f:
        r = f.readline()
        while r:
            ip = re.findall(r'(^[\w\.]*)(?= - - )', r)
            print(ip)
            r = f.readline()

if __name__ == '__main__':
    parse('nginx.access')