#! /usr/bin/env python
#  -*- coding: utf-8 -*-
"""__author__ = "Ashiquzzaman Khan"
__desc__ = "UI file for the alibaba scrapper"
"""

import sys
from tkinter import filedialog

try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk

try:
	import ttk
	py3 = False
except ImportError:
	import tkinter.ttk as ttk
	py3 = True

import ui_support

def vp_start_gui():
	'''Starting point when module is the main routine.'''
	global val, w, root
	root = tk.Tk()
	ui_support.set_Tk_var()
	top = entire_app (root)
	ui_support.init(root, top)
	root.mainloop()

w = None
def create_entire_app(root, *args, **kwargs):
	'''Starting point when module is imported by another program.'''
	global w, w_win, rt
	rt = root
	w = tk.Toplevel (root)
	ui_support.set_Tk_var()
	top = entire_app (w)
	ui_support.init(w, top, *args, **kwargs)
	return (w, top)


def destroy_entire_app():
	global w
	w.destroy()
	w = None


class entire_app:
	def __init__(self, top=None):
		'''This class configures and populates the toplevel window.
			top is the toplevel containing window.'''
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'

		top.geometry("634x360+277+172")
		top.title("Alibaba Scrapper")
		top.configure(background="#d9d9d9")
		top.configure(highlightbackground="#d9d9d9")
		top.configure(highlightcolor="black")

		# custom settings here ================================================
		self._url = ""
		self._category_check = False
		self._filename = ""
		self._directory = ""
		self._previous_csv = ""
		self._user_agents = ""
		self._delay = 0
		self.image_csv = ""

		# Basic Settings  =======================================================
		# frame
		self.basic_label_frame = tk.LabelFrame(top)
		self.basic_label_frame.place(relx=0.008, rely=0.014, relheight=0.458, relwidth=0.986)
		self.basic_label_frame.configure(relief='groove')
		self.basic_label_frame.configure(foreground="black")
		self.basic_label_frame.configure(text='''Basic Settings''')
		self.basic_label_frame.configure(background="#d9d9d9")
		self.basic_label_frame.configure(highlightbackground="#d9d9d9")
		self.basic_label_frame.configure(highlightcolor="black")
		self.basic_label_frame.configure(width=625)
		# url label
		self.url_label = tk.Label(self.basic_label_frame)
		self.url_label.place(relx=0.016, rely=0.182, height=21, width=74, bordermode='ignore')
		self.url_label.configure(activebackground="#f9f9f9")
		self.url_label.configure(activeforeground="black")
		self.url_label.configure(background="#d9d9d9")
		self.url_label.configure(disabledforeground="#a3a3a3")
		self.url_label.configure(foreground="#000000")
		self.url_label.configure(highlightbackground="#d9d9d9")
		self.url_label.configure(highlightcolor="black")
		self.url_label.configure(text='''URL :''')
		# url input
		self.url_entry = tk.Entry(self.basic_label_frame)
		self.url_entry.place(relx=0.192, rely=0.182, height=20, relwidth=0.742, bordermode='ignore')
		self.url_entry.configure(background="white")
		self.url_entry.configure(disabledforeground="#a3a3a3")
		self.url_entry.configure(font="TkFixedFont")
		self.url_entry.configure(foreground="#000000")
		self.url_entry.configure(highlightbackground="#d9d9d9")
		self.url_entry.configure(highlightcolor="black")
		self.url_entry.configure(insertbackground="black")
		self.url_entry.configure(selectbackground="#c4c4c4")
		self.url_entry.configure(selectforeground="black")
		self.url_entry.configure(textvariable=ui_support.Put_URL_here)
		tooltip_font = "TkDefaultFont"
		ToolTip(self.url_entry, tooltip_font, '''Paste The URL Here''', delay=0.5)

		# Output File name label
		self.output_file_label = tk.Label(self.basic_label_frame)
		self.output_file_label.place(relx=0.016, rely=0.364, height=21, width=104, bordermode='ignore')
		self.output_file_label.configure(activebackground="#f9f9f9")
		self.output_file_label.configure(activeforeground="black")
		self.output_file_label.configure(background="#d9d9d9")
		self.output_file_label.configure(disabledforeground="#a3a3a3")
		self.output_file_label.configure(foreground="#000000")
		self.output_file_label.configure(highlightbackground="#d9d9d9")
		self.output_file_label.configure(highlightcolor="black")
		self.output_file_label.configure(text='''Output File Name :''')
		# output File name input
		self.output_folder_entry = tk.Entry(self.basic_label_frame)
		self.output_folder_entry.place(relx=0.192, rely=0.364, height=20, relwidth=0.262, bordermode='ignore')
		self.output_folder_entry.configure(background="white")
		self.output_folder_entry.configure(disabledforeground="#a3a3a3")
		self.output_folder_entry.configure(font="TkFixedFont")
		self.output_folder_entry.configure(foreground="#000000")
		self.output_folder_entry.configure(insertbackground="black")
		self.output_folder_entry.configure(width=164)
		ToolTip(self.output_folder_entry, tooltip_font, '''Type A File Name Here''', delay=0.5)
		# checkbox
		self.cat_chkbx = tk.Checkbutton(self.basic_label_frame)
		self.cat_chkbx.place(relx=0.592, rely=0.364, relheight=0.152, relwidth=0.213, bordermode='ignore')
		self.cat_chkbx.configure(activebackground="#ececec")
		self.cat_chkbx.configure(activeforeground="#000000")
		self.cat_chkbx.configure(background="#d9d9d9")
		self.cat_chkbx.configure(disabledforeground="#a3a3a3")
		self.cat_chkbx.configure(foreground="#000000")
		self.cat_chkbx.configure(highlightbackground="#d9d9d9")
		self.cat_chkbx.configure(highlightcolor="black")
		self.cat_chkbx.configure(justify='left')
		self.cat_chkbx.configure(text='''Only Get Categories''')
		self.cat_chkbx.configure(variable=ui_support.che57)
		ToolTip(self.cat_chkbx, tooltip_font, '''Check If Only Categories Needed''', delay=0.5)

		# output folder label
		self.output_folder_label = tk.Label(self.basic_label_frame)
		self.output_folder_label.place(relx=0.008, rely=0.515, height=31, width=111, bordermode='ignore')
		self.output_folder_label.configure(activebackground="#f9f9f9")
		self.output_folder_label.configure(activeforeground="black")
		self.output_folder_label.configure(background="#d9d9d9")
		self.output_folder_label.configure(disabledforeground="#a3a3a3")
		self.output_folder_label.configure(foreground="#000000")
		self.output_folder_label.configure(highlightbackground="#d9d9d9")
		self.output_folder_label.configure(highlightcolor="black")
		self.output_folder_label.configure(text='''Output Folder :''')
		# output folder browse button
		self.output_folder_br_btn = tk.Button(self.basic_label_frame)
		self.output_folder_br_btn.place(relx=0.216, rely=0.545, height=24, width=117, bordermode='ignore')
		self.output_folder_br_btn.configure(activebackground="#ececec")
		self.output_folder_br_btn.configure(activeforeground="#000000")
		self.output_folder_br_btn.configure(background="#d9d9d9")
		self.output_folder_br_btn.configure(disabledforeground="#a3a3a3")
		self.output_folder_br_btn.configure(foreground="#000000")
		self.output_folder_br_btn.configure(highlightbackground="#d9d9d9")
		self.output_folder_br_btn.configure(highlightcolor="black")
		self.output_folder_br_btn.configure(pady="0")
		self.output_folder_br_btn.configure(text='''Browse''')
		self.output_folder_br_btn.configure(width=117)
		self.output_folder_br_btn.configure(command=self.browsedir)
		# output folder path label
		self.label_out_folder_label = tk.Label(self.basic_label_frame)
		self.label_out_folder_label.place(relx=0.416, rely=0.515, height=31, width=71, bordermode='ignore')
		self.label_out_folder_label.configure(activebackground="#f9f9f9")
		self.label_out_folder_label.configure(activeforeground="black")
		self.label_out_folder_label.configure(background="#d9d9d9")
		self.label_out_folder_label.configure(disabledforeground="#a3a3a3")
		self.label_out_folder_label.configure(foreground="#000000")
		self.label_out_folder_label.configure(highlightbackground="#d9d9d9")
		self.label_out_folder_label.configure(highlightcolor="black")
		self.label_out_folder_label.configure(text='''Folder :''')
		# output folder editable label
		self.out_folder_selected_label = tk.Label(self.basic_label_frame)
		self.out_folder_selected_label.place(relx=0.52, rely=0.515, height=31, width=281, bordermode='ignore')
		self.out_folder_selected_label.configure(activebackground="#f9f9f9")
		self.out_folder_selected_label.configure(activeforeground="black")
		self.out_folder_selected_label.configure(background="#d9d9d9")
		self.out_folder_selected_label.configure(disabledforeground="#a3a3a3")
		self.out_folder_selected_label.configure(foreground="#000000")
		self.out_folder_selected_label.configure(highlightbackground="#d9d9d9")
		self.out_folder_selected_label.configure(highlightcolor="black")
		self.out_folder_selected_label.configure(text='''None''')
		self.out_folder_selected_label.configure(width=281)

		# previous csv label
		self.pre_csv_label = tk.Label(self.basic_label_frame)
		self.pre_csv_label.place(relx=0.008, rely=0.727, height=31, width=121, bordermode='ignore')
		self.pre_csv_label.configure(activebackground="#f9f9f9")
		self.pre_csv_label.configure(activeforeground="black")
		self.pre_csv_label.configure(background="#d9d9d9")
		self.pre_csv_label.configure(disabledforeground="#a3a3a3")
		self.pre_csv_label.configure(foreground="#000000")
		self.pre_csv_label.configure(highlightbackground="#d9d9d9")
		self.pre_csv_label.configure(highlightcolor="black")
		self.pre_csv_label.configure(text='''Previous CSV (if Any) :''')
		self.pre_csv_label.configure(width=121)
		# previous csv browse button
		self.pre_csv_br_btn = tk.Button(self.basic_label_frame)
		self.pre_csv_br_btn.place(relx=0.216, rely=0.727, height=24, width=117, bordermode='ignore')
		self.pre_csv_br_btn.configure(activebackground="#ececec")
		self.pre_csv_br_btn.configure(activeforeground="#000000")
		self.pre_csv_br_btn.configure(background="#d9d9d9")
		self.pre_csv_br_btn.configure(disabledforeground="#a3a3a3")
		self.pre_csv_br_btn.configure(foreground="#000000")
		self.pre_csv_br_btn.configure(highlightbackground="#d9d9d9")
		self.pre_csv_br_btn.configure(highlightcolor="black")
		self.pre_csv_br_btn.configure(pady="0")
		self.pre_csv_br_btn.configure(text='''Browse''')
		self.pre_csv_br_btn.configure(width=117)
		self.pre_csv_br_btn.configure(command=self.browsecsvfile)
		# previous csv name label
		self.label_pre_selected_label = tk.Label(self.basic_label_frame)
		self.label_pre_selected_label.place(relx=0.416, rely=0.727, height=31, width=91, bordermode='ignore')
		self.label_pre_selected_label.configure(activebackground="#f9f9f9")
		self.label_pre_selected_label.configure(activeforeground="black")
		self.label_pre_selected_label.configure(background="#d9d9d9")
		self.label_pre_selected_label.configure(disabledforeground="#a3a3a3")
		self.label_pre_selected_label.configure(foreground="#000000")
		self.label_pre_selected_label.configure(highlightbackground="#d9d9d9")
		self.label_pre_selected_label.configure(highlightcolor="black")
		self.label_pre_selected_label.configure(text='''Previous File :''')
		self.label_pre_selected_label.configure(width=91)
		# previous csv name label editable
		self.pre_selected_selected_label = tk.Label(self.basic_label_frame)
		self.pre_selected_selected_label.place(relx=0.56, rely=0.727, height=31, width=261, bordermode='ignore')
		self.pre_selected_selected_label.configure(activebackground="#f9f9f9")
		self.pre_selected_selected_label.configure(activeforeground="black")
		self.pre_selected_selected_label.configure(background="#d9d9d9")
		self.pre_selected_selected_label.configure(disabledforeground="#a3a3a3")
		self.pre_selected_selected_label.configure(foreground="#000000")
		self.pre_selected_selected_label.configure(highlightbackground="#d9d9d9")
		self.pre_selected_selected_label.configure(highlightcolor="black")
		self.pre_selected_selected_label.configure(text='''No File Selected''')
		self.pre_selected_selected_label.configure(width=261)

		# Advance Settings ======================================================
		# frame
		self.advance_label_frame = tk.LabelFrame(top)
		self.advance_label_frame.place(relx=0.008, rely=0.472, relheight=0.264, relwidth=0.505)
		self.advance_label_frame.configure(relief='groove')
		self.advance_label_frame.configure(foreground="black")
		self.advance_label_frame.configure(text='''Advanced Settings''')
		self.advance_label_frame.configure(background="#d9d9d9")
		self.advance_label_frame.configure(highlightbackground="#d9d9d9")
		self.advance_label_frame.configure(highlightcolor="black")
		self.advance_label_frame.configure(width=320)
		# user agents label
		self.Label2_9 = tk.Label(self.advance_label_frame)
		self.Label2_9.place(relx=0.016, rely=0.263, height=21, width=104, bordermode='ignore')
		self.Label2_9.configure(activebackground="#f9f9f9")
		self.Label2_9.configure(activeforeground="black")
		self.Label2_9.configure(background="#d9d9d9")
		self.Label2_9.configure(disabledforeground="#a3a3a3")
		self.Label2_9.configure(foreground="#000000")
		self.Label2_9.configure(highlightbackground="#d9d9d9")
		self.Label2_9.configure(highlightcolor="black")
		self.Label2_9.configure(text='''User Agents :''')
		# user agents input
		self.user_agents_entry = tk.Entry(self.advance_label_frame)
		self.user_agents_entry.place(relx=0.344, rely=0.263, height=20, relwidth=0.606, bordermode='ignore')
		self.user_agents_entry.configure(background="white")
		self.user_agents_entry.configure(disabledforeground="#a3a3a3")
		self.user_agents_entry.configure(font="TkFixedFont")
		self.user_agents_entry.configure(foreground="#000000")
		self.user_agents_entry.configure(insertbackground="black")
		self.user_agents_entry.configure(width=194)
		self.user_agents_entry.configure(textvariable=ui_support.useragentsvar)
		ToolTip(self.user_agents_entry, tooltip_font, '''Change User Agents Here''', delay=0.5)

		# delay label
		self.Label2_3 = tk.Label(self.advance_label_frame)
		self.Label2_3.place(relx=0.031, rely=0.579, height=21, width=94, bordermode='ignore')
		self.Label2_3.configure(activebackground="#f9f9f9")
		self.Label2_3.configure(activeforeground="black")
		self.Label2_3.configure(background="#d9d9d9")
		self.Label2_3.configure(disabledforeground="#a3a3a3")
		self.Label2_3.configure(foreground="#000000")
		self.Label2_3.configure(highlightbackground="#d9d9d9")
		self.Label2_3.configure(highlightcolor="black")
		self.Label2_3.configure(text='''Delay :''')
		self.Label2_3.configure(width=94)
		# delay input
		self.delya_entry = tk.Entry(self.advance_label_frame)
		self.delya_entry.place(relx=0.344, rely=0.579, height=20, relwidth=0.606, bordermode='ignore')
		self.delya_entry.configure(background="white")
		self.delya_entry.configure(disabledforeground="#a3a3a3")
		self.delya_entry.configure(font="TkFixedFont")
		self.delya_entry.configure(foreground="#000000")
		self.delya_entry.configure(insertbackground="black")
		self.delya_entry.configure(width=194)
		self.delya_entry.configure(textvariable=ui_support.delay)
		ToolTip(self.delya_entry, tooltip_font, '''Change Request Delay to Alibaba Here''', delay=0.5)

		# Image Settings ========================================================
		# frame
		self.image_dl_frame = tk.LabelFrame(top)
		self.image_dl_frame.place(relx=0.521, rely=0.472, relheight=0.39, relwidth=0.473)
		self.image_dl_frame.configure(relief='groove')
		self.image_dl_frame.configure(foreground="black")
		self.image_dl_frame.configure(text='''Image Download''')
		self.image_dl_frame.configure(background="#d9d9d9")
		self.image_dl_frame.configure(highlightbackground="#d9d9d9")
		self.image_dl_frame.configure(highlightcolor="black")
		self.image_dl_frame.configure(width=298)
		# image csv label
		self.img_csv_label = tk.Label(self.image_dl_frame)
		self.img_csv_label.place(relx=0.034, rely=0.138, height=31, width=191, bordermode='ignore')
		self.img_csv_label.configure(activebackground="#f9f9f9")
		self.img_csv_label.configure(activeforeground="black")
		self.img_csv_label.configure(background="#d9d9d9")
		self.img_csv_label.configure(disabledforeground="#a3a3a3")
		self.img_csv_label.configure(foreground="#000000")
		self.img_csv_label.configure(highlightbackground="#d9d9d9")
		self.img_csv_label.configure(highlightcolor="black")
		self.img_csv_label.configure(text='''CSV Files Contains "images_urls" :''')
		self.img_csv_label.configure(width=191)
		# image csv browse button
		self.img_csv_br_btn = tk.Button(self.image_dl_frame)
		self.img_csv_br_btn.place(relx=0.671, rely=0.138, height=24, width=87, bordermode='ignore')
		self.img_csv_br_btn.configure(activebackground="#ececec")
		self.img_csv_br_btn.configure(activeforeground="#000000")
		self.img_csv_br_btn.configure(background="#d9d9d9")
		self.img_csv_br_btn.configure(disabledforeground="#a3a3a3")
		self.img_csv_br_btn.configure(foreground="#000000")
		self.img_csv_br_btn.configure(highlightbackground="#d9d9d9")
		self.img_csv_br_btn.configure(highlightcolor="black")
		self.img_csv_br_btn.configure(pady="0")
		self.img_csv_br_btn.configure(text='''Browse''')
		self.img_csv_br_btn.configure(width=87)
		self.img_csv_br_btn.configure(command=self.browseimagecsvfiles)
		# image csv file name label
		self.label_img_csv_selected_label = tk.Label(self.image_dl_frame)
		self.label_img_csv_selected_label.place(relx=0.067, rely=0.345, height=31, width=71, bordermode='ignore')
		self.label_img_csv_selected_label.configure(activebackground="#f9f9f9")
		self.label_img_csv_selected_label.configure(activeforeground="black")
		self.label_img_csv_selected_label.configure(background="#d9d9d9")
		self.label_img_csv_selected_label.configure(disabledforeground="#a3a3a3")
		self.label_img_csv_selected_label.configure(foreground="#000000")
		self.label_img_csv_selected_label.configure(highlightbackground="#d9d9d9")
		self.label_img_csv_selected_label.configure(highlightcolor="black")
		self.label_img_csv_selected_label.configure(text='''File Name :''')
		# image csv file name editable
		self.img_csv_selected_label = tk.Label(self.image_dl_frame)
		self.img_csv_selected_label.place(relx=0.302, rely=0.345, height=31, width=201, bordermode='ignore')
		self.img_csv_selected_label.configure(activebackground="#f9f9f9")
		self.img_csv_selected_label.configure(activeforeground="black")
		self.img_csv_selected_label.configure(background="#d9d9d9")
		self.img_csv_selected_label.configure(disabledforeground="#a3a3a3")
		self.img_csv_selected_label.configure(foreground="#000000")
		self.img_csv_selected_label.configure(highlightbackground="#d9d9d9")
		self.img_csv_selected_label.configure(highlightcolor="black")
		self.img_csv_selected_label.configure(text='''No File Selected''')
		self.img_csv_selected_label.configure(width=201)

		# Status Settings =======================================================
		# frame
		self.status_frame = tk.LabelFrame(top)
		self.status_frame.place(relx=0.008, rely=0.861, relheight=0.119, relwidth=0.986)
		self.status_frame.configure(relief='groove')
		self.status_frame.configure(foreground="black")
		self.status_frame.configure(text='''Status''')
		self.status_frame.configure(background="#d9d9d9")
		self.status_frame.configure(highlightbackground="#d9d9d9")
		self.status_frame.configure(highlightcolor="black")
		self.status_frame.configure(width=620)
		# editable status laebl
		self.remaining_label = tk.Label(self.status_frame)
		self.remaining_label.place(relx=0.016, rely=0.349, height=21, width=610, bordermode='ignore')
		self.remaining_label.configure(activebackground="#f9f9f9")
		self.remaining_label.configure(activeforeground="black")
		self.remaining_label.configure(background="#d9d9d9")
		self.remaining_label.configure(disabledforeground="#a3a3a3")
		self.remaining_label.configure(foreground="#000000")
		self.remaining_label.configure(highlightbackground="#d9d9d9")
		self.remaining_label.configure(highlightcolor="black")
		# self.remaining_label.configure(textvariable=ui_support.delay)
		self.remaining_label.configure(text='''Idle''')
		self.remaining_label.configure(width=614)
		ToolTip(self.remaining_label, tooltip_font, '''Current Status of the scrapping''', delay=0.5)

		# Main Buttons ==========================================================
		# image download buttons
		self.download_img_btn = tk.Button(self.image_dl_frame)
		self.download_img_btn.place(relx=0.168, rely=0.621, height=34, width=197, bordermode='ignore')
		self.download_img_btn.configure(activebackground="#ececec")
		self.download_img_btn.configure(activeforeground="#000000")
		self.download_img_btn.configure(background="#d9d9d9")
		self.download_img_btn.configure(disabledforeground="#a3a3a3")
		self.download_img_btn.configure(foreground="#000000")
		self.download_img_btn.configure(highlightbackground="#d9d9d9")
		self.download_img_btn.configure(highlightcolor="black")
		self.download_img_btn.configure(pady="0")
		self.download_img_btn.configure(text='''Download Image''')
		self.download_img_btn.configure(width=197)
		self.download_img_btn.configure(command=self.downloadimages)
		# download data buttons
		self.download_data_btn = tk.Button(top)
		self.download_data_btn.place(relx=0.055, rely=0.75, height=34, width=257)
		self.download_data_btn.configure(activebackground="#ececec")
		self.download_data_btn.configure(activeforeground="#000000")
		self.download_data_btn.configure(background="#d9d9d9")
		self.download_data_btn.configure(disabledforeground="#a3a3a3")
		self.download_data_btn.configure(foreground="#000000")
		self.download_data_btn.configure(highlightbackground="#d9d9d9")
		self.download_data_btn.configure(highlightcolor="black")
		self.download_data_btn.configure(pady="0")
		self.download_data_btn.configure(text='''Download Data''')
		self.download_data_btn.configure(width=257)
		self.download_data_btn.configure(command=self.downloaddata)

	# Custom Functions for the UI ==================================================================
	def browsecsvfile(self):
		csvfilename = filedialog.askopenfilename(title="Select A File",
												filetype=(("csv", "*.csv"), ("All Files", "*.*")))
		self._previous_csv = csvfilename
		_fileName = csvfilename.rsplit("/", -1)[-1]
		self.pre_selected_selected_label.configure(text=_fileName)  # update editable label

	def browsedir(self):
		self._directory = filedialog.askdirectory(title="Select A Directory")
		self.out_folder_selected_label.configure(text=self._directory)  # update editable label

	def browseimagecsvfiles(self):
		csvfilename = filedialog.askopenfilename(title="Select A File",
												filetype=(("csv", "*.csv"), ("All Files", "*.*")))
		self.image_csv = csvfilename
		_fileName = csvfilename.rsplit("/", -1)[-1]
		self.img_csv_selected_label.configure(text=_fileName)

	def downloaddata(self):
		# take the url
		self._url = self.url_entry.get()
		# take settings
		self._category_check = ui_support.che57.get()  # Take Category check
		self._directory = self.out_folder_selected_label.cget("text")  # take directory to dump
		self._filename = self.output_folder_entry.get()  # get filename

		# prepare file name _directory + _filename
		self._user_agents = self.user_agents_entry.get()  # get user agents
		self._delay = self.delya_entry.get()  # get delay settings

		# start scraping
		# update stats periodically
		self.remaining_label.configure(text=self._delay)
		# TODO: disable all
		# TODO: Take Settings
		# TODO: Feed The parameters and call run scrapper

	def downloadimages(self):
		# load the csv file
		# take the images_links column
		# start download
		# update stats periodically

		pass

	def updatestatus(self):
		pass

