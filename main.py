from moviepy.editor import *

clip = VideoFileClip("curb.mp4").subclip(0,20)

clip = clip.volumex(0.8)

txt_clip = TextClip("Curb Song",fontsize=70,color='white')

# Say that you want it to appear 10s at the center of the screen
txt_clip = txt_clip.set_pos('center').set_duration(10)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([clip, txt_clip])

# Write the result to a file (many options available !)
video.write_videofile("curbwithtext.webm")

print("d")
