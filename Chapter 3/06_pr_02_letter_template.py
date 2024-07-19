letter='''Dear <|NAME|>
You are selected

Date <|DATE|>'''
name=input("ENTER YOUR NAME\n")
date=input("ENTER DATE\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)