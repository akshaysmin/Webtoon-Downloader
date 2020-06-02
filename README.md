# Webtoon-Downloader
What comic_download_header.py does:
Given url of a page of a webtoon comic,
  download all images in that page, 
  goes to next page, 
  continue this process till given no. of episodes/pages
Images are saved with appropriate names

What image_to_pdf.py does:
Creates pdf out of all images in given directory.

What sensible_sort.py does:
Assists script2 in sorting images by name

## README for webtoon_downloader.py:
Ways to use program from command line:
   python comic_download_header.py metafile #no_of_episodes taken from metafile\n
   python comic_download_header.py metafile no_of_episodes
   python comic_download_header.py metafile reset	               #resets all evolutions of metafile
   python comic_download_header.py current_episode_url  no_of_episodes  season_no  episode_no episode_index #direct input to main function
   NB: last one not recommended
Basic outline of program:
   {current episode url --> download all comic images --> get next episode url as url }*no_of_episodes --> evolve()
   evolve() -- changes global url, episode_no variables to next episode url,next episode no
   reset()   -- evolve to default/original values
NOTE:
   In case of KeyboardInterruption Error , program would not have evolved
---------Requirements---------
bs4, webbrowser, requests, time, sys, json
------------------------------

## README for image_to_pdf.py:
----------How to use----------
python image_to_pdf.py <imagefolder> <imageformat> <outfile>
selects all files in <imagefolder>\n with filenames ending with <imageformat>,\n sorts them alphanumerically and\n combine them to form a single pdf\n in the path <outfile>
NOTE:\n <imageformat> must be an image format\n <outfile> must end in .pdf
---------Requirements---------
PIL, os, sys
------------------------------
