import requests,json
import jsonify
import re
import datetime




# This script is going to be used to check is the API is providing suitable and correct results.
headers = {'content-type': 'application/json'}
sample_input2 = json.dumps({
	'location': "",
    'key_terms': "",
    'start_date': "",
    'end_date': ""
})
sample_input = json.dumps({
	'location': "Chicago",
    'key_terms': "Salmonella , hedgehogs",
    'start_date': "2018-12-19T05:45:10",
    'end_date': "2019-02-21T05:45:10"
})

url = 'http://0.0.0.0:5000/show'



# Test1. check for error codes on wrong inputs - 
def case1():
	print("Test Case 1: Checking for a sample wrong input")
	# print(sample_input2)
	r = requests.get(url, data=sample_input2 , headers=headers)
	# print(r.status_code)
	assert(r.status_code == 400)
	# print(r.text)
	print("Test 1: Pass")


# Test2 check for correct input and output
def case2():
	print("Test case 2: Checking if the input is correct")
	# print(sample_input)
	r = requests.get(url, data=sample_input , headers=headers)
	print("\t2.1 Check the status code")
	assert(r.status_code == 200)
	print("\tTest 2.1: Pass ")



	print("\t2.2 check for the matching dates")
	res = json.loads(r.text)
	dop = res['date_of_publication']
	year = re.search('^[0-9]{4}', dop).group()
	date = re.search('[0-3][0-9]$',dop).group()
	month = re.search('-([0,2][0-9])-',dop).group()
	month = re.search('([0,2][0-9])',month).group()
	re_date = datetime.datetime(int(year),int(month),int(date))
	s_given_date = datetime.datetime(2018,12,19)
	e_givendate = datetime.datetime(2019,2,21)
	assert(re_date > s_given_date and re_date < e_givendate)
	print("\tTest 2.2: Pass ")


	print("\t2.3 check for the matching key terms with headlines")
	g_keyterms = ["Salmonella", "hedgehogs"]
	headline = res['headline']

	for i in g_keyterms:
		assert(i in headline)

	print("\tTest 2.3: Pass ")	

	print("Test 2: Pass")



# Check for correct input but no output
def case3():
	print("Test Case 3: Check if input correct but no output {status code 404}")
	r = requests.get('http://127.0.0.1:5000/show', data=sample_input2 , headers=headers)
	# print(r.status_code)

	assert(r.status_code == 404)
	print("Test 3: Pass")







case1()
case2()
case3()