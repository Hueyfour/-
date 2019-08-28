#coding = utf-8

import tkinter as tk
from tkinter.ttk import Combobox
from tkinter.messagebox import *
from PIL import Image,ImageTk
import os


dataset_path = ""
image_size = (700,300)
_write = ""
_write1 = ""
image_file_path = ""
log_file_path = ""
label_file = {"真实人脸":"./labelStore/human.txt","姓名":"./labelStore/name.txt","身份证号":"./labelStore/ID.txt","性别":"./labelStore/gender.txt","年龄":"./labelStore/age.txt",
                "民族":"./labelStore/nationality.txt","种族":"./labelStore/race.txt","口罩":"./labelStore/mask.txt","帽子":"./labelStore/hat.txt","眼镜":"./labelStore/glasses.txt",
                "遮挡":"./labelStore/occulation.txt","光照":"./labelStore/illumination.txt","倾斜":"./labelStore/slope.txt","伤痕":"./labelStore/scar.txt","电话":"./labelStore/mobelephone.txt",
                "受伤":"./labelStore/injured.txt","饰品":"./labelStore/accessory.txt","人脸大小":"./labelStore/size.txt","模糊度":"./labelStore/blur.txt","面部表情":"./labelStore/expression.txt",
                "人脸出处":"./labelStore/sources.txt"}
finish_flag = True
StringVar = ""

window = tk.Tk()
window.title("dataset")
window.geometry("700x500")
#load= Image.open("/home/dataset/human_attribute/glassess/train/0/0_1000.jpg")
#load = load.resize((400,600))
#render = ImageTk.PhotoImage(load)
finish_flag = True
#attribute_label_list = [0] * 22
img_label = tk.Label(window)
img_label.place(x=0,y=0,anchor="nw")

path_label = tk.Label(window,text="打开文件夹")
path_label.place(x=30,y=310,anchor="nw")
path_entry = tk.Entry(window,width=50)
path_entry.place(x=110,y=310,anchor="nw")
path_entry.insert("end","/home/sfy/images_human/new_image/")

def load_img():
    #获取路径
    path = path_entry.get()
    if not os.path.exists(path) or not os.path.isdir(path):
        showinfo("提示","字符串非路径或者不存在该路径")
        return
    #print(path)
    #root为当前遍历文件夹，dirs为所有目录的列表，files为所有文件列表
    for root,_,files in os.walk(path):
        #print("111")
        dataset_path = root
        for file in files:
            #判断是否为jpg后缀
            if os.path.splitext(file)[1] == ".jpg":
                if not os.path.exists(os.path.join(dataset_path,file) + ".log"):
                    load = Image.open(os.path.join(dataset_path,file))
                    load = load.resize(image_size)
                    render = ImageTk.PhotoImage(load)
                    img_label.config(image=render)
                    img_label.image = render
                    global _write
                    _write = ""
                    _write += file
                
                    _write += " "
                    global image_file_path
                    global log_file_path
                    image_file_path = os.path.join(dataset_path,file)
                    log_file_path = image_file_path + ".log"
                    global finish_flag
                    finish_flag = False
                    return

        showinfo("info","No Unlabeled Images")
        return -1
path_button = tk.Button(window,text="load image",command = load_img)
path_button.place(x=500,y=310,anchor="nw")


label_label = tk.Label(window,text="属性选择")
label_label.place(x=45,y=340,anchor="nw")

