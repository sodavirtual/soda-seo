from urllib.parse import urlparse, parse_qsl


def convert_url(url):
    url = 'http://example.com' + url
    parsed_url = urlparse(url)
    path = parsed_url.path
    parsed_qs = parse_qsl(parsed_url.query)

    if parsed_qs:

        final_query = ''
        first = True

        for key in parsed_qs:
            if first:
                first = False
                final_query += '%s={{ %s }}' % (key[0], key[0])
            else:
                final_query += '&%s={{ %s }}' % (key[0], key[0])

        return path + '?' + final_query

    return path
