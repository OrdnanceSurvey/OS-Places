import urllib

opener = urllib.FancyURLopener({})
url = 'https://api.ordnancesurvey.co.uk/places/v1/addresses/postcode?%s'
params = urllib.urlencode({'postcode':'so16%200AS','dataset':'DPA,LPI', 'key':'INSERT_YOUR_API_KEY_HERE'})

try:
    f = urllib.urlopen(url % params)
except Exception as e:
    print(str(e))
    
response=f.read()
#print 'RESPONSE:', response


for line in response.splitlines():
    
    word_lst = line.split(':')
    for word in word_lst:
        if '"ADDRESS" ' in word: print(line)
        if 'UPRN' in word: print(line)
        if 'COORDINATE' in word: print(line)    
f.close()
