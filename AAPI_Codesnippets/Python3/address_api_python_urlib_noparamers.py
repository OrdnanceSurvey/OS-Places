import urllib
opener = urllib.FancyURLopener({})
url = 'https://api.ordnancesurvey.co.uk/places/v1/addresses/postcode?postcode=so16%206hw&dataset=DPA,LPI&key=6e0WvXJsEzPd1G1pqkRMlGgODvsEg50G'
f = opener.open(url)
response=f.read()
print ( response )
