'''
Write a function that when given a URL as a string, 
parses out just the domain name and returns it as a string. 
For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
'''
def domain_name(url):
    if url.find('://') != -1: 
        url = url[url.find('://') + 3:] # delete http / https

    if url.find('/') != -1: 
        url = url[:url.find('/')] # delete url tail

    if url.find('www.') != -1: 
        url = url[4:] # delete www   

    return url[:url.find('.')]

print(domain_name("www.xakep.ru")), #123