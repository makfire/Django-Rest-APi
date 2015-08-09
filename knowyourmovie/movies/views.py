from django.views.generic import View
from django.core import serializers	
from models import movie_details,auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import md5
import hashlib
import datetime
import json
from django.contrib.auth.models import User



class movielist(View):
	
	def get(self,request):
		if request.GET.get('search',''):
			'''Exact match '''
			queryset = movie_details.objects.filter(name__exact = str(request.GET.get('search','')))
			if not queryset:
				''' Search in sequential order of the name '''
				queryset = movie_details.objects.filter(name__startswith = str(request.GET.get('search','')))
			if not queryset:
				''' searches if string is their in name '''
				queryset = movie_details.objects.filter(name__icontains = str(request.GET.get('search','')))
		else:
			queryset = movie_details.objects.all()
	        data = serializers.serialize('json',queryset)
		return HttpResponse(data, content_type="application/json")
	
	
	def post(self,request,token):
		a = auth.objects.filter(token = unicode(token)).values()
		user = User.objects.get(id=int(a[0]['user_id']))
		if user.is_superuser:
			updated_values = {}
			dict_data = json.loads(request.body.decode("utf-8"))
			obj = movie_details(**dict_data)
			obj.save()
			data_dict = obj.__dict__
			data_dict.pop('_state') 
			data_dict  = json.dumps(dict(data_dict))
			return	HttpResponse(data_dict,content_type="application/json")
				
		else:
			return	HttpResponse(data_dict,content_type="text/plain")
			
		
			
	
	def put(self,request,token):
		updated_values = {}
		dict_data = json.loads(request.body.decode("utf-8"))
		pk = dict_data['pk']
		a = auth.objects.filter(token = unicode(token)).values()
		user = User.objects.get(id=int(a[0]['user_id']))
		if user.is_superuser:
			try:
				queryset = movie_details.objects.get(id = int(pk))
				for i,v in dict_data['fields'].items():
						setattr(queryset ,i,v)
				queryset.save()
				data_dict = queryset.__dict__
				data_dict.pop('_state') 
				data_dict  = json.dumps(dict(data_dict))	
				return HttpResponse(data_dict,content_type="application/json")
			except:
				return HttpResponse("Bad request",content_type="text/plain")
		else:
			return HttpResponse("Bad request",content_type="text/plain")
			


class single_view(View):
	def get(self,request,pk):
		queryset = movie_details.objects.filter(id = int(pk))
		data = serializers.serialize('json',queryset)
		return HttpResponse(data,content_type="application/json")
		
	def delete(self,request,pk,token=None):
		try:
			a = auth.objects.filter(token = unicode(token)).values()
			user = User.objects.get(id=int(a[0]['user_id']))
			if user.is_superuser:
				queryset = movie_details.objects.get(id = int(pk))
				queryset.delete()
				return HttpResponse("Object deleted",content_type="text/plain")
			else:
				return HttpResponse("Bad Request",content_type="text/plain")
			
		except:
			return HttpResponse("wrong id given to consume",content_type="text/plain")


class login_check(View):
	def get(self,request):
		''' return the login form '''
		'''authenticate'''
		user  = authenticate(username = str(request.GET.get('username','')),password = str(request.GET.get('password','')))
		try:
			if user.is_authenticated:
				''' check if token exist '''
				existing_user = auth.objects.filter(user_id = int(user.id)).values()
				if not existing_user:
					'''if token entry does not exists '''
					dict_data = {}
					date = datetime.datetime.now()
					m = hashlib.md5(date.__str__())
					token = m.hexdigest()
					''' save in table '''
					dict_data.update({'user':user,'token':unicode(token)})
					obj = auth(**dict_data)
					obj.save()
					token = obj.token	
				else:
					obj = existing_user[0]
					token = obj['token']
			return HttpResponse({unicode(token)},content_type="application/json")		
		except:	
			return HttpResponse("Bad request",content_type="text/plain")	
				
	