# ======================================================
# Modified by Rozen to remove Tkinter import statements and to receive
# the font as an argument.
# ======================================================
# Found the original code at:
# http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
# ======================================================

from time import time, localtime, strftime

class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=1, follow=True):
        """
        Initialize the ToolTip

        Arguments:
          wdgt: The widget this ToolTip is assigned to
          tooltip_font: Font to be used
          msg:  A static string message assigned to the ToolTip
          msgFunc: A function that retrieves a string to use as the ToolTip text
          delay:   The delay in seconds before the ToolTip appears(may be float)
          follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.wdgt = wdgt
        # The parent of the ToolTip is the parent of the ToolTips widget
        self.parent = self.wdgt.master
        # Initalise the Toplevel
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        # Hide initially
        self.withdraw()
        # The ToolTip Toplevel should have no frame or title bar
        self.overrideredirect(True)

        # The msgVar will contain the text displayed by the ToolTip
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        # The text of the ToolTip is displayed in a Message widget
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()

        # Add bindings to the widget.  This will NOT override
        # bindings that the widget already has
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        # The after function takes a time argument in miliseconds
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        """
        Processes motion within the widget.
        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        # If the follow flag is not set, motion within the
        # widget will make the ToolTip disappear
        #
        if self.follow is False:
            self.withdraw()
            self.visible = 1

        # Offset the ToolTip 10x10 pixes southwest of the pointer
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            # Try to call the message function.  Will not change
            # the message if the message function is None or
            # the message function fails
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()

# ===========================================================
#                   End of Class ToolTip
# ===========================================================

if __name__ == '__main__':
    vp_start_gui()
