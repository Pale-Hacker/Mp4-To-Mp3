import os
import moviepy.editor as mp

# --- #


def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def Banner():
    Clear()
    print(""" __  __      _  _              _______               __  __      ____  
|  \/  |    | || |            |__   __|             |  \/  |    |___ \ 
| \  / |_ __| || |_   ______     | | ___    ______  | \  / |_ __  __) |
| |\/| | '_ \__   _| |______|    | |/ _ \  |______| | |\/| | '_ \|__ < 
| |  | | |_) | | |               | | (_) |          | |  | | |_) |__) |
|_|  |_| .__/  |_|               |_|\___/           |_|  |_| .__/____/ 
       | |                                                 | |         
       |_|                                                 |_|         \n\nCreated By : Pale-Hacker\n""")

# --- #


try:
    Banner()

    Video_Name = input("Enter Video Name : ")
    Audio_Name = input("Enter Audio Name : ")

    if Video_Name.endswith(".mp4") and Audio_Name.endswith(".mp3"):
        Banner()
        print("Converting Video To Audio ..\n")
        Clip = mp.VideoFileClip(Video_Name)
        Clip.audio.write_audiofile(Audio_Name)
        print(f"\nVideo Converted ! \"{Audio_Name}\"")
    else:
        Banner()
        print("Converting Video To Audio ..\n")
        Clip = mp.VideoFileClip(f"{Video_Name}.mp4")
        Clip.audio.write_audiofile(f"{Audio_Name}.mp3")
        print(f"\nVideo Converted ! \"{Audio_Name}.mp3\"")
except:
    print("Error !")
    exit()

# --- #

input("\n\nPress \"Enter\" To Exit ! ")

# --- #
