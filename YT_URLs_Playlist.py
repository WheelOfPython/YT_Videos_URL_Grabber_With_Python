import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import collections
import os.path

print("Starting...")
print("Opening Window...")
driver = webdriver.Chrome()

# Dictionary with all the URLs of the YT playlists, to access them easier
url_dict = {
    'name_1':'https://www.youtube.com/playlist?list=...',
    'name_2':'https://www.youtube.com/playlist?list=...'
    }

key = 'name_1'
url = url_dict[key]

driver.get(url)

print("Scrolling down...")
ht = driver.execute_script("return document.documentElement.scrollHeight;")
while True:
    prev_ht=driver.execute_script("return document.documentElement.scrollHeight;")
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)
    ht=driver.execute_script("return document.documentElement.scrollHeight;")
    if prev_ht==ht:
        break

print("Finding the urls...") # Seperate the URLs from the HTML file
links = driver.find_elements_by_xpath("//a[@href]")

l=[]
for link in links:
    l.append(link.get_attribute("href"))

rls=[]
for rl in l:
    if rl.startswith("https://www.youtube.com/watch?v="):
        rls.append(rl)
us=[]
for i in rls:
    u = i.split('&')
    us.append(u[0])

URLs = [item for item, count in collections.Counter(us).items() if count > 1]

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
    for url_ in URLs:
        if url_ not in already:
            text_file.write("%s\n" % url_)
            n+=1
    text_file.close()
    print("---------------------------------------------------")
    print("There are %d videos in total" % len(URLs))
    print("There are", n, "new urls added")
    print("---------------------------------------------------")
else:
    print('Creating file:', file_name)
    text_file = open(file_name, "w")
    n=0
    for url_ in URLs:
        if url_ not in already:
            text_file.write("%s\n" % url_)
            n+=1
    text_file.close()
    print("---------------------------------------------------")
    print("There are %d videos in total" % len(URLs))
    print("There are", n, "written")
    print("---------------------------------------------------")


driver.quit()
print("Finished!!!")
