import urllib2

url = 'https://api.ordnancesurvey.co.uk/places/v1/addresses/uprn?%s'
params = urllib2.urlencode({'uprn':200010019924,'dataset':'DPA,LPI', 'key':'INSERT_YOUR_API_KEY_HERE'})

try:
    f = urllib2.urlopen(url % params)
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