def labelwork(StringVar):
    if StringVar == "真实人脸":
        isTureFace_label = tk.Label(window,text = "Human")
        isTureFace_label.place(x = 40,y = 400,anchor = "nw")
        trueFace_var = tk.IntVar()
        #def Trueface_select():
         #   global _write1
          #  print(trueFace_var.get())
           # _write1 = str(trueFace_var.get())
        def trueFace_select(event):
            global _write1
            print(trueFace_var.get() + int(event.char) - 1)
            _write1 = str(trueFace_var.get() + int(event.char) - 1)
        trueFace_radiobutton = tk.Radiobutton(window,text = "true face",variable = trueFace_var,value = 1)
        falseFace_radiobutton = tk.Radiobutton(window,text = "false face",variable = trueFace_var,value = 1)
        otherTypeFace_radiobutton = tk.Radiobutton(window,text = "other type face",variable = trueFace_var,value = 1)
        noFace_radiobutton = tk.Radiobutton(window,text = "no face",variable = trueFace_var,value = 1)
        trueFace_radiobutton.bind_all('<KeyPress-1>',trueFace_select)
        falseFace_radiobutton.bind_all('<KeyPress-2>',trueFace_select)
        otherTypeFace_radiobutton.bind_all('<KeyPress-3>',trueFace_select)
        noFace_radiobutton.bind_all('<KeyPress-4>',trueFace_select)
        trueFace_radiobutton.place(x = 100,y = 400,anchor = "nw")
        falseFace_radiobutton.place(x = 200,y = 400,anchor = "nw")
        otherTypeFace_radiobutton.place(x = 300,y= 400,anchor = "nw")
        noFace_radiobutton.place(x = 400,y = 400,anchor = "nw")

    elif StringVar == "姓名":
        name_label = tk.Label(window,text = "Name")
        name_label.place(x = 40,y = 400,anchor = "nw")
        nameEntry = tk.Entry(window,width=50)
        nameEntry.place(x=100,y=400,anchor="nw")
        def name_entry(event):
            global _write1
            print(nameEntry.get())
            _write1 = str(nameEntry.get())
        #submit_name_button = tk.Button(window,text = "SubmitName")
        nameEntry.bind_all('<Return>',name_entry)
        #submit_name_button.place(x = 600,y = 400,anchor = "nw")

    elif StringVar == "身份证号":
        #身份证号
        idNumber_label = tk.Label(window,text = "ID")
        idNumber_label.place(x = 40,y = 400,anchor = "nw")
        idNumberEntry = tk.Entry(window,width = 50)
        idNumberEntry.place(x = 100,y = 400,anchor = "nw")
        def id_entry():
            global _write1
            print(idNumberEntry.get())
            _write = str(idNumberEntry.get())
        #submit_idNumber_button = tk.Button(window,text = "SubmitID",command = id_entry)
        #submit_idNumber_button.place(x = 600,y = 400,anchor = "nw")
        idNumberEntry.bind_all('<Return>',id_entry)

    elif StringVar == "性别":
        gender_label = tk.Label(window,text="Gender")
        gender_label.place(x=40,y=400,anchor="nw")
        gender_var = tk.IntVar()
        def gender_select(event):
            global _write1
            print(gender_var.get() + int(event.char) - 1)
            _write1 = str(gender_var.get() + int(event.char) - 1)
        male_radiobutton = tk.Radiobutton(window,text="Male",variable=gender_var,value = 1)
        female_radiobutton = tk.Radiobutton(window,text="Female",variable=gender_var,value = 1)
        male_radiobutton.bind_all('<KeyPress-1>',gender_select)
        female_radiobutton.bind_all('<KeyPress-2>',gender_select)
        male_radiobutton.place(x=100,y=400,anchor="nw")
        female_radiobutton.place(x=200,y=400,anchor="nw")
        

    elif StringVar == "年龄":
        #年龄
        age_label = tk.Label(window,text="Age")
        age_label.place(x=40,y=400,anchor="nw")
        age_var = tk.IntVar()
        def age_select(event):
            global _write1
            print(age_var.get() + int(event.char) - 1)
            _write1 = str(age_var.get() + int(event.char) - 1)
        less_fourteen_radiobutton=tk.Radiobutton(window,text="0-14",variable=age_var,value=1)
        fifteen_twentyfour__radiobutton=tk.Radiobutton(window,text="15-24",variable=age_var,value=1)
        twentyfive_sixty_radiobutton = tk.Radiobutton(window,text="25-60",variable=age_var,value=1)
        greater_sixty_radiobutton = tk.Radiobutton(window,text=">60",variable=age_var,value = 1)
        less_fourteen_radiobutton.bind_all('<KeyPress-1>',age_select)
        fifteen_twentyfour__radiobutton.bind_all('<KeyPress-2>',age_select)
        twentyfive_sixty_radiobutton.bind_all('<KeyPress-3>',age_select)
        greater_sixty_radiobutton.bind_all('<KeyPress-4>',age_select)
        less_fourteen_radiobutton.place(x=100,y=400,anchor="nw")
        fifteen_twentyfour__radiobutton.place(x=200,y=400,anchor="nw")
        twentyfive_sixty_radiobutton.place(x=300,y=400,anchor="nw")
        greater_sixty_radiobutton.place(x=400,y=400,anchor="nw")

    elif StringVar == "民族":
        #民族
        nationality_label = tk.Label(window,text = "nationality")
        nationality_label.place(x = 40,y = 400,anchor = "nw")
        nationality_var = tk.StringVar()
        natioanality_select = Combobox(window,textvariable = nationality_var)
        natioanality_select['value'] = ("汉族","x族","y族")
        def storeNationality(event):
            global _write1
            print(natioanality_select.get())
            _write1 = str(natioanality_select.get())
        natioanality_select.bind("<<ComboboxSelected>>",storeNationality)
        natioanality_select.place(x = 150,y = 400,anchor = "nw")

    elif StringVar == "种族":
        #种族
        race_label = tk.Label(window,text = "Race")
        race_label.place(x = 40,y = 400,anchor = "nw")
        race_var = tk.IntVar()
        def race_select(event):
            global _write1
            print(race_var.get() + int(event.char) - 1)
            _write1 = str(race_var.get() + int(event.char) - 1)
        yellow_radiobutton = tk.Radiobutton(window,text="yellow",variable=race_var,value=1)
        white_radiobutton = tk.Radiobutton(window,text="white",variable=race_var,value=1)
        black_radiobutton = tk.Radiobutton(window,text="black",variable=race_var,value=1)
        brown_radiobutton = tk.Radiobutton(window,text="brown",variable=race_var,value=1)
        yellow_radiobutton.bind_all('<KeyPress-1>',race_select)
        white_radiobutton.bind_all('<KeyPress-2>',race_select)
        black_radiobutton.bind_all('<KeyPress-3>',race_select)
        brown_radiobutton.bind_all('<KeyPress-4>',race_select)
        yellow_radiobutton.place(x = 100,y = 400,anchor = "nw")
        white_radiobutton.place(x = 200,y = 400,anchor = "nw")
        black_radiobutton.place(x = 300,y = 400,anchor = "nw")
        brown_radiobutton.place(x = 400,y = 400,anchor = "nw")

    elif StringVar == "口罩":
        #是否有面罩
        mask_label = tk.Label(window,text="Mask")
        mask_label.place(x=40,y=400,anchor="nw")
        mask_var = tk.IntVar()
        def mask_select(event):
            global _write1
            print(mask_var.get() + int(event.char) - 1)
            _write1 = str(mask_var.get() + int(event.char) - 1)
        not_wearing_mask_radiobutton = tk.Radiobutton(window,text="Not Wearing",variable=mask_var,value=1)
        wearing_mask_radiobutton = tk.Radiobutton(window,text="Wearing",variable=mask_var,value=1)
        not_wearing_mask_radiobutton.bind_all('<KeyPress-1>',mask_select)
        wearing_mask_radiobutton.bind_all('<KeyPress-2>',mask_select)
        not_wearing_mask_radiobutton.place(x=100,y=400,anchor="nw")
        wearing_mask_radiobutton.place(x=200,y=400,anchor="nw")

    elif StringVar == "帽子":
        #是否有帽子
        hat_label = tk.Label(window,text="Hat")
        hat_label.place(x=40,y=400,anchor="nw")
        hat_var = tk.IntVar()
        def hat_select(event):
            global _write1
            print(hat_var.get() + int(event.char) - 1)
            _write1 = str(hat_var.get() + int(event.char) - 1)
        not_wearing_hat_radiobutton = tk.Radiobutton(window,text="Not Wearing",variable=hat_var,value=1)
        wearing_hat_radiobutton = tk.Radiobutton(window,text="Wearing",variable=hat_var,value=1)
        not_wearing_hat_radiobutton.bind_all('<KeyPress-1>',hat_select)
        wearing_hat_radiobutton.bind_all('<KeyPress-2>',hat_select)
        not_wearing_hat_radiobutton.place(x=100,y=400,anchor="nw")
        wearing_hat_radiobutton.place(x=200,y=400,anchor="nw")

    elif StringVar == "眼镜":
        #是否有眼镜
        glasses_label = tk.Label(window,text="Glasses")
        glasses_label.place(x=40,y=400,anchor="nw")
        glasses_var = tk.IntVar()
        def glasses_select(event):
            global _write1
            print(glasses_var.get() + int(event.char) - 1)
            _write1 = str(glasses_var.get() + int(event.char) - 1)
        not_wearing_glasses_radiobutton = tk.Radiobutton(window,text="Not Wearing",variable=glasses_var,value=1)
        wearing_glasses_radiobutton = tk.Radiobutton(window,text="Wearing",variable=glasses_var,value=1)
        not_wearing_glasses_radiobutton.bind_all('<KeyPress-1>',glasses_select)
        wearing_glasses_radiobutton.bind_all('<KeyPress-2>',glasses_select)
        not_wearing_glasses_radiobutton.place(x=100,y=400,anchor="nw")
        wearing_glasses_radiobutton.place(x=200,y=400,anchor="nw")

    elif StringVar == "遮挡":
        #遮挡
        occlusion_label = tk.Label(window,text = "Occlusion")
        occlusion_label.place(x = 40,y = 400,anchor = "nw")
        occlusion_var = tk.IntVar()
        def occlusion_select(event):
            global _write1
            print(occlusion_var.get() + int(event.char) - 1)
            _write1 = str(occlusion_var.get() + int(event.char) - 1)
        no_occlusion_radiobutton = tk.Radiobutton(window,text="No occlusion",variable=occlusion_var,value=1)
        acceptable_radiobutton = tk.Radiobutton(window,text="Acceptable",variable=occlusion_var,value=1)
        reluctantly_accepted_radiobutton = tk.Radiobutton(window,text="Reluctantly accepted",variable=occlusion_var,value = 1)
        unuseful_radiobutton = tk.Radiobutton(window,text="Unuseful",variable=occlusion_var,value=1)
        no_occlusion_radiobutton.bind_all('<KeyPress-1>',occlusion_select)
        acceptable_radiobutton.bind_all('<KeyPress-2>',occlusion_select)
        reluctantly_accepted_radiobutton.bind_all('<KeyPress-3>',occlusion_select)
        unuseful_radiobutton.bind_all('<KeyPress-4>',occlusion_select)
        no_occlusion_radiobutton.place(x = 100, y = 400,anchor = "nw")
        acceptable_radiobutton.place(x = 200,y = 400,anchor = "nw")
        reluctantly_accepted_radiobutton.place(x = 300,y = 400,anchor = "nw")
        unuseful_radiobutton.place(x = 400,y = 400,anchor = "nw")

    elif StringVar == "光照":
        #光照
        illumination_label = tk.Label(window,text = "Illumination")
        illumination_label.place(x = 40,y = 400,anchor = "nw")
        illumination_var = tk.IntVar()
        def illumination_select(event):
            global _write1
            print(illumination_var.get() + int(event.char) - 1)
            _write1 = str(illumination_var.get() + int(event.char) - 1)
        nomalIllumination_radiobutton = tk.Radiobutton(window,text="Normal",variable=illumination_var,value=1)
        backlight_radiobutton = tk.Radiobutton(window,text="Backlight",variable=illumination_var,value=1)
        stronglight_radiobutton = tk.Radiobutton(window,text="Stronglight",variable=illumination_var,value=1)
        darklight_radiobutton = tk.Radiobutton(window,text="Darklight",variable=illumination_var,value=1)
        nomalIllumination_radiobutton.bind_all('<KeyPress-1>',illumination_select)
        backlight_radiobutton.bind_all('<KeyPress-2>',illumination_select)
        darklight_radiobutton.bind_all('<KeyPress-4>',illumination_select)
        stronglight_radiobutton.bind_all('<KeyPress-3>',illumination_select)
        nomalIllumination_radiobutton.place(x = 100,y = 400,anchor = "nw")
        backlight_radiobutton.place(x = 200,y = 400,anchor = "nw")
        stronglight_radiobutton.place(x = 300,y = 400,anchor = "nw")
        darklight_radiobutton.place(x = 400,y = 400,anchor = "nw")

    elif StringVar == "倾斜":
        #倾斜
        slope_label = tk.Label(window,text = "Slope")
        slope_label.place(x = 40,y = 400,anchor = "nw")
        slope_var = tk.IntVar()
        def slope_select(event):
            global _write1
            print(slope_var.get() + int(event.char) - 1)
            _write1 = str(slope_var.get() + int(event.char) - 1)
        normalSlope_radiobutton = tk.Radiobutton(window,text="Normal",variable=slope_var,value=1)
        leftLeaning_radiobutton = tk.Radiobutton(window,text="Left leaning",variable=slope_var,value=1)
        rightLeaning_radiobutton = tk.Radiobutton(window,text="Right leaning",variable=slope_var,value=1)
        rise_radiobutton = tk.Radiobutton(window,text="Rise",variable=slope_var,value=1)
        bowDown_radiobutton = tk.Radiobutton(window,text="Bow down",variable=slope_var,value=1)
        normalSlope_radiobutton.bind_all('<KeyPress-1>',slope_select)
        leftLeaning_radiobutton.bind_all('<KeyPress-2>',slope_select)
        rightLeaning_radiobutton.bind_all('<KeyPress-3>',slope_select)
        rise_radiobutton.bind_all('<KeyPress-4>',slope_select)
        bowDown_radiobutton.bind_all('<KeyPress-5>',slope_select)
        normalSlope_radiobutton.place(x = 100,y = 400,anchor = "nw")
        leftLeaning_radiobutton.place(x = 200,y = 400,anchor = "nw")
        rightLeaning_radiobutton.place(x = 300,y = 400,anchor = "nw")
        rise_radiobutton.place(x = 400,y = 400,anchor = "nw")
        bowDown_radiobutton.place(x = 500,y = 400,anchor = "nw")

    elif StringVar == "伤痕":
        #伤痕    脸上是否带有肉眼可见伤痕
        scar_label = tk.Label(window,text = "Scar   脸上是否带有肉眼可见的伤痕")
        scar_label.place(x = 40,y = 370,anchor = "nw")
        scar_var = tk.IntVar()
        def scar_select(event):
            global _write1
            print(scar_var.get() + int(event.char) - 1)
            _write1 = str(scar_var.get() + int(event.char) - 1)
        isScar_radiobutton = tk.Radiobutton(window,text="Yes",variable=scar_var,value=1)
        isNotScar_radiobutton = tk.Radiobutton(window,text="No",variable=scar_var,value=1)
        isScar_radiobutton.bind_all('<KeyPress-1>',scar_select)
        isNotScar_radiobutton.bind_all('<KeyPress-2>',scar_select)
        isScar_radiobutton.place(x = 100,y = 400,anchor = "nw")
        isNotScar_radiobutton.place(x = 200,y = 400,anchor = "nw")

    elif StringVar == "电话":
        #电话   是否处于当电话状态
        phone_label = tk.Label(window,text = "Phone   是否处于打电话状态")
        phone_label.place(x = 40,y = 370,anchor = "nw")
        phone_var = tk.IntVar()
        def phone_select(event):
            global _write1
            print(phone_var.get() + int(event.char) - 1)
            _write1 = str(phone_var.get() + int(event.char) - 1)
        isPhone_radiobutton = tk.Radiobutton(window,text="Yes",variable=phone_var,value=1)
        isNotPhone_radiobutton = tk.Radiobutton(window,text="No",variable=phone_var,value=1)
        isPhone_radiobutton.bind_all('<KeyPress-1>',phone_select)
        isNotPhone_radiobutton.bind_all('<KeyPress-2>',phone_select)
        isPhone_radiobutton.place(x = 100,y = 400,anchor = "nw")
        isNotPhone_radiobutton.place(x = 200,y = 400,anchor = "nw")

    elif StringVar == "受伤":
        #受伤   是否面部带伤，需要包扎绷带的严重伤
        injured_label = tk.Label(window,text = "injured   是否面部带伤，需要包扎绷带的严重伤")
        injured_label.place(x = 40,y = 370,anchor = "nw")
        injured_var = tk.IntVar()
        def injured_select(event):
            global _write1
            print(injured_var.get() + int(event.char) - 1)
            _write1 = str(injured_var.get() + int(event.char) - 1)
        isInjured_radiobutton = tk.Radiobutton(window,text="Yes",variable=injured_var,value=1)
        isNotInjured_radiobutton = tk.Radiobutton(window,text="No",variable=injured_var,value=1)
        isInjured_radiobutton.bind_all('<KeyPress-1>',injured_select)
        isNotInjured_radiobutton.bind_all('<KeyPress-2>',injured_select)
        isInjured_radiobutton.place(x = 100,y = 400,anchor = "nw")
        isNotInjured_radiobutton.place(x = 200,y = 400,anchor = "nw")

    elif StringVar == "饰品":
        #饰品   是否有鼻环唇环耳环等装饰物
        accessory_label = tk.Label(window,text = "Accessory   是否有鼻环唇环耳环等装饰物")
        accessory_label.place(x = 40,y = 370,anchor = "nw")
        accessory_var = tk.IntVar()
        def accessory_select(event):
            global _write1
            print(accessory_var.get() + int(event.char) - 1)
            _write1 = str(accessory_var.get() + int(event.char) - 1)
        isAccessory_radiobutton = tk.Radiobutton(window,text="Yes",variable=accessory_var,value=1)
        isNotAccessory_radiobutton = tk.Radiobutton(window,text="No",variable=accessory_var,value=1)
        isAccessory_radiobutton.bind_all('<KeyPress-1>',accessory_select)
        isNotAccessory_radiobutton.bind_all('<KeyPress-2>',accessory_select)
        isAccessory_radiobutton.place(x = 100,y = 400,anchor = "nw")
        isNotAccessory_radiobutton.place(x = 200,y = 400,anchor = "nw")

    elif StringVar =="人脸大小":
        #人脸大小   size 50以下的小人脸可用价值不大，一般较为模糊
        faceSize_label = tk.Label(window,text = "Face size    50以下的小人脸可用价值不大，一般较为模糊")
        faceSize_label.place(x = 40,y = 370,anchor = "nw")
        faceSize_var = tk.IntVar()
        def faceSize_select(event):
            global _write1
            print(faceSize_var.get() + int(event.char) - 1)
            _write1 = str(faceSize_var.get() + int(event.char) - 1)
        greater100_radiobutton = tk.Radiobutton(window,text=">100",variable=faceSize_var,value=1)
        smaller100greater50_radiobutton = tk.Radiobutton(window,text="<100&&>50",variable=faceSize_var,value=1)
        smaller50_radiobutton = tk.Radiobutton(window,text="<50",variable=faceSize_var,value=1)
        greater100_radiobutton.bind_all('<KeyPress-1>',faceSize_select)
        smaller100greater50_radiobutton.bind_all('<KeyPress-2>',faceSize_select)
        smaller50_radiobutton.bind_all('<KeyPress-3>',faceSize_select)
        greater100_radiobutton.place(x = 100,y = 400,anchor = "nw")
        smaller100greater50_radiobutton.place(x = 200,y = 400,anchor = "nw")
        smaller50_radiobutton.place(x = 300,y = 400,anchor = "nw")

    elif StringVar == "模糊度":
        #模糊度
        blur_label = tk.Label(window,text = "Blur")
        blur_label.place(x = 40,y = 400,anchor = "nw")
        blur_var = tk.IntVar()
        def blur_select(event):
            global _write1
            print(blur_var.get() + int(event.char) - 1)
            _write1 = str(blur_var.get() + int(event.char) - 1)
        clear_radiobutton = tk.Radiobutton(window,text="Clear",variable=blur_var,value=1)
        blurLowResolution_radiobutton = tk.Radiobutton(window,text="Blur low resolution",variable=blur_var,value=1)
        blurOutOfFocus_radiobutton = tk.Radiobutton(window,text="Blur out of focus",variable=blur_var,value=1)
        blurDistortion_radiobutton = tk.Radiobutton(window,text="Distortion blur",variable=blur_var,value=1)
        clear_radiobutton.bind_all('<KeyPress-1>',blur_select)
        blurLowResolution_radiobutton.bind_all('<KeyPress-2>',blur_select)
        blurOutOfFocus_radiobutton.bind_all('<KeyPress-3>',blur_select)
        blurDistortion_radiobutton.bind_all('<KeyPress-4>',blur_select)
        clear_radiobutton.place(x = 100,y = 400,anchor = "nw")
        blurLowResolution_radiobutton.place(x = 200,y = 400,anchor = "nw")
        blurOutOfFocus_radiobutton.place(x = 300,y = 400,anchor = "nw")
        blurDistortion_radiobutton.place(x = 400,y = 400,anchor = "nw")

    elif StringVar == "面部表情":
        #面部表情
        expression_label = tk.Label(window,text = "Expression")
        expression_label.place(x = 40,y = 400,anchor = "nw")
        expression_var = tk.IntVar()
        def expression_select(event):
            global _write1
            print(expression_var.get() + int(event.char) - 1)
            _write1 = str(expression_var.get() + int(event.char) - 1)
        happy_radiobutton = tk.Radiobutton(window,text="Happy",variable=expression_var,value=1)
        normalExpression_radiobutton = tk.Radiobutton(window,text="Normal",variable=expression_var,value=1)
        sad_radiobutton = tk.Radiobutton(window,text="Sad",variable=expression_var,value=1)
        surprise_radiobutton = tk.Radiobutton(window,text="Surprise",variable=expression_var,value=1)
        happy_radiobutton.bind_all('<KeyPress-1>',expression_select)
        normalExpression_radiobutton.bind_all('<KeyPress-2>',expression_select)
        sad_radiobutton.bind_all('<KeyPress-3>',expression_select)
        surprise_radiobutton.bind_all('<KeyPress-4>',expression_select)
        happy_radiobutton.place(x = 100,y = 400,anchor = "nw")
        normalExpression_radiobutton.place(x = 200,y = 400,anchor = "nw")
        sad_radiobutton.place(x = 300,y = 400,anchor = "nw")
        surprise_radiobutton.place(x = 400,y = 400,anchor = "nw")

    elif StringVar == "人脸出处":
        #人脸出处
        source_label = tk.Label(window,text = "Source")
        source_label.place(x = 40,y = 400,anchor = "nw")
        source_var = tk.IntVar()
        def source_select(event):
            global _write1
            print(source_var.get() + int(event.char) - 1)
            _write1 = str(source_var.get() + int(event.char) - 1)
        picture_radiobutton = tk.Radiobutton(window,text="Picture",variable=source_var,value=1)
        camera_radiobutton = tk.Radiobutton(window,text="Camera",variable=source_var,value=1)
        video_radiobutton = tk.Radiobutton(window,text="Video",variable = source_var,value=1)
        picture_radiobutton.bind_all('<KeyPress-1>',source_select)
        camera_radiobutton.bind_all('<KeyPress-2>',source_select)
        video_radiobutton.bind_all('<KeyPress-3>',source_select)
        picture_radiobutton.place(x = 100,y = 400,anchor = "nw")
        camera_radiobutton.place(x = 200,y = 400,anchor = "nw")
        video_radiobutton.place(x = 300,y = 400,anchor = "nw")


