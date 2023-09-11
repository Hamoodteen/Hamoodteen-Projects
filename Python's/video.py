from pytube import YouTube

# Create a YouTube object and insert video URL
yt = YouTube('https://youtu.be/RUBQ-DG8Vro?si=BVpdCXYomM4jFZ4n')

# Print the video name
print("Video name:", yt.title)

print("------------------------------------")

# Initialize a set to store unique file extensions
available_extensions = set()

# Iterate through all streams and collect MIME types
for stream in yt.streams:
	mime_type = stream.mime_type
	if mime_type:
		file_extension = mime_type.split('/')[-1]
		available_extensions.add(file_extension)

# Print the available file extensions
print("Available file extensions:", available_extensions)

print("------------------------------------")

# Initialize set and dictionary to store available resolutions and file sizes for each
available_resolutions = set()
resolution_file_sizes = {}

# Iterate through all streams, collect available resolutions, and file sizes
for stream in yt.streams:
    resolution = stream.resolution
    if resolution:
        available_resolutions.add(resolution)
        file_size = stream.filesize
        if file_size is not None:
            # Convert file size to MB for readability
            file_size_mb = round(file_size / (1024 * 1024), 2)
            resolution_file_sizes[resolution] = file_size_mb

# Print available resolutions and file sizes for each
print("Available resolutions:", available_resolutions)
for resolution, size in resolution_file_sizes.items():
    print(f"Resolution: {resolution}, File size: {size} MB")

print("------------------------------------")

# Initialize set and dictionary to store available ABRs and file sizes for each
available_abrs = set()
audio_abrs = {}

# Iterate through all streams, collect available ABRs, and file sizes
for stream in yt.streams.filter(only_audio=True):
    abr = stream.abr
    if abr:
        available_abrs.add(abr)
        file_size = stream.filesize
        if file_size is not None:
            # Convert file size to MB for readability
            file_size_mb = round(file_size / (1024 * 1024), 2)
            audio_abrs[abr] = file_size_mb

# Print available ABRs and file sizes for audio streams
print("Available ABRs:", available_abrs)
for abr, size in audio_abrs.items():
    print(f"Audio ABR: {abr}, File size: {size} MB")
