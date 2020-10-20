from django.shortcuts import render
from django.http import HttpResponse
from hurry.filesize import size, alternative
from pytube import YouTube
from tkinter import filedialog
import tkinter as tk
link = ""
folder_name = ""


def openWindow():
    global folder_name
    root = tk.Tk()
    label = tk.Label(text="Close this window")
    label.grid()
    folder_name = filedialog.askdirectory()
    root.mainloop()


def home(request):
    return render(request, 'homePage.html')


def getUrl(request):
    global link
    link = request.POST['urlLink']
    yt = YouTube(link)
    steam = yt.streams[1]
    filesize = size(steam.filesize, system=alternative)
    return render(request, 'homePage.html', {'link': link, 'fileSize': filesize, 'title': yt.title, 'views': yt.views, 'length': yt.length, 'rating': yt.rating, 'thumb': yt.thumbnail_url})


def download(request):
    openWindow()
    yt = YouTube(link)
    url = yt.streams.get_highest_resolution()
    url.download(folder_name)
    done = True
    return HttpResponse('Return data to ajax call')


