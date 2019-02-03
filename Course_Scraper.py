from bs4 import BeautifulSoup
from urllib.request import urlopen
from connect_sql import insert
from verify import verify_sec_num
from send_mail import processSendMail
from update import update


#Scrape course section info
def findSecNum (testudo_url):
	html = urlopen(testudo_url)
	course_bs = BeautifulSoup(html.read(),'html.parser')
	sections = course_bs.find('div',{'class':'sections sixteen colgrid'})

	face_sec_num = len(sections.findAll('div',{'class':'section delivery-f2f'}))
	blended_sec_num = len(sections.findAll('div',{'class':'section delivery-blended'}))
	online_sec_num = len(sections.findAll('div',{'class':'section delivery-online'}))

	sec_num = face_sec_num + blended_sec_num + online_sec_num

	return sec_num


#Main function that scrape info and compare with existing info in the database
def main():
	base_url = 'https://app.testudo.umd.edu/soc/'
	html = urlopen(base_url)
	bs = BeautifulSoup(html.read(),'html.parser')

	left_list = bs.find('div',{'id':'left-course-prefix-column'}).findAll('div',{'class':'course-prefix row'})
	right_list = bs.find('div',{'id':'right-course-prefix-column'}).findAll('div',{'class':'course-prefix row'})
	complete_list = left_list + right_list

	try:
		for i in complete_list:
			department_url = i.find('a').attrs['href']
			department_html = urlopen(base_url+department_url)
			bs = BeautifulSoup(department_html.read(),'html.parser')
			course_list = bs.findAll('div',{'class':'course'})
			for j in course_list:
				course_name = j.attrs['id']
				course_sec_num = 0
				individual_instruction = j.find('div',{'class':'individual-instruction-message'})
				if(individual_instruction is None):
					course_url = base_url + department_url + '/' + course_name
					course_sec_num = findSecNum(course_url)
					is_update = verify_sec_num(course_name,course_sec_num)
					if(is_update):
						processSendMail(course_name)
						update(course_name,course_sec_num)
	except AttributeError as e:
		main()



main()




