def readfile(file):
    try:
        with open(file,'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {file} is not found")
readfile('1.txt')
readfile('2.txt')
readfile('3.txt')
readfile('4.txt')
readfile('1.txt')