import os

fin = open('word.txt')
print(os.getcwd())
i=0
for line in fin:
    i=i+1
    if i==100:
        break
    worr=line.strip()
    print(worr)
