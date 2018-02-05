import requests as req
import json
import pytest


@pytest.fixture
def getrest():
	def _request(Name):
		base_url = 'http://127.0.0.1:5000/GetRestraunt'
		data = {'Name':Name}
		response = req.get(base_url,data)
		a=json.loads(response.text)
		return a
	return _request
	
@pytest.mark.parametrize("city,expected",[
	("Plano",["Wendys"]),
	("Garland",["Chick-fillA"]),
	("California",["Bawarchi","McDonalds"])
	])

def test_getrest(getrest,city,expected):
	rest_list = list(getrest(city).keys())
	assert rest_list == expected

@pytest.fixture
def getmenuitem():
	def _gmenu(name):
		base_url = 'http://127.0.0.1:5000/GetMenuItem'
		data = {'Rname':name}
		response = req.get(base_url,data)
		out = json.loads(response.text)
		return out
	return _gmenu

@pytest.mark.parametrize("name,expected",[("Wendys","Burger")])

def test_getmenu(getmenuitem,name,expected):
	print(':::',getmenuitem(name)[name]['Itemname'])
	menu_list = getmenuitem(name)[name]['Itemname']
	assert menu_list == expected


