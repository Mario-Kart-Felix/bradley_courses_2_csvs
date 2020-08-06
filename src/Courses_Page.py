import requests 
from bs4 import BeautifulSoup



class Courses_Page:
    def __init__(self, url):
        self.page = requests.get(url)
        
        self.raw_html_str = self.page.text
        self.title = self.get_title()
#         print(self.title)
        
        
        
    def get_title(self):
#         return self.raw_html_str.split('<title>')[1].split('</title>')[0]

        soup = BeautifulSoup(self.page.content, 'html.parser')
#         print(soup.prettify())
#         results = soup.find(id='title')
#         results = soup.t
        raw_title = soup.find('title').get_text()
#         print(raw_title)
#         job_elems = soup.find_all('section', class_='title')
#         job_elems = soup.find_all('title')
        return raw_title.split(' | ')[0]
        
#         job_elems = results.find_all('section', class_='card-content')
    
    
    def print_me(self):
        print(self.title)


if __name__ == '__main__':
    import main
    main.main()