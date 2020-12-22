import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import collections
import os

print("Starting...")
print("Opening Window...")
driver = webdriver.Chrome()

# Dictionary with all the URLs of the YT channels, to access them easier
# The URL should be of the form https://www.youtube.com/user/UserName and not .../user/UserName/videos
url_dict = {'name_1':'https://www.youtube.com/user/...', 
            'name_2':'https://www.youtube.com/user/...'
            }

key = 'name_1'
url = url_dict[key]

driver.get(url+"/videos")

print("Scrolling down...")
ht=driver.execute_script("return document.documentElement.scrollHeight;")
while True:
    prev_ht=driver.execute_script("return document.documentElement.scrollHeight;")
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)
    ht=driver.execute_script("return document.documentElement.scrollHeight;")
    if prev_ht==ht:
        break

print("Finding the urls...")
links = driver.find_elements_by_xpath('//*[@id="video-title"]')

print("Writing the urls...")

already = []
file_name = key + "_URLs.txt"

if os.path.isfile(file_name):
    text_file_r = open(file_name, "r")
    for x in text_file_r:
        already.append(x.strip('\n'))
    text_file_r.close()
    
    n=0
    text_file = open(file_name, "a")
    for link in links:
        url = link.get_attribute("href")
        if url not in already:
            text_file.write("%s\n" % url)
            n+=1
    text_file.close()
    
    print("---------------------------------------------------")
    print("There are %d videos in total" % len(links))
    print("There are", n, "new urls")
    print("---------------------------------------------------")
else:
    print('Creating file:', file_name)
    text_file = open(file_name, "w")
    n=0
    for link in links:
        url = link.get_attribute("href")
        if url not in already:
            text_file.write("%s\n" % url)
            n+=1
    text_file.close()
    print("---------------------------------------------------")
    print("There are %d videos in total" % len(links))
    print("There are", n, "written")
    print("---------------------------------------------------")

driver.quit()
print("Finished!!!")
