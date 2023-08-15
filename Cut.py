from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from datetime import datetime


def convert_to_seconds(time_str):
    time_obj = datetime.strptime(time_str, '%H:%M:%S')
    return time_obj.time().hour * 3600 + time_obj.time().minute * 60 + time_obj.time().second


video_path = 'test.mp4'
video_clip = VideoFileClip(video_path)

time_ranges = [('00:00:10', '00:00:40'),
               ('00:00:50', '00:01:40'),
               ('00:01:50', '00:03:10')]

subclips = []
end_of_previous = 0

for start_time_str, end_time_str in time_ranges:
    start_time = convert_to_seconds(start_time_str)
    end_time = convert_to_seconds(end_time_str)
    subclip = video_clip.subclip(end_of_previous, start_time)
    subclips.append(subclip)
    end_of_previous = end_time


subclip = video_clip.subclip(end_of_previous)
subclips.append(subclip)

final_clip = concatenate_videoclips(subclips)


output_path = 'output.mp4'
final_clip.write_videofile(output_path, codec='libx264', preset='ultrafast')
