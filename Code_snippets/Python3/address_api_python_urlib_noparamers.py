import urllib
opener = urllib.FancyURLopener({})
url = 'https://api.ordnancesurvey.co.uk/places/v1/addresses/postcode?postcode=so16%206hw&dataset=DPA,LPI&key=INSERT_YOUR_API_KEY_HERE'
f = opener.open(url)
response=f.read()
print ( response )
