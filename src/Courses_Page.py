import requests 


class Courses_Page:
    def __init__(self, url):
        self.response = requests.get(url)
        
        self.raw_html_str = self.response.text
        self.title = self.get_title()
        print(self.title)
        
        
        
    def get_title(self):
        return self.raw_html_str.split('<title>')[1].split('</title>')[0]
    
    
    def print_me(self):
        print(self.title)


if __name__ == '__main__':
    import main
    main.main()