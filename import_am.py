"""
TBD
"""


import bpy


def read(filepath):
    #convert the filename to an object name
    objName = bpy.path.display_name_from_filepath(filepath)
    print("loading file " + filepath)     
    
    filehandle = open(filepath, "rb")
    for line in filehandle.readlines():
        print(line)

if __name__ == "__main__":
    read("/tmp/auto-movietest/test.am")