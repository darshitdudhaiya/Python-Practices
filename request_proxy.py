# import requests
#
# proxies = {
#     "http": "http://10.10.1.10:3128",
#     "https": "https://10.10.1.10:1080",
# }
#
# r = requests.get("https://api.ipify.org?format=json",proxies=proxies)
# print(r.json())

import requests

http_proxy = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy = "ftp://10.10.1.10:3128"

proxies = {
    "http": http_proxy,
    "https": https_proxy,
    "ftp": ftp_proxy
}

try:
    r = requests.get("https://api64.ipify.org?format=json", proxies=proxies)
    print(r)

except requests.exceptions.ConnectionError:
    r = {"msg": "Cant'found"}
    print(r)

