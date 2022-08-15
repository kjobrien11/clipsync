from moviepy.editor import *
import moviepy

def convert_bpm_to_seconds(bpm):
    return 60.0/bpm


input = 11
tempo = 128
start_time = 0
end_time = input * convert_bpm_to_seconds(tempo)
audio = AudioFileClip(("128_new_choppa.mp3"))
audio = audio.subclip(start_time, end_time)
final_clips = []

for i in range(1, input+1, 1):
    temp = VideoFileClip(str(str(i) + ".jpg"))
    pos = convert_bpm_to_seconds(tempo)
    temp = temp.set_duration(pos)
    temp = temp.set_start((i-1)*pos)
    final_clips.append(temp)

final = CompositeVideoClip(final_clips)
final = final.set_audio(audio)
final.write_videofile("final.webm", fps=24)
