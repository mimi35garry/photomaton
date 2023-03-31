import tkinter as tk
from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)


def preview_cam():
    picam2.start_preview(Preview.QTGL)
    picam2.start()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="QUIT", fg="red", command=quit)
button.pack(side=tk.LEFT)

slogan = tk.Button(frame, text="apercu", command=preview_cam)
slogan.pack(side=tk.LEFT)

root.mainloop()
