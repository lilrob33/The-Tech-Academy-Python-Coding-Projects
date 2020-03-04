#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.8.1
#
# Author:       Pedro Suarez
#
# Purpose:      For this drill, you will need to gather all of the drills
#               that you have previously completed for this course and write
#               a new script that will use each of the concepts that you had
#               previously used to complete this drill assignment.
#               Your new script will need to provide the user with a graphical
#               user interface that includes two buttons allowing the user to
#               browse their own system and select a source directory and
#               a destination directory. Your script should also show those
#               selected directory paths in their own corresponding text fields.
#               Next, your script will need to provide a button for the user to
#               execute a function that should iterate through the source
#               directory, checking for the existence of any files that end
#               with a “.txt” file extension and if so, cut the qualifying
#               files and paste them within the selected destination directory.
#               Finally, your script will need to record the file names that
#               were moved and their corresponding modified time-stamps into
#               a database and print out those text files and their modified
#               time-stamps to the console.

# Requirements:
#       1. Your script will need to use Python 3, the Tkinter module, and
#          the OS module.
#       2. Your script will need to use the listdir() method from the OS
#          module to iterate through all files within a specific directory.
#       3. Your script will need to use the path.join() method from the
#          OS module to concatenate the file name to its file path,
#          forming an absolute path.
#       4. Your script will need to use the getmtime() method from the
#          OS module to find out the latest date the file has been created
#          or last modified.
#       5. Your script will need to create a database to record the
#          qualifying file and corresponding modified time-stamp.
#       6. Your script will need to print each file ending with a
#          “.txt” file extension and its corresponding mtime to the console.
#       7. Your script will need to use the move() method from the Shutil
#          module to cut all qualifying files and paste them within the
#          destination directory.
#
#       Additional Setup Instructions:
#       To complete this final drill assignment, you will need to use
#       the directory you had previously created on your system from
#       an earlier drill assignment.
#       This directory should have at least 10 different files types,
#       two of which should be text documents that end with the
#       “.txt” file extension.





from tkinter import *
import tkinter as tk

import final_gui
import final_func
                        

class MainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
    
        self.master = master
        self.master.minsize(800,330) 
        self.master.maxsize(800,330)
        self.master.title("Files Transfer")
        self.master.configure(bg="#F0F0F0")
        final_func.center_window(self,800,300)
        

        final_gui.window_gui(self)


if __name__ == "__main__":
    root = Tk()
    App = MainWindow(root)
    root.mainloop()
