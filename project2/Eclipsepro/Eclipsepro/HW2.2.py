import tkinter as tk
from tkinter import font, filedialog, messagebox
from PIL import Image, ImageTk
import docx
import keyboard
import pygame


def change_font():
    selected_font = font.Font(family=font_family.get(), size=font_size.get(), weight=font_weight.get(), slant=font_slant.get())
    text_editor.config(font=selected_font)

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("Word files", "*.doc")])
    if file_path:
        if file_path.endswith(".txt"):
            with open(file_path, "w") as f:
                text = text_editor.get("1.0", "end-1c")
                f.write(text)
        elif file_path.endswith(".doc"):
            doc = docx.Document()
            text = text_editor.get("1.0", "end-1c")
            doc.add_paragraph(text)
            doc.save(file_path)
        messagebox.showinfo("تم الحفظ", "تم حفظ الملف بنجاح!")

# إنشاء نافذة البرنامج
root = tk.Tk()
root.title("محرر نصوص وعرض الصور")

# إنشاء المكونات
text_editor = tk.Text(root, font=("Arial", 12))
font_family_label = tk.Label(root, text="الخط:")
font_family = tk.StringVar()
font_family.set("Arial")
font_family_dropdown = tk.OptionMenu(root, font_family, "Arial", "Times New Roman", "Courier New")
font_size_label = tk.Label(root, text="الحجم:")
font_size = tk.IntVar()
font_size.set(12)
font_size_entry = tk.Entry(root, textvariable=font_size)
font_weight_label = tk.Label(root, text="الوزن:")
font_weight = tk.StringVar()
font_weight.set("normal")
font_weight_dropdown = tk.OptionMenu(root, font_weight, "normal", "bold")
font_slant_label = tk.Label(root, text="الميل:")
font_slant = tk.StringVar()
font_slant.set("roman")
font_slant_dropdown = tk.OptionMenu(root, font_slant, "roman", "italic")
apply_button = tk.Button(root, text="تطبيق", command=change_font)
open_image_button = tk.Button(root, text="فتح صورة", command=open_image)
save_button = tk.Button(root, text="حفظ الملف", command=save_file)
image_label = tk.Label(root)

# ترتيب المكونات على النافذة
text_editor.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
font_family_label.grid(row=1, column=0, padx=10, pady=5)
font_family_dropdown.grid(row=1, column=1, padx=10, pady=5)
font_size_label.grid(row=1, column=2, padx=10, pady=5)
font_size_entry.grid(row=1, column=3, padx=10, pady=5)
font_weight_label.grid(row=1, column=4, padx=10, pady=5)
font_weight_dropdown.grid(row=1, column=5, padx=10, pady=5)
font_slant_label.grid(row=1, column=6, padx=10, pady=5)
font_slant_dropdown.grid(row=1, column=7, padx=10, pady=5)
apply_button.grid(row=1, column=8, padx=10, pady=5)
open_image_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
save_button.grid(row=2, column=2, columnspan=2, padx=10, pady=5)
image_label.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

# إضافة ميزة تغيير اللغة باستخدام الزر F1
def change_language():
    keyboard.send("shift+Alt")

# إضافة مفتاح لتغيير اللغة باستخدام الزر F1
keyboard.add_hotkey("F1", change_language)

# تشغيل النافذة
root.mainloop()
