import customtkinter as ct
import tkinter as tk
import cv2


def extract(video_patch):
    cap = cv2.VideoCapture(video_patch)
    all_frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        small_frame = cv2.resize(gray, (30, 18))
        _, binary_frame = cv2.threshold(small_frame, 127, 255, cv2.THRESH_BINARY)
        frame_matrix = (binary_frame == 255).astype(int).tolist()
        all_frames.append(frame_matrix)

    cap.release()
    return all_frames


video_data = extract("bad.mp4")

app = ct.CTk()
app.geometry("500x300")
app.configure(fg_color="black")
pixel_grid = []

for j in range(18):
    row = []
    for i in range(30):
        lable = tk.Label(app, width=2, height=1, bg="black", borderwidth=0, highlightthickness=0)
        lable.grid(row=j, column=i, padx=0, pady=0)
        row.append(lable)
    pixel_grid.append(row)

current_frame_index = 0


def play_frame():
    global current_frame_index
    if current_frame_index >= len(video_data):
        return

    frame_data = video_data[current_frame_index]

    for y in range(18):
        for x in range(30):
            color = "white" if frame_data[y][x] == 1 else "black"
            pixel_grid[y][x].configure(bg=color)

    current_frame_index += 1
    app.after(33, play_frame)


app.after(0, play_frame)
app.mainloop()