import tkinter as tk
import requests
from PIL import Image, ImageTk
import webbrowser
import config

class NasasPODApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NASA's POD")
        self.root.config(bg='DodgerBlue2')
        self.api_key = config.api_key
        self.load_data()

    def load_data(self):
        try:
            nasa_api = requests.get(self.api_key)
            api = nasa_api.json()
            
            self.display_title(api['title'])
            self.display_date(api['date'])
            self.display_explanation(api['explanation'])

            image_url = api['hdurl']
            self.resize_and_save_image(image_url, 'resized_image.png', (600, 380))
            self.display_image('resized_image.png')
        except Exception as e:
            url = api.get('url', '')
            self.display_error(url)

    def display_title(self, title):
        label1 = tk.Label(self.root, text=title, font=('Harlow Solid Italic', 50), bg='DodgerBlue2')
        label1.pack()

    def display_date(self, date):
        label2 = tk.Label(self.root, text='Date: ' + date, font=('Arial', 16), bg='DodgerBlue2')
        label2.pack()

    def display_explanation(self, explanation):
        label5 = tk.Text(self.root, font=('Arial'), width=75, height=10, state="normal")
        label5.insert(tk.END, explanation)
        label5.config(state="disabled", bg='DodgerBlue4', fg='old lace')
        label5.pack()

    def resize_and_save_image(self, image_url, save_path, size):
        req_image = requests.get(image_url, stream=True).raw
        image = Image.open(req_image)
        image.thumbnail(size)
        image.save(save_path)

    def display_image(self, image_path):
        photo = ImageTk.PhotoImage(file=image_path)
        label3 = tk.Label(self.root, image=photo)
        label3.image = photo
        label3.pack()

    def display_error(self, url):
        label4 = tk.Label(self.root, text='Failed to fetch data', font=('Arial', 18), bg='DodgerBlue4', fg='old lace')
        label4.pack()
        if url:
            butt = tk.Button(self.root, text='Redirect to website', command=lambda: webbrowser.open(url, new=1))
            butt.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = NasasPODApp(root)
    root.mainloop()
