import requests 
   
# Making a get request 
# response = requests.get('https://www.bradley.edu/academic/undergradcat/20202021/cfa-artcourses.dot') 
response = requests.get('https://www.bradley.edu/academic/undergradcat/20202021/las-soccourses.dot') 
    
# prinitng request text 
print(type(response.text)) 
print(response.text) 

 
# from bs4 import BeautifulSoup
#  
# URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
# page = requests.get(URL)
#  
# soup = BeautifulSoup(page.content, 'html.parser')
# 
# div class="row-color-bWhite row-padding-below-breadcrumbs"
