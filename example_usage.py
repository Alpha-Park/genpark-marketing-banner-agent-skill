import sys
from client import Client
def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    c = Client()
    res = c.process("Test Input")
    print(res)
if __name__ == '__main__':
    main()
