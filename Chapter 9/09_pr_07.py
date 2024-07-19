content=True
i=1
with open('file.log') as f:
    while content:
        content=f.readline()
        if "python" in content.lower():
            print(content)
            print(f"the python is present on line number {i}")
        i+=1