import requests

import Courses_Page 

from sms.testing_utils import testing_utlils as tu
from sms.logger        import txt_logger
from sms.logger        import logger
from sms.logger        import json_logger 
   
   
   
URL_TXT_FILE_PATH = 'URLs.txt'
COURSES_PAGE_TITLE_COURSES_DL_D_JSON_PATH = 'courses_page_title_courses_dl_d.json'   
   
   
def get_url_l():   
    raw_lines = txt_logger.read(URL_TXT_FILE_PATH)
    
    url_l = []
    
    for line in raw_lines:
        if line != "":
            url_l.append(line)
    return url_l


# def get_course_page_l(url_l):
#     courses_page_l = []
#     
#     for url in url_l:
#         courses_page_l.append(Courses_Page.Courses_Page(url))
#         
#     return courses_page_l
    
    
def print_courses_page_l(courses_page_l):
    for cp in courses_page_l:
        cp.print_me()
   
   
def get_courses_page_title_courses_dl_d(url_l):
#     def get_course_page_l(url_l):
#     courses_page_l = []
    courses_page_title_courses_dl_d = {}

    
    for url in url_l:
        cp = Courses_Page.Courses_Page(url)
        courses_page_title_courses_dl_d[cp.title] = cp.course_dl
        
    return courses_page_title_courses_dl_d


#     courses_page_l = get_course_page_l(url_l)
#     print_courses_page_l(courses_page_l) #```````````````````````````````````
# 
# 
#     courses_page_title_courses_dl_d = {}
#     
#     for courses_page in courses_page_l:
#         courses_page_title_courses_dl_d[courses_page.title] = courses_page.
    
   
   
def main():
    
    url_l = get_url_l()
    tu.p_print(url_l) #```````````````````````````````````````````````````
    
#     courses_page_l = get_course_page_l(url_l)
#     print_courses_page_l(courses_page_l) #```````````````````````````````````
    
    courses_page_title_courses_dl_d = get_courses_page_title_courses_dl_d(url_l)
    tu.p_print(courses_page_title_courses_dl_d)#```````````````````````````````
    
    


# # Making a get request 
# response = requests.get('https://www.bradley.edu/academic/undergradcat/20202021/las-mthcourses.dot') 
# # response = requests.get('https://www.bradley.edu/academic/undergradcat/20202021/turner-entrepreneur-courses.dot') 
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


if __name__ == '__main__':
    main()    
