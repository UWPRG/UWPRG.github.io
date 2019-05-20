i = 82
content=[]
with open('raw_pubs_old.txt','r') as file:
    for line in file:
        line = line.split()
        line[0] = str(i)+'.'
        line = ' '.join(line)
        content.append(line)
        i -= 1


with open('raw_pubs_04_19.txt','w') as file:
    for line in content:
        file.write(line+'\n')
