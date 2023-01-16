message = 'You have received a message from: valentinaburbano9@gmail.com and you can answer it'
words=message.split()
correo=words[6]
pieces=correo.split('@')
print(pieces[1])