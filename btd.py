import tkinter as tk
from tkinter import messagebox
from random import randint

def check_guess():
    guess = int(guess_entry.get())

    if guess == secret_number:
        messagebox.showinfo("ผลลัพธ์", "ทายถูกต้องครับผม")
        window.destroy()
    elif guess < secret_number:
        messagebox.showinfo("ผลลัพธ์", "เลขที่ทายน้อยเกินไป")
    else:
        messagebox.showinfo("ผลลัพธ์", "เลขที่ทายมากเกินไป")

# สร้างหมายเลขลับ
secret_number = randint(1, 100)

# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("ทายเลข")
window.geometry("300x150")

# สร้างเนื้อหาในหน้าต่าง
guess_label = tk.Label(window, text="ทายเลขระหว่าง 1-100:")
guess_label.pack()

guess_entry = tk.Entry(window)
guess_entry.pack()

submit_button = tk.Button(window, text="ตรวจสอบ", command=check_guess)
submit_button.pack()

# เริ่มการทำงานโปรแกรม
window.mainloop()