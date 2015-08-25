import http.client

connection1 = http.client.HTTPSConnection('www.somesecuresite.com')



conn = http.client.HTTPConnection('https://api.ordnancesurvey.co.uk/places/v1/addresses',8080)
print (conn)
conn.request("GET", "https://api.ordnancesurvey.co.uk/places/v1/addresses/uprn?uprn=100050557412")
r1 = conn.getresponse()
response = r1.read()
print (str(response))
