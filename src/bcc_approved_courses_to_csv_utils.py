

import re
import requests 
from bs4 import BeautifulSoup

from sms.testing_utils import testing_utlils as tu





def get_thing(soup):
    
    def get_course_category_l(soup):
        course_category_l = []
        
        h3_attr_l = soup.find_all('h2')
        
        for h3_attr in h3_attr_l: 
            course_category_l.append(h3_attr.get_text())
                                     
        return course_category_l
        
        
    
    def get_area_of_inquiry_td_attr_ll(td_attr_l):
        area_of_inquiry_td_attr_ll = []
        
        for td_attr_num, td_attr in enumerate(td_attr_l):
            print( 1 + td_attr_num % 3)
            if 1 + td_attr_num % 3 == 1:
                area_of_inquiry_td_attr_ll.append([])
                
            area_of_inquiry_td_attr_ll[-1].append(td_attr.get_text())
            
#         print('qqqqqqqqqqq', area_of_inquiry_td_attr_ll)
        
        return area_of_inquiry_td_attr_ll
        
        
#     def get_course_cat_area_of_inquiry_tlll(course_category_l, area_of_inquiry_td_attr_ll):
#         course_cat_area_of_inquiry_ld = []
#         
#         print(len(course_category_l), len(area_of_inquiry_td_attr_ll)) 
#         print(course_category_l) 
#         print(area_of_inquiry_td_attr_ll) 
        
        

    def format_class_l(course_cat_area_of_inquiry_tlll):     
        
        for course_cat_area_of_inquiry_tll in course_cat_area_of_inquiry_tlll:
            for course_cat_area_of_inquiry_t in course_cat_area_of_inquiry_tll[1]:
                tu.p_print(course_cat_area_of_inquiry_t)
                print('^^^^^^^^^^^^^^^^^^^^^')
                
                raw_class_l_str = course_cat_area_of_inquiry_t[2]
                print(raw_class_l_str)
                
                # format raw_clas_l_str into VVV
                formatted_class_l = []
                
                # remove \u00a0 on bold
                cleaned_class_l_str = raw_class_l_str.replace('\u00a0', '')
                
                s_1 = re.split('; , ', cleaned_class_l_str)


        
        
    page_data = {}
    
    course_category_l = get_course_category_l(soup)
    
    
    table_attr_l = soup.find_all('table', class_ = 'table table-hover')
    
    # build course_cat_area_of_inwuiry_tll:
    
#    [
#         [
#             "Communication",
#             [
#                 [
#                     "Writing 1",
#                     "W1",
#                     "ENG 101; CIV 111/112**"
#                 ],
#                 [
#                     "Writing 2",
#                     "W2",
#                     "ENG 300, 301, 302, 304, 305, 306"
#                 ],
#                 [
#                     "Oral Communication",
#                     "OC",
#                     "COM 103"
#                 ]
#             ]
#         ],
#         [
#             "Fine Arts",
#             [
#                 [
#                     "",
#                     "FA",
#                     "ART 107, 109, 131; CIV 113/114**; MUS 109; PHL 350; THE 131, 141; WLF 351; WLG 352; WLT 151, 152"
#                 ]
#             ]
#         ],
#
#         ...
#         
#         [
#             "Writing Intensive",
#             [
#                 [
#                     "",
#                     "EL",
#                     "ART 317, 406, 310, 421; ATG 430, 461; BUS 301, 400; CHM 283, 299, 499; CIS 59, 475, 491; COM 360, 414, 480; CS 390, 490, 491; ECE 200, 402; ECO 498, 499; EGT 210, 310, 410; EHS 301; ENC 305; ENG 302; ETE  227, 228, 301, 302, 303, 304, 305, 306, 307, 308, 313, 491, 493, 496, 497, 498, 499; FCS 311, 375, 475; H S 230, 300; IME 200; IMT 200; I M 440, 441, 459, 460, 461; I S 495, 498; LAS 301; M E 410, 411, 498, 499; MTH 495; NUR 207, 307, 309, 315, 317, 403, 409, 411, 413, 417; PLS PLS 480, 485; PLW 300; PSY 295, 341, 342, 495; WGS 300, 400; WLF 301; WLS 306, 307"
#                 ]
#             ]
#         ]
#     ]

    course_cat_area_of_inquiry_tlll = []
    for table_attr in table_attr_l:
        
        
        td_attr_l = table_attr.find_all('td')
        print(td_attr_l)
        
        # build area_of_inquiry_td_attr_l
        # each 3 elm is a new area of inquiry
        area_of_inquiry_td_attr_ll = get_area_of_inquiry_td_attr_ll(td_attr_l)
            
        print('qqqqqqqqqqq', area_of_inquiry_td_attr_ll)
            
        course_cat_area_of_inquiry_tlll.append((course_category_l.pop(0), area_of_inquiry_td_attr_ll))
        
#         course_cat_area_of_inquiry_tlll = get_course_cat_area_of_inquiry_tlll(course_category_l, area_of_inquiry_td_attr_ll)
#         
#         print('course_cat_area_of_inquiry_tlll: VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
#         tu.p_print(course_cat_area_of_inquiry_tlll)
#         print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        
    print('course_cat_area_of_inquiry_tlll: VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
    tu.p_print(course_cat_area_of_inquiry_tlll)
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        
    course_cat_area_of_inquiry_tlll_w_formatted_class_l = format_class_l(course_cat_area_of_inquiry_tlll)
#         
# #         for td_attr in td_attr_l:
# #             td_attr_text = td_attr.get_text()
# #         print('\n', td_attr_text)
# 
#         course_group_d = {}
#         
#         if td_attr_l[0] != None:
#             course_group_d['area_of_inquiry'] =  td_attr_l[0].get_text()
#     
# 
#         print('--------------' , len(td_attr_l))
#         tu.p_print(course_group_d)



if __name__ == '__main__':
    import main
    main.main()