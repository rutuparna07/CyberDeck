import ipinfo

access_token = '5c9fce2810212e'
handler = ipinfo.getHandler(access_token)
ip_address = '115.96.77.222'
details = handler.getDetails(ip_address)
print(details.ip)
print(details.org)
print(details.loc)
print(details.city)
print(details.region)
print(details.country_name)
