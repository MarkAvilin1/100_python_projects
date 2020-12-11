with open(file="../file.txt", mode="w") as w:
    w.write("""Hello, my name is mark!
I'm 32 years old.
My favourite food is pizza.""")

with open("../file.txt", "r")as r:
    contents = r.read()
    print(contents)
