x='This message was sended by valentinaburbano9@unal.edu.co and you can answer it'
atpost=x.find('@')
print(atpost)
endpost=x.find(' ',atpost)
print(endpost)
print(x[atpost+1:endpost])
      