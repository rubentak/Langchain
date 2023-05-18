import urllib.request
import html

# clone website and save

response = urllib.request.urlopen('https://www.python.org')
html = response.read()
print(html)

