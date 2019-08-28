#!/usr/bin/env python
# coding=utf-8

import Tkinter as tk
from tkMessageBox import *
from PIL import Image,ImageTk
import os

dataset_path = ""
image_size = (200,600)
write_line = ""
image_file_path = ""
log_file_path = ""
attribute_label_list = [0] * 9 
finish_flag = True

label_file = open("./label.txt","a")

window = tk.Tk()
window.title("dataset")
window.geometry("1000x600")
#load= Image.open("/home/dataset/human_attribute/glassess/train/0/0_1000.jpg")
#load = load.resize((400,600))
#render = ImageTk.PhotoImage(load)
img_label = tk.Label(window)
img_label.place(x=100,y=0,anchor="nw")

path_label = tk.Label(window,text="Path").place(x=410,y=0,anchor="nw")
path_entry = tk.Entry(window,width=50)
path_entry.place(x=450,y=0,anchor="nw")
path_entry.insert("end","/home/sfy/images_human/new_image/")

def load_img():
    path = path_entry.get()
    if not os.path.exists(path) or not os.path.isdir(path):
        showinfo("提示","字符串非路径或者不存在该路径")
        return
    #print(path)
    for root,dirs,files in os.walk(path):
        #print("111")
        dataset_path = root
        for file in files:
            if os.path.splitext(file)[1] == ".jpg":
                if not os.path.exists(os.path.join(root,file) + ".log"):
                    load = Image.open(os.path.join(root,file))
                    load = load.resize(image_size)
                    render = ImageTk.PhotoImage(load)
                    img_label.config(image=render)
                    img_label.image = render
                    global write_line
                    write_line = ""
                    write_line += file
                    global image_file_path
                    global log_file_path
                    image_file_path = os.path.join(root,file)
                    log_file_path = image_file_path + ".log"
                    global finish_flag
                    finish_flag = False
                    return

        showinfo("info","No Unlabeled Images")
        return -1
path_button = tk.Button(window,text="load image",command = load_img).place(x=900,y=0,anchor="nw")

label_label = tk.Label(window,text="Label")
label_label.place(x=410,y=50,anchor="nw")

age_label = tk.Label(window,text="Age")
age_label.place(x=450,y=100,anchor="nw")
age_var = tk.IntVar()
def age_select():
    print(age_var.get())
    attribute_label_list[0] = age_var.get()
less_eighteen_radiobutton=tk.Radiobutton(window,text="0-18",variable=age_var,value=0,command=age_select)
eighteen_sixty__radiobutton=tk.Radiobutton(window,text="18-35",variable=age_var,value=1,command=age_select)
greater_sixty_radiobutton = tk.Radiobutton(window,text="35-60",variable=age_var,value=2,command = age_select)
age_unknown_radiobutton = tk.Radiobutton(window,text=">60",variable=age_var,value = 3,command = age_select)
less_eighteen_radiobutton.place(x=550,y=100,anchor="nw")
eighteen_sixty__radiobutton.place(x=650,y=100,anchor="nw")
greater_sixty_radiobutton.place(x=750,y=100,anchor="nw")
age_unknown_radiobutton.place(x=850,y=100,anchor="nw")

gender_label = tk.Label(window,text="Gender")
gender_label.place(x=450,y=130,anchor="nw")
gender_var = tk.IntVar()
def gender_select():
    print(gender_var.get())
    attribute_label_list[1] = gender_var.get()
male_radiobutton = tk.Radiobutton(window,text="Male",variable=gender_var,value=0,command = gender_select)
female_radiobutton = tk.Radiobutton(window,text="Female",variable=gender_var,value=1,command = gender_select)
#gender_unknown_radiobutton = tk.Radiobutton(window,text="Unknown",variable=gender_var,value=2,command = gender_select)
male_radiobutton.place(x=550,y=130,anchor="nw")
female_radiobutton.place(x=650,y=130,anchor="nw")
#gender_unknown_radiobutton.place(x=750,y=130,anchor="nw")



glasses_label = tk.Label(window,text="Glasses")
glasses_label.place(x=450,y=160,anchor="nw")
glasses_var = tk.IntVar()
def glasses_select():
    print(glasses_var.get())
    attribute_label_list[2] = glasses_var.get()
