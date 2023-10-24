"""
    Filename: org.py
    Author: Alex Williams
    Date Created: 24/10/23
    Date Last Modified: 24/10/23
    Python Version: 3.12.0
"""

import os
import shutil

directories = {
    "audio": [".mp3", ".ogg", ".flac", ".wav", ".flv"],

    "video": [".mp4", ".mov", ".webm"],

    "img": [".jpg", ".jpeg", ".gif", ".png", ".webp", ".svg", ".jfif"],

    "doc": [".doc", ".docx", ".pdf", ".rtf", ".txt"],

    "archive": [".rar", ".zip", ".jar", ".7z", ".iso"]
}

def is_audio(file):
    return os.path.splitext(file)[1] in directories["audio"]

def is_video(file):
    return os.path.splitext(file)[1] in directories["video"]

def is_img(file):
    return os.path.splitext(file)[1] in directories["img"]

def is_doc(file):
    return os.path.splitext(file)[1] in directories["doc"]

def is_archive(file):
    return os.path.splitext(file)[1] in directories["archive"]

for key in directories:
    if not os.path.exists(key):
        os.mkdir(key)

for file in os.listdir():
    if is_audio(file):
        shutil.move(file, "audio")
    elif is_video(file):
        shutil.move(file, "video")
    elif is_img(file):
        shutil.move(file, "img")
    elif is_doc(file):
        shutil.move(file, "doc")
    elif is_archive(file):
        shutil.move(file, "archive")