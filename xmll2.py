import xml.etree.ElementTree as ET
input = '''<stuff>
 <users>
  <user x = "2">
      <id>009</id>
      <name>James</name>
  </user>
  <user x = "17" >
      <id>23</id>
      <name>Webb</name>
  </user>
 </users>
</stuff> '''

stuff= ET.fromstring(input)
print(stuff)
lst=stuff.findall('users/user')
print('User count: ', len(lst))
for item in lst:
    print('Name:', item.find('name').text)
    print('id:', item.find('id').text)
    print('Attribute', item.get('x'))