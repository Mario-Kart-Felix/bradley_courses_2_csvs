import os
import requests 
from bs4 import BeautifulSoup

import Courses_Page 
import bcc_approved_courses_to_csv_utils

from sms.testing_utils import testing_utlils as tu
from sms.logger        import txt_logger
from sms.logger        import logger
from sms.logger        import json_logger 
   
   
   
URL_TXT_FILE_PATH = 'URLs.txt'
COURSES_PAGE_TITLE_COURSES_DL_D_JSON_PATH = 'courses_page_title_courses_dl_d.json'   
OUTPUTS_DIR_PATH = '..//outputs'
COURSES_PAGES_CSVS_DIR_PATH = OUTPUTS_DIR_PATH + '//courses_page_CSVs'
COURSES_PAGES_CSVS_HEADER_L = ['num', 'name', 'hours', 'gen_ed', 'core_curr', 'prereqs', 'descrip']
COURSES_PAGES_CSVS_HEADER_RENAME_D = {
                                       'num'         : 'Num.',
                                       'name'        : 'Course Name',
                                       'hours'       : 'Hours',
                                       'gen_ed'      : 'Gen. Ed.',
                                       'core_curr'   : 'Core. Curr.',
                                       'prereqs'     : 'Prerequisites',
                                       'descrip'     : 'Description' 
                                     }
BCC_APPROVED_COURSES_URL = 'https://www.bradley.edu/sites/bcc/approved-courses/'

   
   
def get_url_l():   
    raw_lines = txt_logger.read(URL_TXT_FILE_PATH)
    
    url_l = []
    
    for line in raw_lines:
        if line != "":
            url_l.append(line)
    return url_l

    
    
def print_courses_page_l(courses_page_l):
    for cp in courses_page_l:
        cp.print_me()
   
   
def get_courses_page_title_courses_dl_d(url_l):
    courses_page_title_courses_dl_d = {}

    
    for url in url_l:
        
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        
        cp = Courses_Page.Courses_Page(soup)
        courses_page_title_courses_dl_d[cp.title] = cp.course_dl
        
    return courses_page_title_courses_dl_d


def log_courses_pages_csvs(courses_page_title_courses_dl_d):    
    for title, courses_dl in courses_page_title_courses_dl_d.items():
        csv_path = COURSES_PAGES_CSVS_DIR_PATH + '//{}.csv'.format(title)
        print('logging to ', csv_path)#``````````````````````````````````````````````````````````````````
        logger.write2CSV(courses_dl, csv_path, headerList = COURSES_PAGES_CSVS_HEADER_L, headerReplaceDict = COURSES_PAGES_CSVS_HEADER_RENAME_D)


##########################
# BCC Approved Courses
##########################

   
def get_class_num_class_data_d(courses_page_title_courses_dl_d):
    class_num_class_data_dd = {}
   
    for course_page_title, courses_dl in courses_page_title_courses_dl_d.items():
        for courses_d in courses_dl:
            class_num_class_data_dd[courses_d['num']] = courses_d
            del class_num_class_data_dd[courses_d['num']]['num']
            
    return class_num_class_data_dd
   
   
   
   
def main():
    
    url_l = get_url_l()
    tu.p_print(url_l) #```````````````````````````````````````````````````
    
    # get courses_page_title_courses_dl_d
    # will only do all the requests again if you delete the json file
    courses_page_title_courses_dl_d = {}
    if not os.path.isfile(COURSES_PAGE_TITLE_COURSES_DL_D_JSON_PATH):
        courses_page_title_courses_dl_d = get_courses_page_title_courses_dl_d(url_l)
#         tu.p_print(courses_page_title_courses_dl_d)#````````````````````````````````````````````````````````````
        
        json_logger.write(courses_page_title_courses_dl_d, COURSES_PAGE_TITLE_COURSES_DL_D_JSON_PATH)
    else:
        courses_page_title_courses_dl_d = json_logger.read(COURSES_PAGE_TITLE_COURSES_DL_D_JSON_PATH)
    
#     tu.p_print(courses_page_title_courses_dl_d)#````````````````````````````````````````````````````````````

    # write a csv for each course area
    log_courses_pages_csvs(courses_page_title_courses_dl_d)
    
    ##########################
    # BCC Approved Courses
    ##########################
    
    soup = BeautifulSoup(requests.get(BCC_APPROVED_COURSES_URL).content, 'html.parser')
    approved_bcc_course_page_data = bcc_approved_courses_to_csv_utils.get_approved_bcc_course_page_data(soup)
    
    tu.tp_print(approved_bcc_course_page_data, 'approved_bcc_course_page_data:')
    
    tu.tp_print(courses_page_title_courses_dl_d, 'courses_page_title_courses_dl_d:')
        
    class_num_class_data_dd = get_class_num_class_data_d(courses_page_title_courses_dl_d)
    
    tu.p_print(class_num_class_data_dd)

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
