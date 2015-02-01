# auto_movie
Blender plugin that creates a movie (in Blenders Video Sequence Editor), from a list of clips. It handles video clips and images and puts a cross fade between each. 

The list of clips and images are defined in a simple text file (with a .am extension)

## How to install
1. Download .zip file (button to the left)
2. Unpack into your Blender scripst folder (should be in it's own sub directory eg auto_movie-master)
3. In Blender go to File -> User Preferences -> Add-ons
4. Search for "auto" and check the check box next to the Auto-movie(.am) plugin

## How to use
1. Select File -> Import -> Auto-movie(.am)
2. Select your .am file

## The auto-movie file
The auto-movie file is a simple text file defining a list of commands for the plugin to process, to create the movie. Each command is placed on a seperate line. Parameters for each command must be seperated by a ```TAB```. Blank lines and lines starting with a # are ignored.

Here is an example .am file:

```
# Example .am file
res	1920	1080
frt	24
ctm	24
img	title.png	96
vid	clip1.mp4	5	10
vid	clip2.mp4	0	0
img	fin.png
img	black.png
```
