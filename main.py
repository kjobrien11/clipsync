from moviepy.editor import *
import moviepy

def createSample():
    clip = VideoFileClip("curb.mp4").subclip(0,20)

    clip = clip.volumex(0.8)

    txt_clip = TextClip("Curb Song",fontsize=70,color='white')

    # Say that you want it to appear 10s at the center of the screen
    txt_clip = txt_clip.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])

    # Write the result to a file (many options available !)
    video.write_videofile("curbwithtext.webm")

def convertBPMToSeconds(bpm):
    return 60.0/bpm


audio = AudioFileClip(("120bpmtempo.wav"))
img = ImageClip("1.jpg", duration = convertBPMToSeconds(15))
img2 = ImageClip("1.jpg", duration = convertBPMToSeconds(15))

#tester = VideoFileClip("1.jpg", duration = convertBPMToSeconds(15))
tester = VideoFileClip("1.jpg")
tester2 = VideoFileClip("1.jpg")

clips = [tester, tester2]

tester.write_videofile("tester111.mp4", fps=24)

print(convertBPMToSeconds(111))
