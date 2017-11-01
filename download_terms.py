import urllib.request, json
import requests

all_terms = []
with open('terms.txt', 'w') as file:
    with open('links.txt', 'r') as links:
        link = links.readline()
        while link != '':
            r = requests.get(link)
            response = r.json()
            pages = list(response["query"]['pages'].values())
            all_terms += ([i['title'] for i in pages])
            link = links.readline()

    for term in sorted(all_terms):
        file.write(term)
        file.write("\n")