from distutils.filelist import findall
import re
message='You have received a message from valentinaburbano9@outlook.com you can answer it if you want'
domain = re.findall('@([^ ]*)', message)
print(domain)