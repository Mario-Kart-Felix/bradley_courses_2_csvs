import requests 
from bs4 import BeautifulSoup

# from 



class Courses_Page:
    def __init__(self, url):
        self.soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        
#         self.raw_html_str = self.page.text
        self.title = self.get_title()
        self.course_dl = self.build_course_dl()
        
        print(self.course_dl)
        
        
        
    def get_title(self):
        raw_title = self.soup.find('title').get_text()
        return raw_title.split(' | ')[0]
        
    
    def print_me(self):
        print(self.title)
        
        
    def build_course_dl(self):
        course_dl = []

        p_attr_l = self.soup.find_all('p')
        
        for p_attr in p_attr_l:
            
            
            em_attr = p_attr.find('em')
            
            # if this then its a real course
            if em_attr != None and ' hours)' in str(em_attr):
                course_d = {'hours'     : None,
                            'num'       : None,
                            'name'      : None,
                            'gen_ed'    : None,
                            'core_curr' : None,
                            'descrip'   : None,
                            'prereqs'   : None}
                
                # hours
                course_d['hours'] = em_attr.get_text().split('(')[1].split(' hours)')[0]
                
                # strong
                
                # name / num
                real_course_name_str = p_attr.find('strong', string = lambda text: ' - ' in text.lower()).get_text()
                split_name_str_l = real_course_name_str.split(' - ')
                
                # in case of something like:  ATG 157 - Accounting Principles - Financial
                if len(split_name_str_l) > 2:
                    course_d['num'] = split_name_str_l[0]
                    
                    name_only_delim = course_d['num'] + ' - '
                    course_d['name'] = real_course_name_str.split(name_only_delim)[1]
                else:                    
                    course_d['num'], course_d['name'] = real_course_name_str.split(' - ')

                # Gen. Ed.
                gen_ed_attr = p_attr.find('strong', string = lambda text: 'Gen. Ed. ' in text)
                
                if gen_ed_attr != None:
                    course_d['gen_ed'] = gen_ed_attr.get_text().split('Gen. Ed. ')[1]
                    
                # Core Curr.
                core_curr_attr = p_attr.find('strong', string = lambda text: 'Core Curr. ' in text)
                
                if core_curr_attr != None:
                    course_d['core_curr'] = core_curr_attr.get_text().split('Core Curr. ')[1]
                    
                # descrip / prereqs
#                 course_d['description'] = p_attr.get_text().split('\n')[-1]#[-1]#.split('<p>')[0]
                real_descrip_str = p_attr.get_text().split('\n')[-1]#[-1]#.split('<p>')[0]
                
                if ' Prerequisite: ' in real_descrip_str:
                    course_d['descrip'], course_d['prereqs'] = real_descrip_str.split(' Prerequisite: ')
                else:
                    course_d['descrip'] = real_descrip_str
                    
                print('------------------------------\n', course_d)
                    
                course_dl.append(course_d)
                
            
        return course_dl
        
#         print(p_l)


if __name__ == '__main__':
    import main
    main.main()