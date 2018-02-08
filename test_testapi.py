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

#@pytest.mark.parametrize("rid,name,city,country,output",[("NYCSB","Starbucks","New York","United States")])

@pytest.fixture
def postrest():
	def _postrestint(rid,name,city,country):
		base_url = 'http://127.0.0.1:5000/CreateRest'
		data = {'Restraunt_id':rid,"Name":name,"Country":country,"City":city}
		response = req.post(base_url,data)
		return(response.text)
	return _postrestint

@pytest.mark.parametrize("rid,name,city,country,expected",[("IPV","Velvet","Pune","India","Successfully Added")])
def test_postrest(postrest,rid,name,city,country,expected):
	a=postrest(rid,name,city,country).strip().replace('"','')
	#rest_list = list(getrest(city).keys()
	assert a == expected

@pytest.fixture
def postmenu():
	def _postmenuint(mtype,mname,mid):
		base_url = 'http://127.0.0.1:5000/Crtmitem'
		data = {'Mtype':mtype,"Menu_id":mid,"Mname":mname}
		response = req.post(base_url,data)
		return(response.text)
	return _postmenuint

@pytest.mark.parametrize("mtype,mname,mid,expected",[("Lunch","Kadhi","L098","Successfully Added")])
def test_postmenu(postmenu,mtype,mname,mid,expected):
	a=postmenu(mtype,mname,mid).strip().replace('"','')
	#rest_list = list(getrest(city).keys()
	assert a == expected


@pytest.fixture
def delrestraunt():
	def _delrestint(getrest,rname):
		base_url = 'http://127.0.0.1:5000/RDelete?Name='+rname
		data = {'Name':rname}
		print("::",data)
		print(":|",base_url)
		respose = req.delete(base_url)
		return('deleted')
		
	return _delrestint

@pytest.mark.parametrize("rname,expected",[("Grub","Grub")])
def test_delrestraunt(delrestraunt,getrest,rname,expected):
	out = delrestraunt(getrest,rname)
	a=getrest(rname)
	list_get = list(a.keys())	
	print(list_get)
	assert list_get == expected

#DELETE MENU TEST FUNCTION
@pytest.fixture
def delmenu():
	def _delmenuint(getrest,mname):
		base_url = 'http://127.0.0.1:5000/MDelete?ItemName='+mname
		respose = req.delete(base_url)
		return('deleted')
		
	return _delmenuint

@pytest.mark.parametrize("rname,expected",[("Grub","Grub")])
def test_delrestraunt(delmenu,getmenuitem,Itemname,expected):
	out = delmenu(getrest,rname)
	a=getmenuitem(rname)
	list_get = a(name)[name]['Itemname']	
	print(list_get)
	assert list_get == expected


