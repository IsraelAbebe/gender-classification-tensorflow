import os
import csv
import numpy as np
import random
import cv2


def facecrop(image):
    facedata = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(facedata)

    img = cv2.imread(image)

    minisize = (img.shape[1], img.shape[0])
    miniframe = cv2.resize(img, minisize)

    faces = cascade.detectMultiScale(miniframe)

    for f in faces:
        x, y, w, h = [v for v in f]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255))

        sub_face = img[y:y + h, x:x + w]
        print "facecrop" + str(sub_face.shape)
        os.remove(image)
        cv2.imwrite(image, sub_face)

    return


def read_through(dirname):
    '''
    :param param: folder where the data is in
    :param file_name: the name of the image
    :return: number that represents a class that image represents given file name and csv that contains the data
    '''
    count = 0
    countm = 0
    countf = 0
    for cur, _dirs, files in os.walk(dirname):
        head, tail = os.path.split(cur)
        while head:
            head, _tail = os.path.split(head)
        for f in files:
            if ".JPG" in f:
                file_path = dirname + "/" + tail + "/" + f
                print f,file_path
                count += 1
                # img = cv2.imread(file_path)
                facecrop(file_path)


            # file_path = dirname+"/"+tail+"/"+f
            # filename = f.replace("coarse_tilt_aligned_face.", "")
            #
            # idnum = filename[:filename.find(".")]
            # filename = filename[filename.find(".")+1:]
            # sex = get_sex(tail,filename,idnum)
            # if sex is None:
            # 	continue
            # print file_path,sex
            # # facecrop(file_path)
            # img = cv2.imread(file_path)
            # if img is None :
            # 	continue
            # print img
            # if sex.lower() == 'm' and countm <=5000:
            # 	i = cv2.imwrite("./data/genderdata/train/m/"+f,img)
            # 	print i
            # 	countm += 1
            # elif sex.lower() =='f'and countm <=5000:
            # 	i = cv2.imwrite("./data/genderdata/train/f/"+f,img)
            # 	print i
            # 	countf += 1
            # elif sex.lower() =='f'and countm >5000:
            # 	i = cv2.imwrite("./data/genderdata/test/f/"+f,img)
            # 	print i
            # 	countf += 1
            # elif sex.lower() == 'm' and countm >5000:
            # 	i = cv2.imwrite("./data/genderdata/test/m/"+f,img)
            # 	print i
            # 	countm += 1

    print count


def get_sex(foldername, filename, idnum):
    for cur, _dirs, files in os.walk('./data/class_label'):
        head, tail = os.path.split(cur)

        while head:
            head, _tail = os.path.split(head)
        for f in files:
            if ".csv" in f:
                file_path = './data' + "/" + tail + "/" + f
                train_data = list(csv.reader(open(file_path), delimiter='\t'))
                for i in train_data:
                    if foldername == i[0] and filename == i[1] and idnum == i[2]:
                        return i[4]


read_through('./data/KDEF')
# facecrop('./data/hey.jpg')
# get_sex('100014826@N03', '9478897989_a9b483d9c1_o.jpg', '463')