not_wearing_glasses_radiobutton = tk.Radiobutton(window,text="Not Wearing",variable=glasses_var,value=0,command = glasses_select)
wearing_glasses_radiobutton = tk.Radiobutton(window,text="Wearing",variable=glasses_var,value=1,command = glasses_select)
glasses_unknown_radiobutton = tk.Radiobutton(window,text="Unknown",variable=glasses_var,value=2,command = glasses_select)
not_wearing_glasses_radiobutton.place(x=550,y=160,anchor="nw")
wearing_glasses_radiobutton.place(x=650,y=160,anchor="nw")
glasses_unknown_radiobutton.place(x=750,y=160,anchor="nw")

hat_label = tk.Label(window,text="Hat")
hat_label.place(x=450,y=190,anchor="nw")
hat_var = tk.IntVar()
def hat_select():
    print(hat_var.get())
    attribute_label_list[3] = hat_var.get()
not_wearing_hat_radiobutton = tk.Radiobutton(window,text="Not Wearing",variable=hat_var,value=0,command = hat_select)
wearing_hat_radiobutton = tk.Radiobutton(window,text="Wearing",variable=hat_var,value=1,command = hat_select)
#hat_unknown_radiobutton = tk.Radiobutton(window,text="Unknown",variable=hat_var,value=2,command= hat_select)
not_wearing_hat_radiobutton.place(x=550,y=190,anchor="nw")
wearing_hat_radiobutton.place(x=650,y=190,anchor="nw")
#hat_unknown_radiobutton.place(x=750,y=190,anchor="nw")

mask_label = tk.Label(window,text="Mask")
mask_label.place(x=450,y=220,anchor="nw")
mask_var = tk.IntVar()
def mask_select():
    print(mask_var.get())
    attribute_label_list[4] = mask_var.get()
not_wearing_mask_radiobutton = tk.Radiobutton(window,text="Not Wearing",variable=mask_var,value=0,command = mask_select)
wearing_mask_radiobutton = tk.Radiobutton(window,text="Wearing",variable=mask_var,value=1,command = mask_select)
mask_unknown_radiobutton = tk.Radiobutton(window,text="Unknown",variable=mask_var,value=2,command = mask_select)
not_wearing_mask_radiobutton.place(x=550,y=220,anchor="nw")
wearing_mask_radiobutton.place(x=650,y=220,anchor="nw")
mask_unknown_radiobutton.place(x=750,y=220,anchor="nw")

#hair_label = tk.Label(window,text="Hair")
#hair_label.place(x=450,y=250,anchor="nw")
#hair_var = tk.IntVar()
#def hair_select():
#    print(hair_var.get())
#    attribute_label_list[5] = hair_var.get()
#hair_short_radiobutton = tk.Radiobutton(window,text="Short",variable=hair_var,value=0,command = hair_select)
#hair_long_radiobutton = tk.Radiobutton(window,text="Long",variable=hair_var,value=1,command = hair_select)
#hair_unknown_radiobutton = tk.Radiobutton(window,text="Unknown",variable=hair_var,value=2,command = hair_select)
#hair_short_radiobutton.place(x=550,y=250,anchor="nw")
#hair_long_radiobutton.place(x=650,y=250,anchor="nw")
#hair_unknown_radiobutton.place(x=750,y=250,anchor="nw")

upper_body_label = tk.Label(window,text="UpperBody")
upper_body_label.place(x=450,y=250,anchor="nw")
upper_body_var = tk.IntVar()
def upper_body_select():
    print(upper_body_var.get())
    attribute_label_list[5] = upper_body_var.get()
short_shirt_radiobutton = tk.Radiobutton(window,text="Short Shirt",variable=upper_body_var,value=0,command = upper_body_select)
long_shirt_radiobutton = tk.Radiobutton(window,text="Long Shirt",variable=upper_body_var,value=1,command = upper_body_select)
jacket_raddiobutton = tk.Radiobutton(window,text="Jacket",variable=upper_body_var,value=2,command = upper_body_select)
sweater_raddiobutton = tk.Radiobutton(window,text="Sweater",variable=upper_body_var,value=3,command = upper_body_select)
cotton_coat_raddiobutton = tk.Radiobutton(window,text="Cotton Coat",variable=upper_body_var,value=4,command = upper_body_select)
short_shirt_radiobutton.place(x=550,y=250,anchor="nw")
long_shirt_radiobutton.place(x=650,y=250,anchor="nw")
jacket_raddiobutton.place(x=750,y=250,anchor = "nw")
sweater_raddiobutton.place(x=850,y=250,anchor = "nw")
cotton_coat_raddiobutton.place(x=550,y=280,anchor="nw")

