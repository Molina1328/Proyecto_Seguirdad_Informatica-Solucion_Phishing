from urllib.parse import urlparse, parse_qsl, unquote_plus
import asyncio
import logging
import socket
import sys

#IP:google desde dns    142.250.78.174 
#IP:google pishing      192.168.188.132

urlMalisiosa = 'https://142.250.78.174/' 
TARGETS = [ 
    ('google.com', 'https'),
]

def compare_urls(urlMalisiosa, urlB):

    url1_parsed = urlparse(urlMalisiosa.rstrip("/"))
    url2_parsed = urlparse(urlB.rstrip("/")) 
    comparisons = ["scheme", "hostname", "path"]

    for attr in comparisons:
        if getattr(url1_parsed, attr) != getattr(url2_parsed, attr):
            return False

    ports = [url1_parsed.port, url2_parsed.port]
    comparisons = [url1_parsed, url2_parsed]
    for index, url in enumerate(comparisons):
        if url.port is None and url.scheme == "http":
            ports[index] = 80 
        elif url.port is None and url.scheme == "https":
            ports[index] = 443 
    print(ports[index])
    return True

urlB='ninguno'
cadena='ninguno'
async def main(loop, targets):    
    for target in targets:
        info = await loop.getaddrinfo(
            *target,
            proto=socket.IPPROTO_TCP,
        )

        for host in info:
            urlB='{:20}: {}'.format(target[0], host[4][0])
            cadena = urlB[22:] 
    aux = 'https://'+cadena+'/'
    print(compare_urls(urlMalisiosa, aux))
    print (urlMalisiosa)
    print (aux)
event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, TARGETS))
finally:
    

    event_loop.close() 

 



 
