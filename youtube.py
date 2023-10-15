from pytube import YouTube
import subprocess
import shutil

# Install the necessary libraries
try:
    subprocess.run(["pip", "install", "pytube"])
except Exception as e:
    print('An error occurred during library installation:', str(e))

# Rest of the script...

# The rest of your script remains the same



# The ASCII art banner
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

# Get the terminal width
terminal_width = shutil.get_terminal_size().columns

# Calculate the number of spaces needed to center the banner
num_spaces = (terminal_width - max(len(line) for line in banner.split('\n'))) // 2

# Print the banner with centered alignment
print('\n'.join(' ' * num_spaces + line for line in banner.split('\n')))


# Prompt the user to input the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

try:
    # Create a YouTube object
    yt = YouTube(video_url)

    print("Options:")
    print("1. Download as video (MP4)")
    print("2. Download as audio (MP3)")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        # Display available video streams and resolutions
        video_streams = yt.streams.filter(file_extension='mp4')
        print("Available video resolutions:")
        for i, stream in enumerate(video_streams, start=1):
            print(f"{i}. {stream.resolution}")

        # Prompt the user to choose a resolution
        chosen_number = int(input("Enter the number for the resolution you want to download: "))

        if 1 <= chosen_number <= len(video_streams):
            video_stream = video_streams[chosen_number - 1]
            # Download the video to the current directory
            video_stream.download()
            print('Download completed!')
        else:
            print('Invalid number. Please choose a valid number.')

    elif choice == 2:
        # Get the highest quality audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        if audio_stream:
            # Download the audio as MP3
            audio_stream.download(filename_prefix='audio_')
            print('Download completed! (MP3)')
        else:
            print('Audio stream not available.')

    else:
        print('Invalid choice. Please choose 1 or 2.')

except Exception as e:
    print('An error occurred:', str(e))
