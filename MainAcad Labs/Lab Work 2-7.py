f = open('myfile.txt','w')

f.write("Hello file world!")

f.close()



f = open('myfile.txt','w+')

print(f.read())

f.seek(len("Hello "))
f.write("my " + "file world!")
f.flush()
