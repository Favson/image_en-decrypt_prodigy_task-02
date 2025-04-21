from tkinter import *
from tkinter import filedialog, messagebox

root = Tk()
root.geometry("200x160")  # fixed the × symbol

def encrypt_image():
    file1 =filedialog.askopenfile(mode='r', filetypes=[('jpg file', '*.jpg'), ('PNG file', '*.png')])
    if file1 is not None:
        # print(file1)
        file_name=file1.name
        # print(file_name)
        key =entry1.get(1.0, END).strip()
        
        if not key.isdigit():
            messagebox.showerror("Invalid Key", "Please enter a valid numeric key.")
            return
        key = int(key)
        
        print(file_name, key)
        fi = open(file_name, 'rb')
        image=fi.read()
        fi.close()
        image=bytearray(image)
        
        for index,values in enumerate(image):
            image[index]=values^int(key)
        messagebox.showinfo("Success", "Successfully Done!")
        fi1 =open(file_name, 'wb')
        fi1.write(image)
        fi1.close()

b1 = Button(root, text="Encrypt/Decrypt", command=encrypt_image)
b1.place(x=70, y=10)


entry1 = Text(root, height=1, width=10)
entry1.place(x=50, y=50)  # fixed the capital X

root.mainloop()
