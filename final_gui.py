# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.8.1
#
# Author:       Pedro Suarez


from tkinter import *
import tkinter as tk

import final
import final_func


def window_gui(self):
    
    self.lblHeading = Label(self.master, text='Please select Source and Destination directories for .txt files to transfer:', font=("Helvetica",16), fg='black')
    self.lblHeading.grid(row=0, columnspan=2, pady=(20,0))
        
    self.btnSource = Button(self.master, text="Source Dir", width=13, font=("Helvetica",16), fg='black', command=lambda: final_func.search_sourceDir(self))
    self.btnSource.grid(row=1, column=0, padx=20, pady=40)
        
    self.btnDestination = Button(self.master, text="Destination Dir", width=13, font=("Helvetica",16), fg='black', command=lambda: final_func.search_destDir(self))
    self.btnDestination.grid(row=2, column=0, padx=20)

    self.txtSource = Text(self.master,width=50, height=1, font=("Helvetica",14), fg='black',bg='white')
    self.txtSource.grid(row=1, column=1, padx=10, sticky=E)
      
    self.txtDestination = Text(self.master, width=50, height=1, font=("Helvetica",14), fg='black',bg='white')
    self.txtDestination.grid(row=2, column=1, padx=10, sticky=E)

    self.btnTransfer = Button(self.master, text="TRANSFER", width=13, height=2, font=("Helvetica",16), fg='black', bg='lightgrey', command=lambda: final_func.work_with_files(self))
    self.btnTransfer.grid(row=3, column=1, padx=10, pady=20, sticky=E)


if __name__ == "__main__":
    pass
