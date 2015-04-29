import urllib
import urllib2 
print ('------------------------error 404 ------------------------------------------')
url = 'https://api.ordnancesurvey.co.uk/places/v1/addresses/find?'
values = {'query':'''ORDNANCE SURVEY, 4, ADANAC DRIVE, NURSLING, SOUTHAMPTON, SO1 0AS''',
          'dataset':'DPA,LPI', 
          'key':'6e0WvXJsEzPd1G1pqkRMlGgODvsEg50G'}
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
try:
    f = urllib2.urlopen(req)
    
except urllib2.HTTPError, e:
            if e.code == 401:
                print '401 not authorized'
            elif e.code == 404:
                print '404 not found'
            elif e.code == 503:
                print 'service unavailable'
            else:
                print 'unknown error: '
else:
            print 'success'
    
            response=f.read()

            for line in response.splitlines():
                
                word_lst = line.split(':')
                for word in word_lst:
                    if '"ADDRESS" ' in word: print(line)
                    if 'COORDINATE' in word: print(line)    
                    if 'UPRN' in word: print(line)
            f.close()
print ('------------------------error 401 ------------------------------------------')

url = 'https://api.ordnancesurvey.co.uk/places/v1/addresses/find?'
values = {'query':'''ORDNANCE SURVEY, 4, ADANAC DRIVE, NURSLING, SOUTHAMPTON, SO1 0AS''',
          'dataset':'DPA,LPI', 
          'key':'6e0WvXJsEzPd1G1pqkRMlGgODvsEg50G'}
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
try:
    f = urllib2.urlopen(req)
except urllib2.HTTPError, e:
            if e.code == 401:
                print '401 not authorized'
            elif e.code == 404:
                print '404 not found'
            elif e.code == 503:
                print 'service unavailable'
            else:
                print 'unknown error: '
else:
            print 'success'
    
            response=f.read()

            for line in response.splitlines():
                
                word_lst = line.split(':')
                for word in word_lst:
                    if '"ADDRESS" ' in word: print(line)
                    if 'COORDINATE' in word: print(line)    
                    if 'UPRN' in word: print(line)
            f.close()
            
print ('------------------------second try ------------------------------------------')
url = 'https://api.ordnancesurvey.co.uk/places/v1/addresses/find'
values = {'query':'ORDNANCE SURVEY, 4, ADANAC DRIVE NURSLING SOUTHAMPTON SO1 0AS',
          'dataset':'DPA,LPI', 
          'key':'6e0WvXJsEzPd1G1pqkRMlGgODvsEg50G'}
full_url = url + '?' + data
print full_url
try:
    f = urllib2.urlopen(full_url)
except urllib2.HTTPError, e:
            if e.code == 401:
                print '401 not authorized'
            elif e.code == 404:
                print '404 not found'
            elif e.code == 503:
                print 'service unavailable'
            else:
                print 'unknown error: '
else:
            print 'success'
    
            response=f.read()
            response_count = 0
            for line in response.splitlines():
                word_lst = line.split(':')
                for word in word_lst:
                    
                    if response_count < 10:

                        if 'UPRN' in word:  
                            response_count = response_count + 1
                            print '-'*80
                            print(line)
                        if '"ADDRESS" ' in word: print(line)
                        if 'COORDINATE' in word: print(line)
                        if 'MATCH' in word: print(line)
            
            f.close()

