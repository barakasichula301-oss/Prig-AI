[app]

# (str) Title of your application
title = Prig AI

# (str) Package name
package.name = prigai

# (str) Package domain (needed for android packaging)
package.domain = org.baraka

# (str) Source code directory where main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
requirements = python3, kivy, google-generativeai, requests, urllib3, certifi, idna, charset-normalizer, pillow, secure-tarfile

# (str) Supported orientations
orientation = portrait

# -----------------------------------------------------------------------------
# Android specific configurations
# -----------------------------------------------------------------------------

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions your app requires
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 26

# (str) Standard stable NDK release string Google's servers accept
android.ndk = r25b

# (bool) Use private storage for data
android.private_storage = True

# (list) The Architecture your APK targets
android.archs = arm64-v8a

# (bool) Automatically accept the SDK licenses on the cloud server
android.accept_sdk_license = True

# -----------------------------------------------------------------------------
# Buildozer configurations
# -----------------------------------------------------------------------------

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 0
