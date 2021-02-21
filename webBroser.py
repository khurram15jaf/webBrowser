from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tkinter import *
import time

def search_result():
    service = Service('/usr/lib/chromium-browser/chromedriver')
    service.start()
    driver = webdriver.Remote(service.service_url)
    driver.get('http://www.google.com/');
    time.sleep(10) # Let the user actually see something!
    window.quit()
    result=driver.find_element_by_name('q')
    result.clear()
    result.send_keys(entry1.get())
    result.send_keys(Service.RETURN)


def facebook():
    service = Service('/path/to/chromedriver')
    service.start()
    driver = webdriver.Remote(service.service_url)
    driver.get('http://www.facebook.com/');
    time.sleep(10) # Let the user actually see something!


window=Tk()
window.title("Hello")
window.geometry("450x200")
search=Label(window,text="What are you thinking .....",font='time 15')
search.place (x=10,y=10)
entry1=Entry(window)
entry1.place(x=250,y=0)

b1=Button(window,text="search",command=search_result,width=12,bg='gray')
b1.place(x=150,y=50)

b2=Button(window,text="Facebook",command=facebook,width=12,bg='gray')
b2.place(x=150,y=100)

window.mainloop()

