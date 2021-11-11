# This is a sample script to download video from youtube

from pytube import YouTube

# Get youtube video link from user
yt_url = input("Enter a valid youtube video link:\n\t")
from pytube.cli import on_progress

yt_url = "http://youtube.com/watch?v=2lAe1cqCOXo"
yt = YouTube(yt_url, on_progress_callback=on_progress)
print(yt.title)



# Stream all format available for the video or filter it by type : video or audio
def filter_by_type(chosen_type=None):
    return yt.streams.filter(type=chosen_type)


# index all formats in list
selected_streams = filter_by_type()  # None or video or audio

for i, vid in list(enumerate(selected_streams)):
    print(f"{i} {vid.type} {vid.mime_type}, {vid.resolution}, {vid.abr}")

_option = int(input("Choose desired option: "))
target_down = selected_streams[_option]

file_size = target_down.filesize
print(f"the file size is : {file_size / 1024**2:.2f} MB")


target_down.download(output_path='C:\\Users\\RammaH\\Downloads\\YT', filename=None,
                     filename_prefix='YT_' + target_down.type, skip_existing=True)
print(f"<<{yt.title}>> is dowloaded successfully in {target_down.mime_type}:{target_down.resolution}!")




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
