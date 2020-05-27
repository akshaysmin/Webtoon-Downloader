from bs4 import BeautifulSoup
import webbrowser,requests,time,sys



#lines 8,9,10 ,11changes every run , lines 8,9,10,11 change on reset
url0='https://www.webtoons.com/en/fantasy/tower-of-god/season-1-ep-0/viewer?title_no=95&episode_no=1'
url="https://www.webtoons.com/en/fantasy/tower-of-god/season-2-ep-1/viewer?title_no=95&episode_no=81"
en=0
sn=2
img_index=80
ne=2
u,e=url,en


display_text='''
Ways ro use program from command line:
   python comic_download_header.py no_of_episodes
   python comic_download_header.py reset	               #resets all evolutions of program
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
	#u - new url , e - new ep_no
	u='url="'+u+'"'
	e='en='+str(e)
	s='sn='+str(s)
	imi='img_index='+str(imi)
	replace_line('comic_download_header.py',8,u)
	replace_line('comic_download_header.py',9,e)
	replace_line('comic_download_header.py',10,s)
	replace_line('comic_download_header.py',11,imi)
	return None

def seconds2clock(t):
	#returns [hr,min,sec]
	return [(t//60)//60,(t//60)%60,t%60]

def reset():
	u,e,s,imi=url0,0,1,0
	evolve(u,e,s,imi)

def save_comic_episodes(url, ne, sn ,en,img_index):
	'''
	next_episode_url=func(current_episode_url, no_of_episodes, season_no ,episode_no)
	saves all images from current episode to total of given no. of episodes
	'''
	t1=time.time()
	session = requests.Session()																					#create Session obj
	for i in range(ne):
		r=session.get(url)
		print('---------------------------%s/%s--------------------------'%(i+1,ne))
		print('accesing tog episode\n',url)
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
	t2=time.time()
	print('time taken for downloading %s episodes, [hr,min,sec] = '%(ne),seconds2clock(t2-t1))
	return url,en,sn,img_index


#run from commandline - interface
if len(sys.argv)==1:
	u,e,s,imi=save_comic_episodes(url, ne, sn ,en,img_index)
elif len(sys.argv)==2:
	not_reset=True
	try:
		ne=int(sys.argv[1])
	except :
		if sys.argv[1]!='reset':
			print('Error : could not load command line argument as function parameter\nusing default no. of episodes (2)')
		else:
			print('Reseting program to initial configuration')
			reset()
			u,e,s,imi=url0,0,1,0
			not_reset=False
	if not_reset:
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
	print('Error : no. of command line arguments different from expected\n must be none,1 or 4')

print('url,en,sn,img_index = ',u,e,s,imi)
evolve(u,e,s,imi)







