import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import subprocess
import os

class WhatsAppBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WAutoBot🤖 - WhatsApp Visual Bot")
        self.root.geometry("500x550")

        # Inputs
        self.contact_name = tk.StringVar()
        self.message_file = tk.StringVar()
        self.schedule_file = tk.StringVar()
        self.search_img = tk.StringVar()
        self.send_img = tk.StringVar()

        tk.Label(root, text="Contact Name:").pack()
        tk.Entry(root, textvariable=self.contact_name).pack(fill="x", padx=10)

        tk.Label(root, text="Messages File (messages.txt):").pack()
        tk.Entry(root, textvariable=self.message_file).pack(fill="x", padx=10)
        tk.Button(root, text="Browse", command=self.browse_messages).pack()

        tk.Label(root, text="Schedule File (schedule.txt):").pack()
        tk.Entry(root, textvariable=self.schedule_file).pack(fill="x", padx=10)
        tk.Button(root, text="Browse", command=self.browse_schedule).pack()

        tk.Label(root, text="Search Box Image:").pack()
        tk.Entry(root, textvariable=self.search_img).pack(fill="x", padx=10)
        tk.Button(root, text="Browse", command=self.browse_search_img).pack()

        tk.Label(root, text="Send Button Image:").pack()
        tk.Entry(root, textvariable=self.send_img).pack(fill="x", padx=10)
        tk.Button(root, text="Browse", command=self.browse_send_img).pack()

        tk.Button(root, text="▶️ START BOT", command=self.start_bot, bg="green", fg="white").pack(pady=10)

        tk.Label(root, text="📋 Bot Logs:").pack()
        self.log_output = scrolledtext.ScrolledText(root, height=15)
        self.log_output.pack(fill="both", padx=10, pady=5)

    def browse_messages(self):
        file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file:
            self.message_file.set(file)

    def browse_schedule(self):
        file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file:
            self.schedule_file.set(file)

    def browse_search_img(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])
        if file:
            self.search_img.set(file)

    def browse_send_img(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])
        if file:
            self.send_img.set(file)

    def start_bot(self):
        # Save inputs to a config file or pass as args
        contact = self.contact_name.get()
        msg_file = self.message_file.get()
        sched_file = self.schedule_file.get()
        search_img = self.search_img.get()
        send_img = self.send_img.get()

        if not (contact and msg_file and sched_file and search_img and send_img):
            messagebox.showerror("Missing Info", "Please fill in all fields.")
            return

        self.log_output.insert(tk.END, "Bot started... Check logs below.
")
        self.log_output.see(tk.END)

        # Run the bot subprocess
        command = [
            "python", "bot.py", 
            "--contact", contact,
            "--messages", msg_file,
            "--schedule", sched_file,
            "--search", search_img,
            "--send", send_img
        ]

        try:
            subprocess.Popen(command)
            self.log_output.insert(tk.END, "Bot launched successfully!
")
        except Exception as e:
            self.log_output.insert(tk.END, f"Error launching bot: {e}
")

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = WhatsAppBotGUI(root)
    root.mainloop()
