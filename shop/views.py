import os
import random
import requests
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.urls import reverse

from .models import *


def gen_file_name():
	res = ''
	for i in range(50):
		rand = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
		res = res+rand
	return res +'.txt'


def check_pay(code, cash):
	setting = Setting.objects.all()[0]
	phone = setting.phone
	token = setting.token
	s = requests.Session()
	s.headers['authorization'] = 'Bearer ' + token  
	parameters = {'rows': '50'}
	h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + phone + '/payments', params = parameters)
	req = json.loads(h.text)
	for i in range(len(req['data'])):
		if req['data'][i]['comment'] == str(code) and float(req['data'][i]['sum']['amount']) >= float(cash):
			return True

	return False


def download(request, id):
	if request.user.is_staff:
		data = {
			'id':id,
			'user':request.user,
			}

		if request.POST:
			f = open('product.txt', 'w')
			f.write(request.POST['download_product'])
			f.close()
			f = open('product.txt')
			count = 0
			for i in f:
				res = i.strip('\n').strip("")

				if res == '':
					continue

				count = count+1
				ls = List(product_id = id, product = res)
				ls.save()

			ct = Product.objects.get(id = id)
			ct.count = int(ct.count) + count
			ct.save()

			f.close()
			os.remove('product.txt')

		return render(request, 'admin/download_product.html', data)


def send_file(request, filename):
	file = open("products/"+filename, 'rb')
	return FileResponse(file, as_attachment=True)


def index(request):
	buy_key = random.randint(111111111, 999999999)
	request.session['buy_key'] = buy_key
	setting = Setting.objects.all()
	products = Product.objects.all()


	if request.GET.get('search'):
		search = request.GET['search']
		products = Product.objects.all().filter(title = search)

	try:
		data = {
			'products':products,
			'List':List,
			'setting':setting[0],
			'buy_key':buy_key,
			}
	except IndexError:
		return redirect('/admin')

	return render(request, 'shop/index.html', data)


def buy(request):
	if request.POST:
		product_id = request.POST['product_id']
		count = request.POST['count']
		buy_key = request.session['buy_key']

		product = Product.objects.get(id = product_id)

		cash = float(product.price) * float(count) 
		check_oplata = check_pay(request.session['buy_key'], cash)

		if check_oplata:
			edit_count = Product.objects.get(id = product_id)
			if edit_count.count < int(count):
				edit_count.count = 0 
				edit_count.save()
			else:
				edit_count.count = int(edit_count.count) - int(count) 
				edit_count.save()

			item = List.objects.all().filter(product_id = product_id)[:int(count)]

			filename = gen_file_name()
			f = open('products/'+ filename, 'a')
			for i in item:
				f.write(str(i.product) + '\n')
				i.delete()
			f.close()
					
			url = reverse('send_file', args = [filename])
			request.session['buy_key'] = random.randint(111111111, 999999999)
			no_pay = False
		else:
			no_pay = True
			url = False

		buy_key = request.session['buy_key']
		setting = Setting.objects.all()
		products = Product.objects.all()

		data = {
			'products':products,
			'List':List,
			'setting':setting[0],
			'buy_key':buy_key,
			'good_pay':url,
			'no_pay':no_pay
			}


		return render(request, 'shop/index.html', data)