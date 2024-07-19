with open('poem.txt','r') as f:
    a=f.read()
    if 'twinkle' in a:
        print("twinkle is present")
    else:
        print("twinkle is not present")