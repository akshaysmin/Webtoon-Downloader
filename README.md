# Webtoon-Downloader</br>

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

## README for webtoon_downloader.py:</br>

Ways to use program from command line:</br>
   python comic_download_header.py metafile #no_of_episodes taken from metafile</br>
   python comic_download_header.py metafile no_of_episodes</br>
   python comic_download_header.py metafile reset	               #resets all evolutions of metafile</br>
   python comic_download_header.py current_episode_url  no_of_episodes  season_no  episode_no episode_index #direct input to main function</br>
   NB: last one not recommended</br>
Basic outline of program:</br>
   {current episode url --> download all comic images --> get next episode url as url }*no_of_episodes --> evolve()</br>
   evolve() -- changes global url, episode_no variables to next episode url,next episode no</br>
   reset()   -- evolve to default/original values</br>
NOTE:</br>
   In case of KeyboardInterruption Error , program would not have evolved</br>
### Requirements</br>
bs4, webbrowser, requests, time, sys, json</br>
------------------------------</br>

## README for image_to_pdf.py:</br>

----------How to use----------</br>
python image_to_pdf.py imagefolder imageformat outfile</br>
selects all files in imagefolder</br> with filenames ending with imageformat,</br> sorts them alphanumerically and</br> combine them to form a single pdf</br> in the path outfile</br>
NOTE:</br> imageformat must be an image format</br> outfile must end in .pdf</br>
### Requirements</br>
PIL, os, sys</br>
------------------------------</br>
