from urllib2 import Request, urlopen, URLError, HTTPError

url = 'https://api.ordnancesurvey.co.uk/places/v1/addresses/bbox?'

params = [['bbox',437318.0,115426.1,437367.0,115766.0],['dataset','DPA','LPI'],['key','INSERT_YOUR_API_KEY_HERE']]

for param_count, param in enumerate(params): #a list
    for value_count, value in enumerate(param):
        if value_count ==0:
            if param_count ==0:
                data=value + '='
            else:
                data = data + '&' + str(value) + '='
        elif value_count == 1:
            data = data + str(value)
        else :
            data = data + ','+ str(value)
print (url + data)
req = Request(url + data)
try:
    f = urlopen(req)
    print (f)
except HTTPError, e:
            if e.code == 401:
                print 'not authorized'
            elif e.code == 404:
                print 'not found'
            elif e.code == 503:
                print 'service unavailable'
            else:
                print 'unknown error: '
else:
            print 'success'
   
response = f.read()
#print 'RESPONSE:', response 
for line in response.splitlines():
       
    word_lst = line.split(':')
    for word in word_lst:
        if '"ADDRESS" ' in word: print(line)
        if 'COORDINATE' in word: print(line)
        if 'UPRN' in word: print(line)
f.close()
