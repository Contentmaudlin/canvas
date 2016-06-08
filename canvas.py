import requests, json, pprint, wget
access_token = "1396~lVocfzFT3YufgeS0MDaMsTAUZFxwovLZTQRHbSJmXUwzDDLNDBBH4rwbZ2d1Zqrm"
def canvas():
	url = "https://canvas.instructure.com/api/v1/courses?access_token=" + access_token
	response = requests.get(url)
	json_courses = response.json() #need to check status code later here.
	course_id = list()
	for i in json_courses:
		if "Data Structures" in i['name']: #get Data Structures
			course_id.append(i['id'])
	print(course_id)

	# get assignment lists
	download_url = list()
	request = "https://canvas.instructure.com/api/v1/courses/" + str(course_id[0]) + "/assignments?access_token=" + access_token
	print(request)
	response = requests.get(request)
	json_assignments = response.json()
	for i in json_assignments:
		if "6" in i['name']:
			download_url.append(i['submissions_download_url'])
	print(download_url)
	download(download_url[0])

def download(url):
	print(url)
	wget.download(url)
canvas()