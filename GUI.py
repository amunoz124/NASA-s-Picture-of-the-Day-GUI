import tkinter
import requests
import json
from PIL import Image
import webbrowser
import config

root = tkinter.Tk()
root.title('NASA\'s POD')
root.config(bg='DodgerBlue2')


nasa_api = requests.get(config.api_key)
api = json.loads(nasa_api.content)
label1 = tkinter.Label(root, text=api['title'], font=('Harlow Solid Italic', 50))
label1.config(bg='DodgerBlue2')  
label1.pack()   

label2 = tkinter.Label(root, text='Date: ' + api['date'], font=('Arial', 16))
label2.config(bg='DodgerBlue2')
label2.pack()

label5 = tkinter.Text(root, font=('Arial'),width=75, height=10)
label5.config(state="normal",)
label5.insert(tkinter.INSERT,api['explanation'])
label5.config(state="disabled")
label5.config(bg='DodgerBlue4',fg='old lace')
label5.pack()

try:
    image_url = api['hdurl']
    req_image = requests.get(image_url, stream=True).raw
    image = Image.open(req_image)
    image = image.resize((600,380), Image.ANTIALIAS)
    image.save('image_url.png')
    photo = tkinter.PhotoImage(file='image_url.png')

    label3 = tkinter.Label(root, image=photo)
    label3.pack()
except Exception as e:
    url = api ['url']
    label4 = tkinter.Label(root, text=url, font=('Arial', 18))
    label4.config(bg='DodgerBlue4', fg='old lace')
    label4.pack()
    butt = tkinter.Button(root,text='Redirect to website.', command=lambda:webbrowser.open(url, new=1))
    butt.pack()

root.mainloop()
