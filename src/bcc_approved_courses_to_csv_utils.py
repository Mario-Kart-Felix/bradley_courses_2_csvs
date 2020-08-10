


import requests 
from bs4 import BeautifulSoup

from sms.testing_utils import testing_utlils as tu





def get_thing(soup):
    
    def get_area_of_inquiry_td_attr_ll(td_attr_l):
        area_of_inquiry_td_attr_ll = []
        
        for td_attr_num, td_attr in enumerate(td_attr_l):
            print( 1 + td_attr_num % 3)
            if 1 + td_attr_num % 3 == 1:
                area_of_inquiry_td_attr_ll.append([])
                
            area_of_inquiry_td_attr_ll[-1].append(td_attr)
            
#         print('qqqqqqqqqqq', area_of_inquiry_td_attr_ll)
        
        return area_of_inquiry_td_attr_ll
        
        
        
        
        
        
    page_data = {}
    
#     print(soup.prettify())

#     h3_attr_l = soup.find_all('h2', class_='h3')
#     h3_attr_l = soup.find_all('h2 class="h3"')
    h3_attr_l = soup.find_all('h2')
#     print(tu.p_print(h3_attr_l))
    print((h3_attr_l))
    print(len(h3_attr_l))
    
    table_attr_l = soup.find_all('table', class_ = 'table table-hover')
    
    for table_attr in table_attr_l:
        
        
        td_attr_l = table_attr.find_all('td')
        print(td_attr_l)
        
        # build area_of_inquiry_td_attr_l
        # each 3 elm is a new area of inquiry
        area_of_inquiry_td_attr_ll = get_area_of_inquiry_td_attr_ll(td_attr_l)
        
#         for td_attr_num, td_attr in enumerate(td_attr_l):
#             print( 1 + td_attr_num % 3)
#             if 1 + td_attr_num % 3 == 1:
#                 area_of_inquiry_td_attr_ll.append([])
#                 
#             area_of_inquiry_td_attr_ll[-1].append(td_attr)
            
        print('qqqqqqqqqqq', area_of_inquiry_td_attr_ll)
            
        
#         for td_attr in td_attr_l:
#             td_attr_text = td_attr.get_text()
#         print('\n', td_attr_text)

        course_group_d = {}
        
        if td_attr_l[0] != None:
            course_group_d['area_of_inquiry'] =  td_attr_l[0].get_text()
    

        print('--------------' , len(td_attr_l))
        tu.p_print(course_group_d)



if __name__ == '__main__':
    import main
    main.main()