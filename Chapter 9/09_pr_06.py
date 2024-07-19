with open('file.log') as f:
    c=f.read()
if "python" in c:
    print("present")
else:
    print("not present")