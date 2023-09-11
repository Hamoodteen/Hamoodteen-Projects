try:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox as msg
    from pytube import YouTube , Playlist
    from pytube.cli import on_progress
    from tkinter.filedialog import asksaveasfilename as save
    from tqdm import tqdm
    import os
    import clipboard
    import subprocess
    import threading
    import requests
except ModuleNotFoundError:
    x = ModuleNotFoundError("Libraries not found !", "'pytube', 'tqdm', 'requests', 'clipboard', 'tkinter', 'subprocess' python libraries are required to run the program . Check if they are installed using 'pip install (library_name)' in your terminal to avoid errors.")
    raise x
    sys.exit(1)

def check_url(yt):
    try:
        if "playlist?list=" in yt:
            msg.showwarning("Sorry !", "This tool doesn't support downloading playlists.")
            return
        else:
            yt = YouTube(yt)
            vn['text'] = f"Name: {yt.title}"
            return yt
    except:
        msg.showerror("Error in link", "Invalid URL. Check and try again.")
        return

def filtering():
    yt = ve.get()
    check = check_url(yt)
    if check == None:
        return
    available_extensions = set()
    for stream in check.streams:
        mime_type = stream.mime_type
        if mime_type:
            file_extension = mime_type.split('/')[-1]
            available_extensions.add(file_extension)
    vc1nf1['values'] = ()
    vc1nf1['values'] = tuple(available_extensions)
    vc1nf1.current(0)
    vc1nf2['values'] = ()
    vc1nf2['values'] = tuple(available_extensions)
    vc1nf2.current(0)
    vc1nf3['values'] = ()
    vc1nf3['values'] = tuple(available_extensions)
    vc1nf3.current(0)

    available_resolutions = set()
    for stream in check.streams:
        resolution = stream.resolution
        if resolution:
            available_resolutions.add(resolution)
    vc2nf1['values'] = ()
    vc2nf1['values'] = tuple(available_resolutions)
    vc2nf1.current(0)
    vc2nf2['values'] = ()
    vc2nf2['values'] = tuple(available_resolutions)
    vc2nf2.current(0)

