**

# simpleSlice

## If you're a pro 
If you're at least familiar with python scripts, arguments, and the command line, this should be easy for you to use.
 - Clone the repo or download the zip
 - Run the python script with python3 and provide the correct arguments (see below)
 
 ## If you're a beginner
 This program will seem a kinda scary to use (you'll need to use the command line) but it's really not complex or dangerous at all. Here are the steps
 Note: This guide is only for Mac or any unix environment because, well, Python on windows is a mess. Plus the way they specify directories sucks.
 - Download and install python3.x (any version of python 3 should work)
 - Open your command line. On mac it's an app called 'terminal' already installed on your mac. On linux, well, if you're on linux and need to read this guide, umm.
 - On the mac command line, copy and paste in the following command. All it does is install a simple image processing package. 
 `pip install opencv-python`
 If it doesn't work, do what all engineers do and copy the error into google and do some researching.
 - Now, let's tell our terminal WHERE our program is. I'm assuming this folder is in your downloads, so type in:
 `cd ~/Downloads/simpleSplicer`
Note, if this is somewhere else, like documents, you can type `cd ~/Documents/simpleSplicer``
 - Alright! Now you're ready to run the program. You do so by typing in:
 `python3 splice.py --video testVideo.mp4`
 - Let it run for a little bit (a few min at most)
 - What did we just do? Well, that command told your computer to execute my program, which splices the video into individual frames! Where are those frames? Check now in the 'output' folder in the simpleSplicer folder (where this program lives)
 - Now, how do we control that? We use things called arguments. The `--video testVideo.mp4` is actually an argument! It told the program, "Hey, use the video called testVideo.mp4 to splice from."
 All arguments (across all of compsci) follow the following format:
 `--<argument> <data>`
 And you can have multiple of these! Let me list all the possible arguments for our pro's and then I'll give you some examples.
## **Arguments:** 
 - `--video <videoname.mp4>`
 Specify video to splice from
 Example to splice from a file named testVideo.mp4: `--video testVideo.mp4`
 Note: You **must** put the video you wanna splice from in the same folder that `splice.py` lives.
 
 - `--start_frame <number of frame to start from>`
 Specify the number of the frame to start from 
 Example to start on the 10th frame of the video: `--start_frame 10`
 
 - `--end_frame <number of frame to end at>`
 Specify the number of the frame to start from 
 Example to end on the 100th frame of the video: `--end_frame 100`

 - `-path <absolute path to save frames to>`
 Specify the absolute path of the frames save location
 **Do not use this if you're a beginner**, stick with everything being put into `output` and just move them out like you know how every time.
 
  - `--prepend <words to put at the beginning>`
 Specify a string to put before the number of the frame in the name of the file
 Example to add "raw" to the beginning of the name of each frame image that you're gonna save: `--prepend raw` results in files called "rawX.jpg"
  - `--append <words to put at the end>` 
 Specify a string to put after the number of the frame in the name of the file
 Example to add "raw" to the beginning of the name of each frame image that you're gonna save: `--append capture` results in files called "Xcapture.jpg"

**You can use both!**
 - Example to add "raw" to the beginning and "capture" to the end of the name of each frame image that you're gonna save: `--prepend raw --append capture` results in files called "rawXcapture.jpg"

- `--leading <number of total available leading zeroes for the number of each frame>` 
 Specify a how many leading zeroes you want
 Example to add two leading zeroes to the beginning of the number  in each frame image that you're gonna save: `--leading 2` results in:
 "01.jpg"
 "41.jpg"
 "99.jpg"
 "119.jpg"
 `--leading 3` results in:
 "001.jpg"
 "041.jpg"
 "099.jpg"
 "119.jpg"
 And so on
