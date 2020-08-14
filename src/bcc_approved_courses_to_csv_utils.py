

import re
import requests 
from bs4 import BeautifulSoup

from sms.testing_utils import testing_utlils as tu


#     [
#         [
#             "Communication",
#             [
#                 [
#                     "Writing 1",
#                     "W1",
#                     [
#                         [
#                             "ENG 101",
#                             ""
#                         ],
#                         [
#                             "CIV 111",
#                             "**"
#                         ],
#                         [
#                             "CIV 112",
#                             "**"
#                         ]
#                     ]
#                 ],
#                 [
#                     "Writing 2",
#                     "W2",
#                     [
#                         [
#                             "ENG 300",
#                             ""
#                         ],
#                         [
#                             "ENG 301",
#                             ""
#                         ],
#                         [
#                             "ENG 302",
#                             ""
#                         ],
#                         [
#                             "ENG 304",
#                             ""
#                         ],
#                         [
#                             "ENG 305",
#                             ""
#                         ],
#                         [
#                             "ENG 306",
#                             ""
#                         ]
#                     ]
#                 ],
#                 [
#                     "Oral Communication",
#                     "OC",
#                     [
#                         [
#                             "COM 103",
#                             ""
#                         ]
#                     ]
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
#                     [
#                         [
#                             "ART 317",
#                             ""
#                         ],
#
#                         ...
#
#                         [
#                             "WLS 306",
#                             ""
#                         ],
#                         [
#                             "WLS 307",
#                             ""
#                         ]
#                     ]
#                 ]
#             ]
#         ]
#     ]



def get_approved_bcc_course_page_data(soup):
    
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
#                 print(raw_class_l_str)

                
                # remove \u00a0 on bold
                cleaned_class_l_str = raw_class_l_str.replace('\u00a0', ' ').replace(';', ',').replace('.', ',')
                
#                 s_1 = re.split('; , ', cleaned_class_l_str)

                s_1 = cleaned_class_l_str.split(',')
                print('s_1: ', s_1)
               
                # trim whitespace
                whitespace_trimmed_class_l = []
                
                for elm in s_1:
                    whitespace_trimmed_class_l.append(elm.strip().lstrip())
                
#                 print('whitespace_trimmed_class_l: ', whitespace_trimmed_class_l)
                
                # give all class nums their dept. code
                dept_code_class_l = []
                cur_dept_code = None # assumes 1st will always have a dept code
                
                for class_num in whitespace_trimmed_class_l:
                    
                    class_num = class_num.replace('PLS PLS', 'PLS') # fix typo
                    
                    # if string contains any letters
                    if re.search('[a-zA-Z]', class_num):
                        cur_dept_code = ''.join([i for i in class_num if not i.isdigit()]).strip().lstrip() # removes all non-digit chars and trims whitespace
                        
                        dept_code_class_num = class_num.replace('  ', ' ')
                        
                        dept_code_class_l.append(dept_code_class_num) # also removes double spaces
                            
                        print(class_num)
                    else:
                        # for fixing typos like "RLS 320 321"
                        s_1 = class_num.split(' ')
                         
                        for class_num in s_1:
                            if elm != '':
                                
                        
                                dept_code_class_l.append( cur_dept_code + ' ' + class_num ) 
                        
                # format *'s
                formatted_class_l = []
                
                for class_num in dept_code_class_l:
                    
                    class_num = class_num.replace('P T HS', 'HS')
                    
                    # first exceptions
                    if class_num == '400/M L 452****':
                        formatted_class_l.append(('BUS 400', '****'))
                        formatted_class_l.append(('M L 452', '****'))
                        
                    elif class_num == 'RLS 321 WLS 334':
                        formatted_class_l.append(('RLS 321', ''))
                        formatted_class_l.append(('WLS 334', ''))                    
                    
                    elif '*' in class_num:
#                         print('reeeeeeeeeeeeeeeeeee')
                        

                            
                        
                        # for stuff like:  "CHM 110/111***"
#                         else:
                        s_1 = class_num.split('/')
                        second_num_str = s_1[1][0:3]
                        astericies_str = s_1[1][3:]
                        first_class_num = s_1[0]
                        
                        dept_code = ''.join([i for i in first_class_num if not i.isdigit()]).strip().lstrip() # removes all non-digit chars and trims whitespace

                        second_class_num = dept_code + ' ' + second_num_str
                        
                        formatted_class_l.append((first_class_num, astericies_str))
                        formatted_class_l.append((second_class_num, astericies_str))
                        print('.')
                    
                    else:
                        formatted_class_l.append((class_num, ''))

                
                # set formatted class list
                course_cat_area_of_inquiry_t[2] = formatted_class_l
                
        return course_cat_area_of_inquiry_tlll
                
                
        
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
            
#         print('qqqqqqqqqqq', area_of_inquiry_td_attr_ll)
            
        course_cat_area_of_inquiry_tlll.append((course_category_l.pop(0), area_of_inquiry_td_attr_ll))
        
#         course_cat_area_of_inquiry_tlll = get_course_cat_area_of_inquiry_tlll(course_category_l, area_of_inquiry_td_attr_ll)
#         
#         print('course_cat_area_of_inquiry_tlll: VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
#         tu.p_print(course_cat_area_of_inquiry_tlll)
#         print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        
#     print('course_cat_area_of_inquiry_tlll: VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
#     tu.p_print(course_cat_area_of_inquiry_tlll)
#     print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        
    course_cat_area_of_inquiry_tlll_w_formatted_class_l = format_class_l(course_cat_area_of_inquiry_tlll)
    
#     tu.tp_print(course_cat_area_of_inquiry_tlll_w_formatted_class_l, 'course_cat_area_of_inquiry_tlll_w_formatted_class_l: ')
    
    
    return course_cat_area_of_inquiry_tlll_w_formatted_class_l




if __name__ == '__main__':
    import main
    main.main()