print('----------How to use----------')
print('python image_to_pdf.py <imagefolder> <imageformat> <outfile>')
print('selects all files in <imagefolder>\n with filenames ending with <imageformat>,\n sorts them alphanumerically and\n combine them to form a single pdf\n in the path <outfile>')
print('NOTE:\n <imageformat> must be an image format\n <outfile> must end in .pdf')
print('---------Requirements---------')
print('PIL,os,sys')
print('------------------------------')

import time
start_time=time.time()

from PIL import Image
from sensible_sort import sensible_sort
import sys
import os


if len(sys.argv)==4:
	folder = sys.argv[1]
	file_format = sys.argv[2]
	out_file = sys.argv[3]
else:
	print('Improper usage, please read How to use')
	sys.exit()

os.chdir(folder)
imglist = [imgname for imgname in os.listdir() if imgname.endswith(file_format)]
print('found ',len(imglist),' images\n sorting by name..')

imglist = sensible_sort(imglist)
print('sorted !\n opening and converting images..')

imglist_pil = []
for i,img in enumerate(imglist):
	imglist_pil.append(Image.open(img).convert('RGB'))
	if i%50==0:
		print(i)

print('images ready!\n creating pdf file..')
imglist_pil[0].save(out_file,save_all=True,append_images=imglist_pil[1:])

end_time = time.time()
print(' Done :) in',end_time-start_time,'seconds')