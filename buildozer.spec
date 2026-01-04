[app]
title = TextToAudio
package.name = texttoaudio
package.domain = org.textaudio
source.dir = .
source.include_exts = py
version = 1.0

requirements = python3,kivy,pyttsx3

orientation = portrait
fullscreen = 0

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
