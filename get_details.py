import re
from image_downloader import image_downloader_

pname=''
img_link=''
follower=''
following=''


def get_detail(s):
	rawname=s.title.string.strip()
	rawname= rawname.split("(")
	pname=str(rawname[0])
	#print("Name :"+pname)

	following='ers,(.+?)Follo'
	pattern_following=re.compile(following)
	follower= "(.+?)Followers"
	pattern_follower= re.compile(follower)

	for metas in s.findAll('meta',{'name':'description'}):
		cont=metas.get("content")
		cont=cont.split("-")
		fwers_count=re.findall(pattern_follower,cont[0])
		follower=''.join(fwers_count)
		#print(follower)
		following_count = re.findall(pattern_following,cont[0])
		following=''.join(following_count)
		print("\t\t\t"+ follower+" Followers ")
		print("\t\t\t"+following +"Following ")

	for ppic in s.find_all("meta",{'property':"og:image"}):
		print("image location:"+ppic.get("content"))
		image_url=ppic.get("content")
		img_link = image_url.replace("/s150x150","")
		image_downloader_(img_link,pname)


