from django.shortcuts import render
from django.http import HttpResponse
from hurry.filesize import size, alternative
from pytube import YouTube
from tkinter import filedialog
import tkinter as tk
import math

link = ""
folder_name = ""
millnames = ['', ' Thousand', ' Million', ' Billion', ' Trillion']


def millify(n):
    n = float(n)
    millidx = max(0, min(len(millnames) - 1,
                         int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))))

    return '{:.0f}{}'.format(n / 10 ** (3 * millidx), millnames[millidx])


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
    return render(request, 'homePage.html',
                  {'link': link, 'fileSize': filesize, 'title': yt.title, 'views': millify(yt.views), 'length': yt.length,
                   'rating': yt.rating, 'thumb': yt.thumbnail_url})


def download(request):
    openWindow()
    yt = YouTube(link)
    url = yt.streams.get_highest_resolution()
    url.download(folder_name)
    done = True
    return HttpResponse('Return data to ajax call')
