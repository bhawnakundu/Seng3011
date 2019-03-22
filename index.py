from flask import Flask, request, Response
from flask_restplus import Api, Resource , fields
import datetime , re
import json, os, time, decimal, re, subprocess,random,string

app=Flask(__name__)
api = Api(app)


# function used to split a date strting 
def getDateInParts(inputs):
		s_year = re.search('^[0-9]{4}-' , inputs).group()
		s_year = re.search('^[0-9]{4}' , s_year).group()
		s_date = re.search('-[0-9]{2}-', inputs).group()
		s_date = re.search('[0-9]{2}', s_date).group()
		s_month = re.search('-[0-9]{2}T', inputs).group()
		s_month = re.search('[0-9]{2}', s_month).group()
		s_hour = re.search('T[0-9]{2}:', inputs).group()
		s_hour = re.search('[0-9]{2}', s_hour).group()
		s_min = re.search(':[0-9]{2}:', inputs).group()
		s_min = re.search('[0-9]{2}', s_min).group()
		s_sec = re.search(':[0-9]{2}$', inputs).group()
		s_sec = re.search('[0-9]{2}', s_sec).group()
		return s_year, s_date ,s_month, s_hour, s_min , s_sec



@api.route('/show')
class show(Resource):
	
	def get(self):

		inputs = request.get_json()
		location = inputs['location']
		#  now key terms are a array 
		key_terms = inputs['key_terms']
		key_terms = re.split(',', key_terms)
		# splitted the date string
		s_year, s_date ,s_month, s_hour, s_min , s_sec = getDateInParts(inputs['start_date'])
		# start_date = datetime.datetime(s_year, s_date ,s_month, s_hour, s_min , s_sec)
		e_year, e_date ,e_month, e_hour, e_min , e_sec = getDateInParts(inputs['end_date'])
		# end_date = datetime.datetime(s_year, s_date ,s_month, s_hour, s_min , s_sec)



		# start_date = datetime.datetime()
		sample_result = {
		    'url':"www.google.com",
		    'date_of_publication':"2016-05-19",
		    'headline':"My Name is amol",
		    'main_text':"I am the best human being in the world",
		    'reports': "NULL"
		 }
		return sample_result


# this is the main file 
#########################################################################
if __name__ == '__main__':
	app.run(debug=True)