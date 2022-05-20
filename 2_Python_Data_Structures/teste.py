fh = open("romeo.txt", "r")

for line in fh:
    print(line.strip())

for linha in fh:
    print(linha.strip(), "a")

fh.close()
