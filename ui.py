import tkinter as tk
from threading import Thread
from engine import listen, process

class AssistantUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Assistant Pro")
        self.root.geometry("600x700")
        self.root.configure(bg="#0f1115")

        # HEADER
        tk.Label(root, text="AI ASSISTANT",
                 font=("Segoe UI", 22, "bold"),
                 fg="#00d4ff", bg="#0f1115").pack(pady=10)

        # STATUS
        self.status = tk.Label(root, text="Status: Idle",
                               fg="white", bg="#0f1115")
        self.status.pack()

        # CHAT LOG
        self.chat = tk.Text(root, height=25, width=65,
                            bg="#161a22", fg="#00ff99",
                            font=("Consolas", 10))
        self.chat.pack(pady=20)

        # BUTTONS
        tk.Button(root, text="🎤 Speak",
                  bg="#00d4ff", fg="black",
                  font=("Segoe UI", 12, "bold"),
                  command=self.start).pack(pady=5)

        tk.Button(root, text="Exit",
                  bg="#ff3b3b", fg="white",
                  command=root.quit).pack()

    def log(self, text):
        self.chat.insert(tk.END, text + "\n")
        self.chat.see(tk.END)

    def start(self):
        Thread(target=self.run, daemon=True).start()

    def run(self):
        try:
            self.status.config(text="Listening...")
            command = listen()

            if not command:
                self.status.config(text="Idle")
                return

            self.log("You: " + command)
            self.status.config(text="Processing...")

            process(command, self.log)

            self.status.config(text="Idle")

        except Exception as e:
            self.log("Error: " + str(e))
            self.status.config(text="Error")