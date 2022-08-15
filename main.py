from moviepy.editor import *
import moviepy

def convert_bpm_to_seconds(bpm):
    return 60.0/bpm

input = 6
tempo = 120
audio = AudioFileClip(("120bpmtempo.wav"))
finalclips = []

for i in range(1, input+1, 1):
    temp = VideoFileClip(str(str(i) + ".jpg"))
    pos = convert_bpm_to_seconds(tempo)
    temp = temp.set_duration(pos)
    temp = temp.set_start((i-1)*pos)
    finalclips.append(temp)

dexter = CompositeVideoClip(finalclips)
dexter = dexter.set_audio(audio)
dexter.write_videofile("final.webm", fps=24)
