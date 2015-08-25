import urllib

url = 'https://api.ordnancesurvey.co.uk/places/v1/addresses/bbox?%s'
url_full = 'https://api.ordnancesurvey.co.uk/places/v1/addresses/bbox?bbox=437318.0,115426.1,437367.0,115766.0&dataset=DPA,LPI&key=INSERT_YOUR_API_KEY_HERE'
params = urllib.urlencode({'bbox':'437318.0,115426.1,437367.0,115766.0','dataset':'DPA,LPI','key':'INSERT_YOUR_API_KEY_HERE'})

try:
    f = urllib.urlopen(url % params)
except Exception as e:
    print(str(e))
   
response = f.read()
#print 'RESPONSE:', response 
for line in response.splitlines():
     
    word_lst = line.split(':')
    for word in word_lst:
        if '"ADDRESS" ' in word: print(line)
        if 'COORDINATE' in word: print(line )   
        if 'UPRN' in word: print(line)
f.close()
