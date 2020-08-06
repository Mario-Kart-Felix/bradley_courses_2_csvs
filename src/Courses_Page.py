import requests 
from bs4 import BeautifulSoup



class Courses_Page:
    def __init__(self, url):
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        
        self.raw_html_str = self.page.text
        self.title = self.get_title()
        self.class_l = self.build_class_l()
        
        
        
    def get_title(self):
        raw_title = self.soup.find('title').get_text()
        return raw_title.split(' | ')[0]
        
    
    def print_me(self):
        print(self.title)
        
        
    def build_class_l(self):
        course_dl = []

        p_attr_l = self.soup.find_all('p')
        
        for p_attr in p_attr_l:
            
            
            em_attr = p_attr.find('em')
            
            # if this then its a real course
            if em_attr != None and ' hours)' in str(em_attr):
                course_d = {}
                
                # hours
                course_d['hours'] = em_attr.get_text().split('(')[1].split(' hours)')[0]
                
                # strong
                
                # name / num
                real_course_name_str = p_attr.find('strong', string = lambda text: ' - ' in text.lower()).get_text()
                course_d['num'], course_d['name'] = real_course_name_str.split(' - ')
                
                # Gen. Ed. / Core Curr
                strong_dot_attr_l = p_attr.find_all('strong', string = lambda text: '. ' in text.lower())
                
                for strong_dot_attr in strong_dot_attr_l:
                    if 'Gen. Ed. ' in str(strong_dot_attr):
                        course_d['Gen. Ed.'] = strong_dot_attr.get_text().split('Gen. Ed. ')[1]
                

                    
                
            
#             if em_attr.get_
#             print(hours)
            
                print('------------------------------\n', course_d)
            
        return course_dl
        
#         print(p_l)


if __name__ == '__main__':
    import main
    main.main()