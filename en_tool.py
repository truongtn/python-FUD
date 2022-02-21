import base64
file_name = input('Press file name: ')
f = open(file_name)
a = f.read()
encoded = a.encode("utf-8")
encoded = base64.b64encode(encoded)

f2 = open('file_fud.py','w+')
content = """
import base64
myscript = """+str(encoded)+"""
eval(compile(base64.b64decode(myscript),'<string>','exec'))
"""
f2.write(content)