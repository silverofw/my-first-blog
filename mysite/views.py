from django.http import HttpResponse
from django.shortcuts import render_to_response

def here(request):
	return HttpResponse('媽,I am here!')

def math(request,a,b):
	a=int(a)
	b=int(b)
	s=a+b
	d=a-b
	p=a*b
	q=a/b
	return render_to_response('math.html',{'s':s, 'd':d, 'p':p, 'q':q})