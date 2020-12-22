# <p align="center"><b>YouTube Videos URL Grabber With Python</b></p>
It makes a text file with the URL addresses of the videos of a given playlist or channel, in case you need them!

It works by opening a browser instance, scrolling down to catch everything and searches the HTML file for the video URLs. Then it closes the instance.

Feel free to change the code to get other information from an HTML file!

I created this some time ago, using pieces of code, mainly from StackOverflow, of which the original creators I can't find to include here...

# <p align="center"><b>Dependencies</b></p>
!!! This code works only with the Chromium browser !!!

• selenium (Python library)

• chromedriver (Executable)

You can download the chromedriver executable for your Chromium version from here: https://chromedriver.chromium.org/downloads

# <p align="center"><b>Setup</b></p>
Make a directory, in which you will put the python script and the chromedriver.exe (on Windows).

The text files will be saved in the same directory.
