from tkinter import filedialog
import tkinter as tk 
from pytube import YouTube

class Downloader:
    def __init__(self):
        self.url = input("Enter a YouTube url: ")
        self.save_path = self.open_file_dialog()

    def open_file_dialog(self):
        folder = filedialog.askdirectory()

        if folder:
            print(f"Selected folder is {folder}")

        return folder
    
    def download_video(self, url, save_path):
        try:
            yt = YouTube(url)
            streams = yt.streams.filter(file_extension='mp4')
            highest_resolution = streams.get_highest_resolution()
            highest_resolution.download(output_path=save_path)
            print("Video downloaded successfully!")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    downloader = Downloader()

    url = downloader.url
    save_path = downloader.save_path

    if downloader.save_path:
        print("Started download")
        downloader.download_video(url, save_path)
    else:
        print("Invalid save location")
    