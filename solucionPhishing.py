from urllib.parse import urlparse, parse_qsl, unquote_plus



def compare_urls(url1, url2):

    url1_parsed = urlparse(url1.rstrip("/"))
    url2_parsed = urlparse(url2.rstrip("/"))
    print(url1_parsed)
    print(url2_parsed)
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

url1 = 'https://www.google.com/'
url2 = 'https://www.google.com/'


print(compare_urls(url1, url2))
