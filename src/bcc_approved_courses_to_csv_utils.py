


import requests 
from bs4 import BeautifulSoup

from sms.testing_utils import testing_utlils as tu


def get_thing(soup):
    page_data = {}
    
#     print(soup.prettify())

#     h3_attr_l = soup.find_all('h2', class_='h3')
#     h3_attr_l = soup.find_all('h2 class="h3"')
    h3_attr_l = soup.find_all('h2')
#     print(tu.p_print(h3_attr_l))
    print((h3_attr_l))
        
    




if __name__ == '__main__':
    import main
    main.main()