from moviepy.editor import *
import moviepy


speed = {"two beats": 2, "beat": 1, "half beat": 0.5, "quarter beat": 0.25}

#convert bpm to seconds
def convert_bpm_to_seconds(bpm, divsion = "beat"):
    return 60.0/(bpm/speed[divsion])

#initial vars
input = 11
tempo = 105
seconds = convert_bpm_to_seconds(tempo, "quarter beat")
start_time = 9.35
end_time = start_time + input * convert_bpm_to_seconds(tempo)
audio = AudioFileClip(("105_mind_right.mp3"))
audio = audio.subclip(start_time, end_time)
final_clips = []


#prepare the clips for video
for i in range(1, input+1, 1):
    temp = VideoFileClip(str("photos/" + str(i) + ".jpg"))
    pos = seconds
    temp = temp.set_duration(pos)
    temp = temp.set_start((i-1)*pos)
    final_clips.append(temp)

#combine clips and export
final = CompositeVideoClip(final_clips)
final = final.set_audio(audio)
final.write_videofile("quar.webm", fps=24)
