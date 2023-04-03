import tkinter as tk


class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer")


        self.minutes = tk.StringVar()
        self.seconds = tk.StringVar()
        self.milliseconds = tk.StringVar()


        self.minutes.set("00")
        self.seconds.set("00")
        self.milliseconds.set("00")


        self.label_minutes = tk.Label(master, textvariable=self.minutes, font=("Helvetica", 48))
        self.label_seconds = tk.Label(master, textvariable=self.seconds, font=("Helvetica", 48))
        self.label_milliseconds = tk.Label(master, textvariable=self.milliseconds, font=("Helvetica", 24))

        self.label_minutes.grid(row=0, column=0)
        self.label_seconds.grid(row=0, column=1)
        self.label_milliseconds.grid(row=0, column=2)

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)

        self.start_button.grid(row=1, column=0)
        self.stop_button.grid(row=1, column=1)
        self.reset_button.grid(row=1, column=2)


        self.is_running = False
        self.time_elapsed = 0

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer()

    def stop_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.time_elapsed = 0
        self.update_timer()

    def update_timer(self):
        if self.is_running:
            self.time_elapsed += 10
            self.minutes.set("{:02d}".format((self.time_elapsed // 60000) % 60))
            self.seconds.set("{:02d}".format((self.time_elapsed // 1000) % 60))
            self.milliseconds.set("{:02d}".format((self.time_elapsed // 10) % 100))
            self.master.after(10, self.update_timer)

root = tk.Tk()
app = TimerApp(root)
root.mainloop()