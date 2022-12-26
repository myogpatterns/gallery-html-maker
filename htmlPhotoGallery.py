#
# This script adds gallery and thumbs directories and copies lower res photos
# Outputs html in format for use on LearnMYOG.com
#
# <div class="gallery style1 small">
#     <article>
#         <a href="images/pulloverHoodie/1.JPG" class="image">
#             <img src="images/pulloverHoodie/thumbs/1.JPG" title="" loading="lazy" />
#         </a>
#     </article>
# </div>

#
#   Activate venv : source .venv/bin/activate
#
#   Place source jpgs into a jpg_path e.g. build
#   Copy output folder which includes gallery.html and directories to place in website images folder /project/build
#   Flip gall_path for build photos
#

import os
from PIL import Image

def htmlPhotoGallery(project, jpg_path, output):

    # site directories for images in gallery.html
    gall_path = "images/" + project + "build/"
    #gall_path = "images/" + project

    thumb_path = gall_path + "thumbs/"

    paths = sorted(os.listdir(jpg_path))
    
    #generate a list of inputs, then writelines(list)
    line_list = []

    div = '<div id = "build_gallery" style="display:none;" class="gallery style1 small">'
    line_list.append(div + '\n')
    
    for i in paths: 
        if i.endswith('.jpg'):
            print("working on "+i)

            item = (
                '\t' + '<article>'
                '\n\t\t' + '<a href="' + gall_path + i + '" class="image">'
                '\n\t\t' + '<img src="'+ thumb_path + i + '"' + ' title="Step ' + os.path.splitext(i)[0] + '"' + ' loading="lazy" />' + '</a>'
                '\n\t' + '</article>'
            )
            line_list.append(item + '\n')

            imageDrop(i, jpg_path, gall_path, thumb_path)
    line_list.append('</div>')

    hf = open(output, 'w')
    hf.writelines(line_list)
    hf.close()
    print(output,"created.")



def imageDrop(f, jpg_path, gall_path, thumb_path):
    with Image.open(jpg_path + f) as image:

        if not os.path.isdir(gall_path):
            os.makedirs(gall_path)
        if not os.path.isdir(thumb_path):
            os.makedirs(thumb_path)

        galsize = (800,2400)
        #gal = image.copy().resize(galsize)
        gal = image.copy()
        #thumbnail respects aspect ratio
        gal.thumbnail(galsize)
        thumbsize = (1200, 400)
        thumb = image.copy()
        #thumbnail respects aspect ratio for wide images
        thumb.thumbnail(thumbsize)

        gal.save(gall_path + f, "JPEG", quality="web_high")
        thumb.save(thumb_path + f, "JPEG", quality="web_high")



if __name__ == '__main__':
    htmlPhotoGallery(project='chonkysling/', jpg_path='imports/', output='gallery.html')