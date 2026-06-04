[app]

# (str) Title of your application
title = Prig AI

# (str) Package name
package.name = prigai

# (str) Package domain (needed for android packaging)
package.domain = org.baraka

# (str) Source code directory where main.py lives
source.dir = .

# (list) Source files to include (let's include everything python and kv related)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# All your necessary dependencies are listed cleanly right here without restrictive version pins
requirements = python3, kivy, google-generativeai, requests, urllib3, certifi, idna, charset-normalizer, pillow, secure-tarfile

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# -----------------------------------------------------------------------------
# Android specific configurations
# -----------------------------------------------------------------------------

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions your app requires (Internet is essential for Gemini AI)
android.permissions = INTERNET

# (int) Target Android API, should match the pre-installed platform tools
android.api = 34

# (int) Minimum API your APK will support
android.minapi = 26

# (str) The exact Android NDK version pre-cached on the GitHub runner
android.ndk = 27.3.13750724

# (bool) Use private storage for data (true or false)
android.private_storage = True

# (list) The Architecture your APK targets (arm64-v8a is standard for modern phones)
android.archs = arm64-v8a

# (bool) Automatically accept the SDK licenses on the cloud server
android.accept_sdk_license = True

# -----------------------------------------------------------------------------
# Buildozer configurations
# -----------------------------------------------------------------------------

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
