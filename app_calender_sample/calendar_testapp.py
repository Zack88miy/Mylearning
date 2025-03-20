import tkinter as tk
from tkinter import messagebox
import os
import calendar
from datetime import datetime

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar & Notes App")
        self.root.geometry("600x500")
        
        self.selected_date = tk.StringVar()
        self.selected_date.set(datetime.today().strftime('%Y-%m-%d'))
        
        self.calendar_frame = tk.Frame(root)
        self.calendar_frame.pack(pady=10)
        
        self.year_var = tk.IntVar(value=datetime.today().year)
        self.month_var = tk.IntVar(value=datetime.today().month)
        
        self.year_entry = tk.Entry(self.calendar_frame, textvariable=self.year_var, width=5)
        self.year_entry.pack(side=tk.LEFT)
        self.month_entry = tk.Entry(self.calendar_frame, textvariable=self.month_var, width=3)
        self.month_entry.pack(side=tk.LEFT)
        
        #更新用のボタン
        self.update_button = tk.Button(self.calendar_frame, text="Update", command=self.show_calendar)
        self.update_button.pack(side=tk.LEFT)
        
        # カレンダーを表示するtextウィジェット
        self.calendar_text = tk.Text(root, height=7, width=40)
        self.calendar_text.pack()
        self.show_calendar()
        
        self.date_label = tk.Label(root, text="Select Date (YYYY-MM-DD):")
        self.date_label.pack()
        self.date_entry = tk.Entry(root, textvariable=self.selected_date)
        self.date_entry.pack()
        
        self.text_area = tk.Text(root, wrap="word", height=10)
        self.text_area.pack(expand=1, fill="both")
        
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        
        # メモのメニューの機能を用意
        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Save Note", command=self.save_note)
        file_menu.add_command(label="Load Note", command=self.load_note)
        file_menu.add_command(label="Delete Note", command=self.delete_note)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        
        self.menu.add_cascade(label="File", menu=file_menu)

    def show_calendar(self):
        try:
            year = self.year_var.get()
            month = self.month_var.get()
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12")
            
            self.calendar_text.delete(1.0, tk.END)
            cal = calendar.month(year, month)
            self.calendar_text.insert(tk.END, cal)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
    
    def validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    
    def save_note(self):
        date = self.selected_date.get()
        if not self.validate_date(date):
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
            return
        
        file_path = f"notes_{date}.txt"
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Success", f"Note for {date} saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save note: {str(e)}")
    
    def load_note(self):
        date = self.selected_date.get()
        if not self.validate_date(date):
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
            return
        
        file_path = f"notes_{date}.txt"
        try:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, content)
            else:
                messagebox.showinfo("Info", "No note found for this date.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load note: {str(e)}")
    
    def delete_note(self):
        date = self.selected_date.get()
        if not self.validate_date(date):
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
            return
        
        file_path = f"notes_{date}.txt"
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                messagebox.showinfo("Success", "Note deleted successfully!")
            else:
                messagebox.showinfo("Info", "No note found for this date.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete note: {str(e)}")

if __name__ == "__main__":
    #ウィンドウの作成
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
