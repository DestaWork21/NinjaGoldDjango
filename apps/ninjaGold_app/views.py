from django.shortcuts import render, redirect
from random import randrange

def index(request):

	if 'gold' not in request.session:
		request.session['gold'] = 0
	if 'activity' not in request.session:
		request.session['activity'] = []

	return render(request, "ninjaGold_app/index.html")

def process(request, location):

	if location == "farm":
		gold=randrange(10,21) 
	elif location == "cave":
		gold=randrange(5,11) 
	elif location == "house":
		gold=randrange(2,6) 
	else: #casino route
		gold=randrange(-50,51) 

	if gold >= 0:
		verb = "earned"
	else:
		verb = "lost"

	request.session['activity'].append('you went to the {} and {} {} gold'.format(location, verb, gold))
	request.session['gold']+=gold

	return redirect('/')