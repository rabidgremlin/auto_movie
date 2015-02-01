"""
TBD
"""


import bpy,os

current_channel = 1
current_frame = 1
scene = None
base_path = ""
cross_time = 24
def_image_length = 48

def init_nle(filepath):
    global scene, current_channel, current_frame,base_path
    
    scene = bpy.context.scene   
    scene.sequence_editor_clear()  
    scene.sequence_editor_create()
    
    current_channel = 1
    current_frame = 1
    base_path = os.path.dirname(os.path.abspath(filepath))
    print(base_path)       

def toggle_channel():
    global current_channel
    current_channel +=1
    if current_channel > 2:
        current_channel = 1

def increment_current_frame(sequence):
    global current_frame
    current_frame += sequence.frame_final_duration

def do_set_resolution(params):
    x_res = int(params[0])
    y_res = int(params[1])    
    print("Setting resolution to  %d x %d" % (x_res,y_res))
    print(scene)
    
    scene.render.resolution_x = x_res
    scene.render.resolution_y = y_res


def do_set_frame_rate(params):
    frame_rate = int(params[0])    
    print("Setting frame rate to %d" % (frame_rate))
    
    scene.render.fps = frame_rate
    scene.render.fps_base = 1

def do_set_cross_time(params):
    global cross_time
    cross_time = int(params[0])    
    print("Setting default crossfade time to %d" % (cross_time))

def do_insert_image(params):
    image_path = os.path.join(base_path,str(params[0]))
    
    image_length = def_image_length
    if len(params) >= 2:
        image_length = int(params[1])
       
    
    print("Insert image here" + str(image_path))
    
    image_seq = scene.sequence_editor.sequences.new_image(
                name=image_path,
                filepath=image_path,
                channel=current_channel, frame_start=current_frame)
    
    image_seq.frame_final_duration = image_length
    
    toggle_channel()
    increment_current_frame(image_seq) 
                
    
def do_insert_video(params):    
    clip_path = os.path.join(base_path,str(params[0]))
    
    offset_start = 0
    if len(params) >= 2:
        offset_start = int(params[1])
    
    offset_end = 0
    if len(params) >= 3:
        offset_end = int(params[2])    
    
    print("Insert video here" + str(clip_path))
    
    vid_seq = scene.sequence_editor.sequences.new_movie(
        name=clip_path,
        filepath=clip_path,
        channel=current_channel, frame_start=current_frame)	
		
    vid_seq.animation_offset_start=offset_start
    vid_seq.animation_offset_end=offset_end
    
    toggle_channel()
    increment_current_frame(vid_seq)    


def do_cmd(command):
    instr = command[0]    
    print ("Executing command %s" % instr)
    
    if not instr or instr[0] == '#':
        return
    
    if instr == "res":
        do_set_resolution(command[1:])
    else:
        if instr == "frt":
            do_set_frame_rate(command[1:])
        else:
            if instr == "ctm":
                do_set_cross_time(command[1:])
            else:
                if instr == "img":
                    do_insert_image(command[1:])
                else:
                    if instr == "vid":
                        do_insert_video(command[1:])
                    else:
                        print("Error! Unknown command")
    

def read(filepath):
    init_nle(filepath)    
    
    print("loading file " + filepath)     
    
    filehandle = open(filepath, "r")
    for line in filehandle.readlines():
        do_cmd(line.strip().split("\t"))
        
    scene.frame_end = current_frame
    bpy.context.window.screen = bpy.data.screens["Video Editing"]    

if __name__ == "__main__":
    read("/tmp/auto-movietest/test.am")