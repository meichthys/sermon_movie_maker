# SERMON MOVIE MAKER

![Screenshot](screenshot.png "Screenshot")

Creator: MeIchthys
License: MIT (See LICENSE.txt)

## History

After searching for a simple program that could convert an mp3 into an mp4, I decided to build my own script that could do it automatically. Thus Sermon Movie Maker was born.

## What is Does

Converts an mp3 file + a jpg image file + text descriptions into a mp4 video with a static image and text (see screenshot above). The mp4 file is facebook compatible, and should play well in most browsers if uploaded to a webpage.

## How to install/deploy

Run the following command from within the scripts directory to build a MacOS app that can be run like any other mac app:

`sh buildapp.sh`

Pyinstaller can support other platforms as well, so it should be very easy to port to windows and linux.

## How to Use it

1. Double click the SermonMovieMaker app in the 'dist' directory. This app is stand-alone and can be moved anywhere.

2. When prompted, enter the following information:

    - Full path to image file (you can drag the file into the terminal) or image search term.
    - Full path to mp3 file (you can drag the file into the terminal)
    - Name of the mp4 file to be generated (excluding the extension)
    - First line of text (Sermon Title)
    - Second line of text (Speaker Name)
    - Third line of text (Date)

3. The program will then get to work on exporting the mp4 file to the location set in the settings file.

## Configuration

Settings can be changed in the settings.py file to modify the appearance of the overlaid text, location of the font file, output directory, etc.

## Development Requirements

See [Pipfile](Pipfile)
