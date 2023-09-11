import pytube
v = pytube.YouTube('https://youtu.be/5BZLz21ZS_Y?si=3f84gUOLQD3DEjp3')
s = v.streams.all()
for ss in s:
	ss.download('D:\c')