def openLabelFile(event):
    print(label_select.get())
    global StringVar
    StringVar = label_select.get()
    labelwork(StringVar)
    global fileOpen
    fileOpen = open(label_file[StringVar],'a')
label_var = tk.StringVar()
label_select = Combobox(window,textvariable = label_var)
label_select["value"] = ("真实人脸","姓名","身份证号","性别","年龄","民族","种族","口罩","帽子","眼镜","遮挡","光照","倾斜","伤痕","电话","受伤","饰品","人脸大小","模糊度","面部表情","人脸出处")
label_select["state"] = "readonly"
label_select.place(x = 110,y = 340,anchor = "nw")
label_select.bind('<<ComboboxSelected>>',openLabelFile)



def delete_img(event):
    print("delete image")
    global finish_flag
    if finish_flag:
        showinfo("Info","No Unlabeled Images")
    else: 
        os.remove(image_file_path)
        if -1 == load_img():
            
            finish_flag = True

delete_button = tk.Button(window,text="Delete Image",command = delete_img)
delete_button.place(x=150,y=450,anchor="nw")
delete_button.bind_all('<KeyPress-Delete>',delete_button)

def next_img(event):
    print("next image")
    global finish_flag
    global _write,_write1
    global fileOpen
    if finish_flag:
        showinfo("Info","No Unlabeled Images")
    else:
        fileOpen.write(_write + " " + _write1 + "\n")
        log_file = open(log_file_path,"w")
        log_file.write("111")
        log_file.close()
        _write = ""
        _write1 = ""
        if -1 == load_img():
            
            finish_flag = True
    #print write_line
next_button = tk.Button(window,text="Next Image",command = next_img)
next_button.place(x=350,y=450,anchor="nw")
next_button.bind_all('<KeyPress-Right>',next_img)

window.mainloop()
fileOpen.close()