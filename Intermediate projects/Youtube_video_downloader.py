# from pytube import YouTube
import yt_dlp
import tkinter as tk
from tkinter import filedialog

'''def download_video(url,save_path):
    try:
        yt=YouTube(url)
        streams= yt.streams.filter(progressive=True,file_extension="mp4")
        highest_res_stream=streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully")
    
    except Exception as e:
        print(e)'''

def download_video(url, save_path):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'format': 'best[ext=mp4]/best',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            #Open a downloader using these settings, do the download, then close everything neatly.
            ydl.download([url])
        print("Video downloaded successfully")
    except Exception as e:
        print("Error:", e)

def open_file_dialog():
    folder= filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder

if __name__ == "__main__":
    #This line ensures that the following code only runs when the script is executed directly, not when it’s imported as a module into another script.
    root= tk.Tk()
    '''tk here refers to the Tkinter module — Python’s built-in GUI library.
    Tk() creates the main application window (often called the “root window”).
    This window is necessary before you can use other GUI elements (like message boxes or file dialogs).'''
    root.withdraw()
    '''This hides the main window right after it’s created.
    It doesn’t destroy it — it just makes it invisible.
    You do this when you don’t want a blank GUI window to appear, but still want to use Tkinter dialogs.'''

    video_url = input("Please enter a youtube url : ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started Downloading")
        download_video(video_url,save_dir)
    else:
        print("Invalid save location")

    


