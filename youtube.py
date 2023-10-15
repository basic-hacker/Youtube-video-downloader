from pytube import YouTube
import shutil
import os

try:
    import pytube
except ImportError:
    print("pytube not installed. Installing...")
    os.system("pip install -r requirements.txt")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

banner = """
:'######::'##::::'##::::'###::::'########:'##:::::::
'##... ##: ###::'###:::'## ##::: ##.....:: ##:::::::
 ##:::..:: ####'####::'##:. ##:: ##::::::: ##:::::::
. ######:: ## ### ##:'##:::. ##: ######::: ##:::::::
:..... ##: ##. #: ##: #########: ##...:::: ##:::::::
'##::: ##: ##:.:: ##: ##.... ##: ##::::::: ##:::::::
. ######:: ##::::: ##: ##:::: ##: ########: ########:
:......:::..:::::::..::..:::::..::........::........::
"""
terminal_width = shutil.get_terminal_size().columns

num_spaces = (terminal_width - max(len(line) for line in banner.split('\n'))) // 2

print('\n'.join(' ' * num_spaces + line for line in banner.split('\n')))

video_url = input("Enter the YouTube video URL: ")

try:
    yt = YouTube(video_url)

    print("Options:")
    print("1. Download as video (MP4)")
    print("2. Download as audio (MP3)")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        video_streams = yt.streams.filter(file_extension='mp4')
        print("Available video resolutions:")
        for i, stream in enumerate(video_streams, start=1):
            print(f"{i}. {stream.resolution}")

        chosen_number = int(input("Enter the number for the resolution you want to download: "))

        if 1 <= chosen_number <= len(video_streams):
            video_stream = video_streams[chosen_number - 1]
            # Download the video to the current directory
            video_stream.download()
            print('Download completed!')
        else:
            print('Invalid number. Please choose a valid number.')

    elif choice == 2:
        audio_stream = yt.streams.filter(only_audio=True).first()

        if audio_stream:
            audio_stream.download(filename_prefix='audio_')
            print('Download completed! (MP3)')
        else:
            print('Audio stream not available.')

    else:
        print('Invalid choice. Please choose 1 or 2.')

except Exception as e:
    print('An error occurred:', str(e))
