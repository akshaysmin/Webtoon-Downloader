from bs4 import BeautifulSoup
import webbrowser,requests,time,sys
import json


#these will be used only in case 3 of command line usage only if arguments are not properly provided
url0='https://www.webtoons.com/en/fantasy/tower-of-god/season-1-ep-0/viewer?title_no=95&episode_no=1'
url="https://www.webtoons.com/en/challenge/hafu/character-profiles/viewer?title_no=155881&episode_no=3"
en=2
sn=1
img_index=2
ne=2
u,e=url,en


display_text='''
Ways to use program from command line:
   python comic_download_header.py metafile #no_of_episodes taken from metafile
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
'''
print(display_text)

def replace_line(file_name, line_num, text):
   line_num-=1
   text+='\n'
   lines = open(file_name, 'r').readlines()
   lines[line_num] = text
   out = open(file_name, 'w')
   out.writelines(lines)
   out.close()
   return None

def evolve(u,e,s,imi):
	meta["current"]["start_url"] = u
	meta["current"]["episode_num"] = e
	meta["current"]["season_num"] = s
	meta["current"]["img_num"] = imi
	with open(metafile, "w") as f:
	    json.dump(meta,f)
	return None

def seconds2clock(t):
	#returns [hr,min,sec]
	return [(t//60)//60,(t//60)%60,t%60]

def reset():
	meta["current"] = meta["default"]
	with open(metafile, "w") as f:
	    json.dump(meta,f)

def save_comic_episodes(url, ne, sn ,en,img_index):
	'''
	next_episode_url=func(current_episode_url, no_of_episodes, season_no ,episode_no)
	saves all images from current episode to total of given no. of episodes
	'''
	print('url : ',url,'\nno. of episodes : ',ne,'\nseason no. : ',sn,'\nepisode no. : ',en,'\nimage no. : ',img_index)
	t1=time.time()
	session = requests.Session()																					#create Session obj
	for i in range(ne):
		r=session.get(url)
		print('---------------------------%s/%s--------------------------'%(i+1,ne))
		print('accesing comic episode\n',url)
		print(r)
		session.headers['referer']=url																			#set optional header 'referer' as url of original page
		print('Session_obj.headers = \n',session.headers)
		
		soup=BeautifulSoup(r.text, features='lxml')
		img_lst=soup.find_all('div',id='_imageList')[0].find_all('img')
		
		for i,img in enumerate(img_lst):
			img_url=img['data-url']
			response = session.get(img_url)
			with open('im%ss%se%s_%s.jpg'%(img_index,sn,en,i),'wb') as f:
				f.write(response.content)
		
		#under dev
		if sn==1 and en==79:
			en=0
			sn=2
		elif sn==2 and en==337:
			en=1
			sn=3
		else:
			en+=1
		url=soup.find_all('a',title='Next Episode')[0]['href']
		img_index += 1
	evolve(url, en, sn,img_index)
	t2=time.time()
	print('time taken for downloading %s episodes, [hr,min,sec] = '%(ne),seconds2clock(t2-t1))
	return url,en,sn,img_index

if __name__=="__main__":
	#run from commandline - interface
	if len(sys.argv)==2:
		metafile = sys.argv[1]
		with open(metafile) as f:
			meta = json.load(f)
			meta_current = meta['current']
		url, ne, sn ,en,img_index = meta_current["start_url"], meta_current["max_episode_num"], meta_current["season_num"], meta_current["episode_num"], meta_current["img_num"]
		u,e,s,imi=save_comic_episodes(url, ne, sn ,en,img_index)
	elif len(sys.argv)==3:
		metafile = sys.argv[1]
		with open(metafile) as f:
			meta = json.load(f)
			meta_current = meta['current']
		url, ne, sn ,en,img_index = meta_current["start_url"], meta_current["max_episode_num"], meta_current["season_num"], meta_current["episode_num"], meta_current["img_num"]
		no_reset=True
		try:
			ne=int(sys.argv[2])
		except :
			if sys.argv[2]!='reset':
				print('Error : could not load command line argument as function parameter\nusing default values')
			else:
				print('Reseting metafile to initial configuration')
				reset()
				u,e,s,imi=url0,0,1,0
				no_reset=False
		if no_reset:
			u,e,s,imi=save_comic_episodes(url, ne, sn ,en,img_index)
	elif len(sys.argv)==6:
		print('using command line arguments as current_episode_url  no_of_episodes  season_no  episode_no episode_index')
		url=sys.argv[1]
		try:
			ne=int(sys.argv[2])
			sn=int(sys.argv[3])
			en=int(sys.argv[4])
			img_index=int(sys.argv[5])
		except:
			print('Error : could not load command line arguments as function parameters\nusing default values..')
		u,e,s,imi=save_comic_episodes(url,ne,sn,en,img_index)
	else:
		print('Error : no. of command line arguments different from expected\n see Ways to use program from command line')
		sys.exit()
	
	print('url,en,sn,img_index = ',u,e,s,imi)








