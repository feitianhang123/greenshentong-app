[app]

# (str) Title of your application
title = 绿申通

# (str) Package name
package.name = greenshentong

# (str) Package domain (needed for android/ios packaging)
package.domain = org.greenshentong

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to ignore (let empty to not ignore anything)
#source.exclude_exts = spec

# (list) List of directory to ignore
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,flask,pandas,openpyxl,requests,chardet

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/assets/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT_TO_PY2

#
# OSX Specific
#

#
# Android specific
#

# (bool) Indicates if the application should be fullscreen or not
fullscreen = 0

# (string) Android intent category
android.intent.category = LAUNCHER

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
#android.api = 28

# (int) Minimum API your APK will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 19b

# (int) Android NDK API to use. This is the minimum API your project will support.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) Antivirus tool to scan the APK
#android.antivirus = 

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
#android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
#android.accept_sdk_license = False

# (str) Android entry point
#android.entrypoint = org.renpy.android.PythonActivity

#
# Buildozer specific
#

# (str) The directory in which buildozer will store logs
#log_dir = .logs

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
#log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
#disable_run_as_root_warning = 0

# (int) Disable colored output
#disable_colors = 0

# (list) Enable compilation with cython
#cythonize = 

# (str) Path to a custom cython configuration file
#cython_config = 

# (str) Path to a custom setuptools configuration file
#setuptools_config = 

# (int) Build timeout in seconds
#build_timeout = 0