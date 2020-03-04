# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.8.1
#
# Author:       Pedro Suarez


from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import time
import shutil
import sqlite3

import final
import final_gui


# Get the window centered on the screen

def center_window(self, w, h): 
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# Source Directory select function

def search_sourceDir(self):
    
    source_path=filedialog.askdirectory(initialdir=os.getcwd(),title='Pick a directory')
    if source_path:
        self.txtSource.insert(INSERT,source_path)
        self.source_dir = source_path
   
# Destination dir select function
                                
def search_destDir(self):
    
    dest_path=filedialog.askdirectory(initialdir=os.getcwd(),title='Pick a directory')
    if dest_path:
         self.txtDestination.insert(INSERT,dest_path)
         self.dest_dir = dest_path    
            
# .txt files search + transfer + record into db + print into the console 
                
def work_with_files(self):

    # Warning message if dir not selected 
    if len(self.txtSource.get("1.0", "end-1c")) == 0:
        messagebox.showwarning("Warning", "You have not selected both directories")
    elif len(self.txtDestination.get("1.0", "end-1c")) == 0:
        messagebox.showwarning("Warning", "You have not selected both directories") 
        
    # Create db for the files
    conn = sqlite3.connect('files.db')

    with conn:
         cur = conn.cursor()
         cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname VARCHAR(25), \
            col_mtime VARCHAR(50) \
          )")
         conn.commit()
    conn.close()

    # txt files search   
    fList = os.listdir(self.source_dir)
    for f in fList:
        if f.endswith('.txt'):
            txt_files_source = os.path.join(self.source_dir,f) # Absolute path of txt file in the source dir
            txt_files_dest = os.path.join(self.dest_dir,f) # Absolute path of txt file in the destination dir

            # Trasfer the file into destination dir
            shutil.move(txt_files_source,txt_files_dest)

            # Extract the file name from the file path
            file_name=os.path.basename(txt_files_dest)

            # Get the file modified time-stamp 
            mod_time = time.localtime(os.path.getmtime(txt_files_dest)) # Get date & time modified
            fm_time = time.strftime("%m/%d/%Y, %H:%M:%S", mod_time) # Convert time into common date & time format

            # Print the file name and modified time-stamp 
            print("File Name:", file_name,"Modified:", fm_time)

            # Record the file name and modified time-stamp into the db: files.db
            conn = sqlite3.connect('files.db')
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files(col_fname,col_mtime) VALUES (?,?)",(file_name,fm_time,))
                conn.commit()
            conn.close()

    
            
if __name__ == "__main__":
    pass
