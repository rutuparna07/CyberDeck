import ipinfo

access_token = '<IPINFO_TOKEN>'
handler = ipinfo.getHandler(access_token)
ip_address = '<Enter Public IP>'
details = handler.getDetails(ip_address)
print(details.ip)
print(details.org)
print(details.loc)
print(details.city)
print(details.region)
print(details.country_name)
