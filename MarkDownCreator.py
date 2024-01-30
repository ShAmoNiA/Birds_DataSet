import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from PIL import Image

# Path to the directory containing your videos
video_directory = "./"

# Path to the directory where you want to save the .md file
output_directory = "./md"

# Function to generate thumbnails
def generate_thumbnail(video_path):
    # You might need to adjust the dimensions based on your preference
    thumbnail_size = (1000, 1000)
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    thumbnail_path = os.path.join(output_directory, f"{video_name}_thumbnail.jpg")

    # Open the video file and extract a frame
    try:
        with VideoFileClip(video_path) as video:
            frame = video.get_frame(0)  # Get the first frame
            thumbnail = Image.fromarray(frame)
            thumbnail.thumbnail(thumbnail_size)
            thumbnail.save(thumbnail_path)
        return thumbnail_path
    except Exception as e:
        print(f"Error generating thumbnail for {video_path}: {e}")
        return None

# List all video files in the directory
video_files = [file for file in os.listdir(video_directory) if file.endswith((".mp4", ".avi", ".mkv"))]

# Create or open the .md file for writing
md_file_path = os.path.join(output_directory, "videos.md")
with open(md_file_path, "w") as md_file:
    # Write the header
    md_file.write("# Video Thumbnails\n\n")

    # Generate thumbnails and write information to the .md file
    for video_file in video_files:
        video_path = os.path.join(video_directory, video_file)
        thumbnail_path = generate_thumbnail(video_path)

        if thumbnail_path:
            md_file.write(f"## {video_file}\n")
            md_file.write(f"![{video_file}](./md/{os.path.basename(thumbnail_path)})\n\n")

print(f"Markdown file created at: {md_file_path}")