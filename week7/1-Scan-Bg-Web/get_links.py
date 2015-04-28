import urllib
from bs4 import BeautifulSoup
import requests


class Links():
    def get_links(self):
        result_list = []
        url = "http://register.start.bg/"
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page.read())
        universities = soup.find_all('a')
        for href in universities:
            if "link.php" in str(href.get("href")):
                result_list.append(href.get("href"))
        return result_list

    def make_request(self, links):
        for item in links:
            try:
                r = requests.get('http://register.start.bg/' + item, timeout = 4)
                self.to_file("servers.txt", r.headers['server'])
                print (r.headers['server'])
            except:
                pass

    def to_file(self, filename, info):
        # file = open(filename, "a")
        # file.write(info)
        with open(filename, "a+") as myfile:
            myfile.write(info + '\n')


a = Links()


if __name__ == "__main__":
    # a.get_links()
    # a.make_request(a.get_links())

