import http.client

connection1 = http.client.HTTPSConnection('www.somesecuresite.com')



conn = http.client.HTTPConnection('ec2-52-16-246-76.eu-west-1.compute.amazonaws.com',8080)
print (conn)
conn.request("GET", "https://ec2-52-16-246-76.eu-west-1.compute.amazonaws.com:8080/address-api-0.6.10.11-SNAPSHOT/uprn?uprn=100050557412")
r1 = conn.getresponse()
response = r1.read()
print (str(response))
