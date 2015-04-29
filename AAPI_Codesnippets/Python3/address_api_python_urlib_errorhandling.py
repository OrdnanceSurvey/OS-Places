import urllib

url = 'https://api.ordnancesurvey.co.uk/places/v1/addresses/bbox?bbox=437367.0,437318.0,115766.0,115426.1&dataset=DPA,LPI&key=6e0WvXJsEzPd1G1pqkRMlGgODvsEg50G'
try:
    f = urllib.urlopen(url)
except Exception as e:
    print(str(e))
response=f.read()
print (response)

