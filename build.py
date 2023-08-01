# Copyright 2023 Sascha Willems
# SPDX-License-Identifier: Apache-2.0

# Convert Vulkan Samples documentation into an Antora project

import shutil
import os

# Copy files into the structure expected by an Antora module

SAMPLES_ROOT = "../samples"
ANTORA_ROOT = "modules/ROOT"

def convert_folder(folder_name):
    dst_folder = ANTORA_ROOT + "/pages/" + folder_name
    dst_image_folder = ANTORA_ROOT + "/images/" + folder_name
    src_folder = SAMPLES_ROOT + "/" + folder_name
    os.makedirs(dst_folder, 0o777, True)
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            # Docs
            if (file.endswith(".adoc")):                
                dst_sub_folder = dst_folder + "/" + os.path.basename(root)
                if os.path.basename(root) == folder_name:
                    shutil.copy(os.path.join(root, file), dst_folder + "/" + file)
                else:
                    os.makedirs(dst_sub_folder, 0o777, True)
                    shutil.copy(os.path.join(root, file), dst_sub_folder + "/" + file)
                    # We need to add the image folder to the doc to match how Antora expects images to be stored
                    with open(dst_sub_folder + "/" + file, "r+") as f:
                        s = f.read()
                        f.seek(0)
                        f.write(":images: " + root.replace("../samples/", "") + "\n" + s)
                        f.close()
            # Antora requires images to be in a predefined folder, which clashes with how images are stored in the repo (besides the docs)                    
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):                
                dst_image_sub_folder = ANTORA_ROOT + "/images/" + root.replace("../samples/", "")
                # print(os.path.join(root, file))
                # print(root.replace("../samples/", ""))
                os.makedirs(dst_image_sub_folder, 0o777, True)
                shutil.copy(os.path.join(root, file), dst_image_sub_folder + "/" + file)
 
convert_folder("api")
convert_folder("extensions")
convert_folder("performance")
convert_folder("tooling")