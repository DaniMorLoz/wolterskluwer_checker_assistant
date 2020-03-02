from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import tkinter as tk


#-------------------------------------#

user = ''
passwd = ''

#-------------------------------------#

def infoSuccess():
    tk.messagebox.showinfo("Success","Successful check-in.")

def error(info):
    return tk.messagebox.askretrycancel("Error during the check-in","Info: {0}".format(info))

def exit(root):
    root.destroy()

def center(toplevel):
    toplevel.update_idletasks()
    screen_width = toplevel.winfo_screenwidth()
    screen_height = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2
    toplevel.geometry("+%d+%d" % (x, y))

def clock():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://a3gt.wolterskluwer.es/gt#/clockings/16457")
    usertext = driver.find_element_by_xpath('//*[@id="username"]')
    passtext = driver.find_element_by_xpath('//*[@id="pwd"]')
    usertext.send_keys(user)
    passtext.send_keys(passwd)
    btn = driver.find_element_by_xpath('//*[@id="sendClocking"]')
    btn.click()
    try:
        errormsg=driver.find_element_by_xpath('//*[@id="purr-container"]/div/div[1]/p')
        error(errormsg.text)
    except:
        infoSuccess()
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False,False)
    tk.Frame(heigh="250",width="450").place()
    label = tk.Label(text="Do you want to check-in/out now?")
    label.grid(pady=(10,20),padx=20,row=0,columnspan=2)
    button_cancel = tk.Button(text="No",command=lambda:exit(root))
    button_cancel.grid(column=0,row=1,pady=(0,20))
    button_accept = tk.Button(text="Yes",command=lambda:clock())
    button_accept.grid(column=1,row=1,pady=(0,20))
    center(root)
    root.mainloop()