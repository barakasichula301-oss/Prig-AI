[app]
# (str) Title of your application
title = Prig AI

# (str) Package name
package.name = prigai

# (str) Package domain (needed for android packaging)
package.domain = org.baraka

# (str) Source code directory where main.py lives
source.dir = .

# (list) Source files to include (let's include all python files)
source.include_exts = py

# (str) Application versioning
version = 1.0

# (list) Application requirements
# We must include kivy, the google-generativeai SDK, and its background requirements
requirements = python3, kivy==2.3.0, google-generativeai, requests, urllib3, certifi, idna, charset-normalizer, pillow, secure-tarfile

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Permissions your app needs
# This ensures your app can connect to the internet to talk to Gemini
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support (Android 8.0+)
android.minapi = 26

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use architectures for modern devices
android.archs = arm64-v8a

# (str) The format used to package the app
android.release_artifact = apk
