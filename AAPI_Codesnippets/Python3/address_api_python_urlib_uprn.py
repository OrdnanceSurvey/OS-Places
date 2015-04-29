import urllib

url = 'https://api.ordnancesurvey.co.uk/places/v1/addresses/uprn?%s'
params = urllib.urlencode({'uprn':200010019924,'dataset':'DPA,LPI', 'key':'6e0WvXJsEzPd1G1pqkRMlGgODvsEg50G'})

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
        if 'COORDINATE' in word: print(line)    
        if 'UPRN' in word: print(line)
f.close()