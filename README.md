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
vid	clip2.mp4
img	fin.png
img	black.png
```

This file sets up the output to be 1920x1080px with a framerate of 24fps, with a 24 frame cross-fade between each sequence. 

The movie consists of:
* a title image (displayed for 96 frames)
* a video clip (clip1.mp4) trimmed by 5 and 10 frames
* another video clip (clip2.mp4) untrimmed.
* a fin image (displayed for 48 frames)
* a black image (displayed for 48 frames)

### Commands
#### res
Sets the project resolution.
Parameters:
* width (required)
* height (required)

### frt
Sets the project framerate.
Parameters:
* framerate (required)

### ctm
Sets the cross fade time
Parameters:
* time in frames (required)

### img
Adds an image
Parameters:
* image path (required). Must be relative to .am file
* display time (optional). Length of time in frames that image is shown. Defaults to 48 frames.

### vid
Adds an video clip
Parameters:
* clip path (required). Must be relative to .am file
* start trim (optional). Number of frames to trim from the start of the clip. Defaults to 0 frames.
* end trim (optional). Number of frames to trim from the end of the clip. Defaults to 0 frames. 

## Notes/Issues
* Code is ugly, lots of globals etc
* Audio on video clips is not currently imported
 

 


