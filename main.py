from moviepy.editor import *
import PySimpleGUI as sg
import moviepy
import os

speed = {"Two Beats": 2, "Beat": 1, "Half Beat": 0.5, "Quarter Beat": 0.25}

layout = [
      [sg.Text('Welcome')],
      [sg.Text('Time Division:', size=(20, 1)), sg.Combo(['Two Beats', 'Beat', "Half Beat", "Quarter Beat"])],
      [sg.Text('BPM:', size=(20, 1)), sg.InputText()],
      [sg.Text('Song Start Time (sec):', size=(20, 1)), sg.InputText()],
      [sg.Text('Picture Folder', size=(20, 1)), sg.InputText(key="picture_path"), sg.FolderBrowse()],
      [sg.Text('File of Instrumental', size=(20, 1)), sg.InputText(key="instrumental_file"), sg.FileBrowse()],
      [sg.Submit(), sg.Cancel()]]

window = sg.Window('PictureSync', layout)

event, values = window.read()
window.close()

#convert bpm to seconds
def convert_bpm_to_seconds(bpm, divsion = "Beat"):
    return 60.0/(bpm/speed[divsion])

#provided by user
division = values[0]
tempo = float(values[1]) #bpm of the beat provided by user
start_time = float(values[2]) #where in the song they want the pictures to start
path = os.listdir(values["picture_path"])
audio = AudioFileClip(values["instrumental_file"]) #mp3 or wav file of the song

#computed based on input
seconds = convert_bpm_to_seconds(tempo, division) #conversion of bpm to seconds for display use
end_time = start_time + len(path) * seconds #when to end the video to ensure no excess
audio = audio.subclip(start_time, end_time) #sets the correct start & end times for the beat
final_clips = [] #stores indivual VideoFileClip to be used to combine at the end

path.sort()
#prepare the clips for video
for i in range(1, len(path), 1):
    if path[i].startswith('.'):
        i = i-1
    else:
        temp = VideoFileClip(values["picture_path"] + "/" + str(path[i]))
        pos = seconds
        temp = temp.set_duration(pos)
        temp = temp.set_start((i-1)*pos)
        final_clips.append(temp)

#combine clips and export
final = CompositeVideoClip(final_clips)
final = final.set_audio(audio)
final.write_videofile("results/yourvideo.webm", fps=24)
