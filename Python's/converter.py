try:
    import tkinter as tk
    import sys
    import clipboard
    import webbrowser as wb
    from tkinter import ttk
    from tkinter import messagebox as msg
    from tkinter.filedialog import askopenfilename as open
    from tkinter.filedialog import asksaveasfilename as save
    import ffmpeg
    import subprocess
    import os
    import threading as th
except ModuleNotFoundError:
    x = ModuleNotFoundError("Libraries not found !", "'ffmpeg', 'tkinter', 'clipboard' python libraries are required to run the program . Check if they are installed using 'pip install (library_name)' in your terminal to avoid errors.")
    raise x
    sys.exit(1)

link = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z"
ffmpegpath = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"
if not os.path.exists(ffmpegpath):
    root = tk.Tk()
    root.withdraw()
    m = msg.askyesno("ffmpeg not exists !", f"ffmpeg is not installed or not found !\nthis program requires it to run\n\nRedirect to download it now ?")
    if m:
        msg.showinfo("Redirecting. . .", f"After downloading , it will be 7z file.\nExtract all to this directory : {ffmpegpath[:-15]}\nRun the program again after finishing.")
        wb.open(link)
    else:
        msg.showinfo("Canceled !", f"you can download it directly from {link}\nand extract all to this directory : {ffmpegpath[:-15]}")
    sys.exit(1)

con = tk.Tk()
con.title("Video to Audio Converter")
con.resizable(False, False)
con.geometry("560x100")

def openit():
    opfile = open()
    if opfile:
        ae.delete(0, tk.END)
        ae.insert('end', opfile)

def saveit():
    svfile = save(initialfile="output", defaultextension=".mp3",
                  filetypes=[("Audio", "*.mp3")])
    if not svfile:
        return
    pathv = ae.get()
    dirv = os.path.dirname(pathv)
    inputv = os.path.basename(pathv)
    if svfile and os.path.exists(pathv):
        os.chdir(dirv)
        try:
            if os.path.splitext(inputv)[1] == ".mp3" or os.path.splitext(inputv)[1] == ".MP3":
                msg.showinfo("Check", f"This file :{inputv} is already mp3")
                return
            if os.path.exists(svfile):
                os.remove(svfile)
            subprocess.call([ffmpegpath, "-i", inputv, "-vn",
                           "-acodec", "mp3", svfile])
            if os.path.exists(svfile):
                msg.showinfo(
                    "Successfully !", f"The video file : {inputv}\nhas successfully converted to audio here : {svfile}")
            else:
                msg.showerror(
                    "Error !", "Error in converting or invalid video file or error in path, check and try again")
        except subprocess.CalledProcessError:
            msg.showerror(
                "Error !", "Error in converting or invalid video file or error in path, check and try again")
    else:
        msg.showerror("Warning !", "Video file not found, check path")

def savenow():
    th.Thread(target=saveit).start()

cv = tk.Label(con, text="Choose video file to convert it to audio , or input its path",
              foreground="darkred", font=("Segoe UI", 15))
cv.pack()
al = tk.Label(con, text="Video:", foreground="darkred", font=("Segoe UI", 12))
al.place(x=5, y=50)
ae = tk.Entry(con, width=53, font=("Segoe UI", 10), justify="center")
ae.place(x=55, y=55)
ae.bind('<Button-3>', lambda event: ae.insert('end', clipboard.paste()))
ab = tk.Button(con, text="choose...", command=openit)
ab.place(x=433, y=52)
asv = tk.Button(con, text="save as...", command=savenow)
asv.place(x=495, y=52)
ae.focus_force()
con.mainloop()
