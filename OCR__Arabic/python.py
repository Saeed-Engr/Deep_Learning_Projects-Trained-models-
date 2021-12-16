import tkinter
from tkinter import *
from tkinter import ttk  # is used for combobox
from tkinter import messagebox
import os
from tkinter import filedialog
from ArabicOcr import arabicocr
from tkinter import messagebox
from time import sleep


class OCR:
    def __init__(self, root):
        self.root = root
        self.root.geometry("665x600")

        self.root.title("OCR of Arabic and English")
        self.root.configure(bg='Light Blue')
        self.image_path = ""
        self.folder_path = ""

        self.root.minsize(665, 600)
        self.root.maxsize(665, 600)
        self.root.resizable(0, 0)

        # Input FIle Label
        self.add_img = Label(root, text='Add Image:')
        self.add_img.grid(column=0, row=0, padx=10, pady=10, sticky='w')

        self.path_var = StringVar()
        # Input FIle Entry
        self.imgbox = Entry(root, width=30, state='readonly', textvariable=self.path_var)
        self.imgbox.grid(column=1, row=0, padx=10, pady=10, sticky='w')

        # Input FIle Button
        self.browse = Button(root, text='Browse', command=self.loadimage)
        self.browse.grid(column=2, row=0, padx=10, pady=10, sticky='w')

        # Output Folder Label
        self.output = Label(root, text='Output Folder:')
        self.output.grid(column=0, row=1, padx=10, pady=10, sticky='w')

        # Output Folder Entry
        self.out_var = StringVar()
        self.textbox2 = Entry(root, state='readonly', width=30, textvariable=self.out_var)
        self.textbox2.grid(column=1, row=1, padx=10, pady=10, sticky='w')

        # Output Folder Button
        self.btn = Button(root, text='Browse', command=self.choose_directory)
        self.btn.grid(column=2, row=1, padx=10, pady=10, sticky='w')

        # Output Result Label
        self.showinfo = Label(root, text='Result will show below in Text Area Pleas Wait', bg='Light Blue')
        self.showinfo.grid(column=2, row=2, padx=10, pady=10, sticky='w')

        # Output Result Label
        self.output = Label(root, text='Result Area')
        self.output.grid(column=0, row=2, padx=10, pady=10, sticky='w')

        # Output Result Text Area
        self.textarea = Text(root)
        # textarea.place(x=10, y=10, width=400, height=300)
        self.textarea.grid(column=0, row=3, padx=10, pady=10, columnspan=400, rowspan=300)

        # Start Button
        self.startbtn = Button(root, text='Start', command=self.arabicOcr)
        self.startbtn.grid(column=0, row=303, padx=10, pady=10, sticky='w')

        # Exit Button
        self.exit_button = Button(root, text="Exit", state='disabled', command=self.exitw)
        self.exit_button.grid(column=1, row=303, sticky='w')

    # Get text from Arabic Image Function
    def arabicOcr(self):
        global image_path, folder_path
        if self.image_path == "":
            messagebox.showerror('Select Image File', 'Please Add the Image')
        elif self.folder_path == "":
            messagebox.showerror('Select Folder Path', 'Please Select Output Folder')
        else:
            out_image = 'out.jpg'
            results = arabicocr.arabic_ocr(self.image_path, out_image)
            for r in results:
                self.textarea.insert(tkinter.END, r)
            words = []
            for i in range(len(results)):
                word = results[i][1]
                words.append(word)
            with open(os.path.join(self.folder_path, 'file.txt'), 'w', encoding='utf-8') as myfile:
                myfile.write(str(words))
            self.showinfo.config(text="")
            messagebox.showinfo('Done', 'Your Task Completed Successfully')
            self.exit_button.config(state='normal')

    # Load Image File Function
    def loadimage(self):
        global image_path
        loadimg = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image file',
                                             filetypes=(("JPEG File", "*.jpeg"),("PNG File", "*.png"),("JPG File", "*.jpg")))
        self.path_var.set(loadimg)
        if self.image_path == "":
            self.image_path = loadimg

    # Choose Output Folder Function
    def choose_directory(self):
        global folder_path
        path_work = filedialog.askdirectory(title='Select Output Folder')
        if path_work == '':
            print('Pleae Enter Your Folder Directory :')
            sleep(2)
            return self.choose_directory()
        else:
            self.out_var.set(path_work)
            self.folder_path = path_work

    def exitw(self):
        msg = messagebox.askquestion('Exit', 'Do you want to Exit?')
        if msg == 'yes':
            root.destroy()

        else:
            pass


if __name__ == "__main__":
    root = Tk()
    ob = OCR(root)
    root.mainloop()
