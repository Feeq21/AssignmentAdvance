# import package
import labelme2coco

# set directory that contains labelme annotations and image files
labelme_folder = "D:/KOTOCLASS/secondmonth/cv-master/advanceworkbook/assignment28/classdata/pic2_json"

# set path for coco json to be saved
save_json_path = "D:/KOTOCLASS/secondmonth/cv-master/advanceworkbook/assignment28/classdata/pic2.json"

# convert labelme annotations to coco
labelme2coco.convert(labelme_folder, save_json_path)
