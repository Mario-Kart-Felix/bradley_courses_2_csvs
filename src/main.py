import requests 

from sms.testing_utils import testing_utlils as tu
from sms.logger        import txt_logger
from sms.logger        import logger
   
   
   
URL_TXT_FILE_PATH = 'URLs.txt'
   
   
   
def get_url_l():   
    raw_lines = txt_logger.read(URL_TXT_FILE_PATH)
    
    url_l = []
    
    for line in raw_lines:
        if line != "":
            url_l.append(line)
    return url_l
   
   
   
if __name__ == '__main__':
    
    url_l = get_url_l()
    tu.p_print(url_l)
    
    
    
    
    
    
    
# Making a get request 
# response = requests.get('https://www.bradley.edu/academic/undergradcat/20202021/cfa-artcourses.dot') 
# response = requests.get('https://www.bradley.edu/academic/undergradcat/20202021/turner-entrepreneur-courses.dot') 
#     
# # prinitng request text 
# print(type(response.text)) 
# print(response.text) 

 
# from bs4 import BeautifulSoup
#  
# URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
# page = requests.get(URL)
#  
# soup = BeautifulSoup(page.content, 'html.parser')
# 
# div class="row-color-bWhite row-padding-below-breadcrumbs"