lower_body_label = tk.Label(window,text="LowerBody")
lower_body_label.place(x=450,y=310,anchor="nw")
lower_body_var = tk.IntVar()
def lower_body_select():
    print(lower_body_var.get())
    attribute_label_list[6] = lower_body_var.get()
trousers_radiobutton = tk.Radiobutton(window,text="Trousers",variable=lower_body_var,value=0,command = lower_body_select)
shorts_radiobutton = tk.Radiobutton(window,text="Shorts",variable=lower_body_var,value=1,command = lower_body_select)
skirts_radiobutton = tk.Radiobutton(window,text="Skirts",variable=lower_body_var,value=2,command = lower_body_select)
trousers_radiobutton.place(x=550,y=310,anchor="nw")
shorts_radiobutton.place(x=650,y=310,anchor="nw")
skirts_radiobutton.place(x=750,y=310,anchor="nw")


facing_label = tk.Label(window,text="Facing")
facing_label.place(x=450,y=340,anchor="nw")
facing_var = tk.IntVar()
def facing_select():
    print(facing_var.get())
    attribute_label_list[7] = facing_var.get()
front_radiobutton = tk.Radiobutton(window,text="Front",variable=facing_var,value=0,command = facing_select)
side_radiobutton = tk.Radiobutton(window,text="Side",variable=facing_var,value=1,command = facing_select)
back_radiobutton = tk.Radiobutton(window,text="Back",variable=facing_var,value=2,command = facing_select)
front_radiobutton.place(x=550,y=340,anchor="nw")
side_radiobutton.place(x=650,y=340,anchor="nw")
back_radiobutton.place(x=750,y=340,anchor="nw")

carrying_items_label = tk.Label(window,text="Carrying Items")
carrying_items_label.place(x=450,y=370,anchor="nw")
carrying_items_var = tk.IntVar()
def carrying_items_select():
    print(carrying_items_var.get())
    attribute_label_list[8] = carrying_items_var.get()
backpack_radiobutton = tk.Radiobutton(window,text="Backpack",variable=carrying_items_var,value=0,command = carrying_items_select)
shoulder_bag_radiobutton = tk.Radiobutton(window,text="Shoulder Bag",variable=carrying_items_var,value=1,command = carrying_items_select)
handbag_radiobutton = tk.Radiobutton(window,text="Handbag",variable=carrying_items_var,value=2,command = carrying_items_select)
carrying_items_unknown_radiobutton = tk.Radiobutton(window,text="Unknown",variable=carrying_items_var,value=3,command = carrying_items_select)
backpack_radiobutton.place(x=550,y=370,anchor="nw")
shoulder_bag_radiobutton.place(x=650,y=370,anchor="nw")
handbag_radiobutton.place(x=750,y=370,anchor="nw")
carrying_items_unknown_radiobutton.place(x=850,y=370,anchor="nw")

def delete_img():
    print("delete image")
    if finish_flag:
        showinfo("Info","No Unlabeled Images")
    else: 
        os.remove(image_file_path)
        if -1 == load_img():
            global finish_flag
            finish_flag = True

delete_button = tk.Button(window,text="Delete Image",command = delete_img)
delete_button.place(x=550,y=500,anchor="nw")
def next_img():
    print("next image")
    global write_line
    if finish_flag:
        showinfo("Info","No Unlabeled Images")
    else:
        for i in attribute_label_list:
            write_line += " "
            write_line += str(i)
        write_line += "\n"
        label_file.write(write_line)
        log_file = open(log_file_path,"w")
        log_file.write("111")
        log_file.close()
        write_line = ""
        if -1 == load_img():
            global finish_flag 
            finish_flag = True
    #print write_line
next_button = tk.Button(window,text="Next Image",command = next_img)
next_button.place(x=750,y=500,anchor="nw")
window.mainloop()

