from moviepy.editor import *
import moviepy
import PySimpleGUI as sg

speed = {"Two Beats": 2, "Beat": 1, "Half Beat": 0.5, "Quarter Beat": 0.25}

layout = [
      [sg.Text('Welcome')],
      [sg.Text('Time Division:', size=(20, 1)), sg.Combo(['Two Beats', 'Beat', "Half Beat", "Quarter Beat"])],
      [sg.Text('BPM:', size=(20, 1)), sg.InputText()],
      [sg.Text('Song Start Time (sec):', size=(20, 1)), sg.InputText()],
      [sg.Text('Picture Folder', size=(20, 1)), sg.InputText(), sg.FolderBrowse()],
      [sg.Text('File of Instrumental', size=(20, 1)), sg.InputText(), sg.FileBrowse()],
      [sg.Submit(), sg.Cancel()]]

window = sg.Window('Rename Files or Folders', layout)

event, values = window.read()
window.close()
folder_path, file_path = values[0], values[1]       # get the data from the values dictionary

#convert bpm to seconds
def convert_bpm_to_seconds(bpm, divsion = "Beat"):
    return 60.0/(bpm/speed[divsion])

#provided by user
input = 11 #how many total pictures
division = values[0]
tempo = float(values[1]) #bpm of the beat provided by user
start_time = float(values[2]) #where in the song they want the pictures to start
audio = AudioFileClip(("105_mind_right.mp3")) #mp3 or wav file of the song

#computed based on input
seconds = convert_bpm_to_seconds(tempo, division) #conversion of bpm to seconds for display use
end_time = start_time + input * seconds #when to end the video to ensure no excess
audio = audio.subclip(start_time, end_time) #sets the correct start & end times for the beat
final_clips = [] #stores indivual VideoFileClip to be used to combine at the end

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
final.write_videofile("final.webm", fps=24)
