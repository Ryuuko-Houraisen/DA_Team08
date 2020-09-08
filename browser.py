# Use the Request library
import requests

# Set the target webpage
url = "http://172.18.58.238/creative/"
r = requests.get(url)
# This will get the full page
print(r.text)

# This will get the status code
print("Status code:")
print("\t *", r.status_code)

# This will modify the headers user-agent
headers = {
    "User-Agent" : "Mobile"
}
# Test it on an external site
url2 = "http://172.18.58.238/creative/"
rh = requests.get(url2, headers=headers)

# This will just get just the headers
h = requests.head(url)
print(rh.text, headers)
print("**")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**")