def proggd1():
    yt = ve.get()
    check = check_url(yt)
    if check == None:
        return
    ask = msg.askyesno("Confirm", f"Name: {check.title}\n\nExtension: {vc1nf1.get()}\n\nResolution: {vc2nf1.get()}")
    if not ask:
        return
    svfile = save(initialfile="output", defaultextension=f".{vc1nf1.get()}", filetypes=[("Video", f"*.{vc1nf1.get()}")])
    if not svfile:
        return
    fileout = check.streams.filter(file_extension=vc1nf1.get(), res=vc2nf1.get()).first()
    if fileout is not None:
        d = tk.Toplevel(ytd)
        d.title("Downloading . . .")
        d.resizable(False, False)
        downloadprogress = 0.0
        response = requests.get(fileout.url, stream=True)
        totalsize = int(response.headers.get("content-length", 0))
        with open(svfile, "wb") as f, tqdm(
            desc=svfile,
            total=totalsize,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(chunk_size=1024):
                f.write(data)
                downloadprogress += len(data)
                bar.update(len(data))
        fileout.download(os.path.dirname(svfile), os.path.basename(svfile))
        downprog = (downloadprogress / totalsize) * 100
        
    else:
        msg.showerror("Error", "No matching stream found.")

def proggd2():
    if check_url(ve.get()) == None:
        return
    ask = msg.askyesno("Confirm", f"Name: {ve.get()} (video only)\n\nExtension: {vc1nf2.get()}\n\nResolution: {vc2nf2.get()}")
    if not ask:
        return
    d = tk.Toplevel(ytd)
    d.title("Downloading . . .")
    d.resizable(False, False)
    p = ttk.Progressbar(d, length=300, value=0)
    p.pack()

def proggd3():
    if check_url(ve.get()) == None:
        return
    ask = msg.askyesno("Confirm", f"Name: {ve.get()} (audio only)\n\nExtension: {vc1nf3.get()}")
    if not ask:
        return
    d = tk.Toplevel(ytd)
    d.title("Downloading . . .")
    d.resizable(False, False)
    p = ttk.Progressbar(d, length=300, value=0)
    p.pack()

ytd = tk.Tk()
ytd.title("Youtube Downloader !")
ytd.resizable(False, False)
ytd.geometry("490x300")
cv = tk.Label(ytd, text="Input video URL (Press submit first)",
              foreground="darkred", font=("Segoe UI", 18))
cv.pack()
vl = tk.Label(ytd, text="Vid URL:", foreground="darkred", font=("Segoe UI", 12))
vl.place(x=5, y=50)
ve = tk.Entry(ytd, width=50, font=("Segoe UI", 10), justify="center")
ve.place(x=70, y=55)
ve.bind('<Button-3>', lambda event: ve.insert('end', clipboard.paste()))
vb = tk.Button(ytd, text="submit", command=filtering)
vb.place(x=430, y=52)
vn = tk.Label(ytd, text=f"Name: ", foreground="blue", font=("Segoe UI", 10), wraplength=465)
vn.place(x=10, y=85)
vs = tk.Label(ytd, text="---------------------------------------------------------------------------------------------")
vs.place(x=10, y=120)
vf = tk.Label(ytd, text="filters:", font=("Segoe UI", 18))
vf.place(x=5, y=150)
ytdb = ttk.Notebook(ytd)
ytdb.place(x=100, y=150)
vnf1 = tk.Frame(ytdb, width=310, height=115)
vnf1.pack(fill='both', expand=True)
ytdb.add(vnf1, text="original ")
vnf2 = tk.Frame(ytdb, width=310, height=115)
vnf2.pack(fill='both', expand=True)
ytdb.add(vnf2, text="video only ")
vnf3 = tk.Frame(ytdb, width=310, height=115)
vnf3.pack(fill='both', expand=True)
ytdb.add(vnf3, text="audio only ")

vt1nf1 = tk.Label(vnf1, text="extension:", font=("Segoe UI", 12))
vt1nf1.place(x=5, y=5)
vc1nf1 = ttk.Combobox(vnf1, state="readonly", width=5, font=50, values=(""))
vc1nf1.place(x=8, y=40)
vt2nf1 = tk.Label(vnf1, text="resolution:", font=("Segoe UI", 12))
vt2nf1.place(x=105, y=5)
vc2nf1 = ttk.Combobox(vnf1, state="readonly", width=5, font=50, values=(""))
vc2nf1.place(x=110, y=40)
vdf1 = tk.Button(vnf1, text="Download Now !", foreground="blue", font=("Segoe UI", 10), command=proggd1)
vdf1.place(x=100, y=80)

vt1nf2 = tk.Label(vnf2, text="extension:", font=("Segoe UI", 12))
vt1nf2.place(x=5, y=5)
vc1nf2 = ttk.Combobox(vnf2, state="readonly", width=5, font=50, values=(""))
vc1nf2.place(x=8, y=40)
vt2nf2 = tk.Label(vnf2, text="resolution:", font=("Segoe UI", 12))
vt2nf2.place(x=105, y=5)
vc2nf2 = ttk.Combobox(vnf2, state="readonly", width=5, font=50, values=(""))
vc2nf2.place(x=110, y=40)
vdf2 = tk.Button(vnf2, text="Download Now !", foreground="blue", font=("Segoe UI", 10), command=proggd2)
vdf2.place(x=100, y=80)

vt1nf3 = tk.Label(vnf3, text="extension:", font=("Segoe UI", 12))
vt1nf3.place(x=5, y=5)
vc1nf3 = ttk.Combobox(vnf3, state="readonly", width=5, font=50, values=(""))
vc1nf3.place(x=8, y=40)
vdf3 = tk.Button(vnf3, text="Download Now !", foreground="blue", font=("Segoe UI", 10), command=proggd3)
vdf3.place(x=100, y=80)

ve.focus_force()
ytd.mainloop()
