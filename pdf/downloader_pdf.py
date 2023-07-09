import requests
import os
from bs4 import BeautifulSoup
import urllib


def telechargement(src:str)->None:
    """
    Permet de télécharger le pdf correspondant à une these
    """

    url = 'https://tel.archives-ouvertes.fr/' + src + '/document'
    try :
        r = requests.get(url, stream=True)
        with open(os.path.join("data", "theses", src + '.pdf'), 'wb') as fd:
            for chunk in r.iter_content(2000):
                fd.write(chunk)

    except ConnectionError:
        print("Erreur dans la connection")


def get_summary(name:str)->str:
    """
    Scrap the summary of the theses
    """

    url = os.path.join("https://theses.hal.science", name)
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()

    soup = BeautifulSoup(mystr, 'html.parser')

    domain = soup.find("div", {"class": "domains"}).find("a").get_text()
    summary = soup.find("div", {"class": "abstract-content fr active"})
    if summary is None:
        summary = soup.find("div", {"class": "abstract-content active"})

    if not domain is None and not summary is None:
        path = os.path.join("data", "summary", domain)
        if not os.path.exists(path):
            os.makedirs(path)

        with open(os.path.join(path, name + ".txt"), 'w') as f:
            f.write(summary.get_text().lstrip())

        return domain, summary.get_text().lstrip()
    
    return None
    
