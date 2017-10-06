# SERMON MOVIE MAKER
------------------
Creator: MeIchthys

License: Unlicensed (See LICENSE.txt)


## History
After searching for a program that could convert an mp3 into an mp4, I decided to build my own script that could do it automatically. Thus Sermon Movie Maker was born.

## What is Does
Converts an mp3 file + an image file + text descriptions into a mp4 video with a static image and text.


## How to Use it

1. Double click the SermonMovieMaker app in the 'dist' directory.

2. When prompted, enter the following information:

	a. Full path to image file (you can drag the file into the terminal)

	b. Full path to mp3 file (you can drag the file into the terminal)

	c. Name of the mp4 file to be generated (excluding the extension)

	d. First line of text (Sermon Title)

	e. Second line of text (Speaker Name)

	f. Third line of text (Date)


3. The program will then get to work on exporting the mp4 file to the location set in the settings file.


## Configuration
Settings can be changed in the settings.py file to modify the appearance of the overlaid text, location of the font file, output directory, etc.


## Development Requirements
Python 3.6
See requirements.txt
