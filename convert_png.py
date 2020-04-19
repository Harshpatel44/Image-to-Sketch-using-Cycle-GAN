from PIL import Image
import glob2
import sys


#conversion for gif to png

def processImage(infile):
    print(infile)
    try:
        im = Image.open(infile)
        print(im)
    except IOError:
        print("Cant load", infile)
        sys.exit(1)
    i = 0
    mypalette = im.getpalette()

    try:
        while 1:
            print(mypalette)
            im.putpalette(mypalette)
            new_im = Image.new("RGBA", im.size)
            new_im.paste(im)
            new_im.save('png/'+(infile.split('.')[-2]).split('\\')[-1]+'.png')

            i += 1
            im.seek(im.tell() + 1)

    except EOFError:
        pass # end of sequence



files=glob2.glob('dataset/*')
print(files)
for i in files:
    print(('png/'+i.split('.')[-2]).split('\\')[-1])
    Image.open(i).convert('RGB').save('png_data/'+(i.split('.')[-2]).split('\\')[-1]+'.png')
