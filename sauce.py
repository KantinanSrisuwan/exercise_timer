import tkinter as tk
from tkinter import ttk
from playsound import playsound

def start_countdown():
    countdown_time = int(entry.get())
    countdown_brake = int(entry2.get())
    nun_cycles = int(entry3.get())
    countdown_label.config(text="")
    
    for n in range (nun_cycles):
        round_cout = ttk.Label(frame, text=f"เหลืออีก: {nun_cycles-n} รอบ",font=("Helvetica", 24))
        round_cout.grid(row=5, column=0,columnspan=2)

        for i in range(countdown_time, -1, -1):
            countdown_label.config(text=f"เวลาที่เหลือ: {i} วินาที",foreground="red")
            root.update()
            root.after(1000)

        playsound("pip.mp3")
        

        for a in range(countdown_brake, -1,-1):
            countdown_label.config(text=f"เวลาพัก: {a} วินาที",foreground="blue")
            root.update()
            root.after(1000)
        
        playsound("pip.mp3")
        root.after(500) #ตั้งไว้เพื่อให้มีดีเลนิดนึงที่เปลียนเวลาพัก
        

    countdown_label.config(text="หมดเวลาแล้ว!",foreground="green")

root = tk.Tk()
root.title("โปรแกรมนับถอยหลัง")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

countdown_label = ttk.Label(frame, text="", font=("Helvetica", 24))
countdown_label.grid(row=0, column=0, columnspan=2)

ttk.Label(frame, text="จำนวนวินาที:").grid(row=1, column=0)
entry = ttk.Entry(frame)
entry.grid(row=1, column=1)

ttk.Label(frame, text="จำนวนวินาทีพัก:").grid(row=2, column=0)
entry2 = ttk.Entry(frame)
entry2.grid(row=2, column=1)

ttk.Label(frame, text="จำนวนรอบ:").grid(row=3, column=0)
entry3 = ttk.Entry(frame)
entry3.grid(row=3, column=1)

start_button = ttk.Button(frame, text="เริ่มนับถอยหลัง", command=start_countdown)
start_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
