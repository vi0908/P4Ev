name = input('Enter file name: ')
fhandle = open(name)

count = dict()
for line in fhandle:
    words = line.split()
    for word in words:
       count[word]= count.get(word,0) + 1

bigcount = None
bigword = None
for word,counting in count.items():
    if bigcount is None or counting > bigcount:
        bigcount = counting
        bigword = word

print(bigword, bigcount)


