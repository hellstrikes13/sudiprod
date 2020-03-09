from  selenium import webdriver
import sys
import argparse
import commands
'''
for this script you have to do: 
 apt-get install phantomjs,
 sudo pip install selinum
'''
print '''
this script will take screenshot of webpage 
you can find the image under DIR: /home/sudeep/screenshot
'''
w,h = commands.getoutput("xrandr | grep \* | awk '{print $1}'").split('x')
w = int(w)
h = int(h)
if len(sys.argv) < 2:
    print "ENTIRE URL missing..!!! e.g: http://google.com"
    sys.exit(0)
url = sys.argv[1]
driver = webdriver.PhantomJS()
url_name = url.split('.')[1]
driver.set_window_size(w, h) # set the window size that you need 
driver.get(url)
driver.save_screenshot('/home/sudeep/screenshot/'+url_name+'.png')
