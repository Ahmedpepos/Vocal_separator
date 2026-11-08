import  moviepy as mp
import os
import time
from pathlib import Path

def extract_file_name(file_name: str) -> str:
    name = os.path.basename(file_name)
    name_without_ext, _ = os.path.splitext(name)
    return name_without_ext

def video_track(in_vid: str):

    if "\"" in in_vid:
        in_vid = in_vid.replace("\"","")

    return mp.VideoFileClip(in_vid)

def audio_track():
    in_aud = input("input your audio file path: ")
    if "\"" in in_aud:
        in_aud = in_aud.replace("\"","")

    return mp.AudioFileClip(in_aud)

def duration_formated(timeinsec: float) -> str:
    return time.strftime("%H:%M:%S", time.gmtime(timeinsec))

def add_audio_to_video(video_track, audio_track):

    video_track.audio = audio_track
    video_track.write_videofile("D:\\Personal\\remove_music\\tennis[vocals].mp4")

def split_audio_clips(video_track, chunk_duration_min: int) -> list:
    """
    Splits a video's audio track into smaller clips of a specified duration.
    """
    chunk_duration_sec = chunk_duration_min * 60
    subclips = []
    start = 0
    audio = video_track.audio

    while start < audio.duration:
        end = min(start + chunk_duration_sec, audio.duration)
        
        subclips.append(audio.subclipped(start, end))
        
        start = end
    
    return subclips

def export_audio_clips(video_track: VideoFileClip):

    distination = "D:\\Personal\\remove_music\\splitted_audio"
    subclips = split_audio_clips(video_track)
    
    n = 1
    for subclip in subclips:
        subclip.write_audiofile(f"{distination}\\{extract_file_name(video_track.filename)}{n}.mp3")
        n+=1

        subclip.close()

def combine_audio_clips():

    audio_clips = [mp.AudioFileClip(str(file)) for file in Path("D:\\Personal\\remove_music\\splitted_audio").glob("*mp3")]

    full_audio_clip = mp.concatenate_audioclips(audio_clips)
    full_audio_clip.write_audiofile(f"D:\\Personal\\remove_music\\final_video\\{extract_file_name(audio_clips[0].filename)}_combined.mp3")

    folder_path = "D:\\Personal\\remove_music\\splitted_audio"
    for file in os.listdir(folder_path):
        if file.lower().endswith(".mp3"):
            file_to_delete = os.path.join(folder_path, file)
            os.remove(file_to_delete)

while True:
    print("Starting program...")

    # vid_path = input("input your video file path: ")
    # video = video_track(vid_path)
    # export_audio_clips(video)
    combine_audio_clips()
    # audio_clip.write_audiofile(f"{extract_file_name(vid_path)}_half.mp3")

    condition = input("continue? [y/n]")
    if condition == "n":
        break





