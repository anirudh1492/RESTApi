import requests as req
import json
import pytest




@pytest.fixture
def client(request):
	test_client = app.test_client()

	def teardown():
		pass

	request.addfinalizer(teardown)
	return test_client


@pytest.get.paramterized("Name",[('California'),('Atlanta'),('Garland'),('Plano')])

def getrest(Name):
	base_url = 'http://127.0.0.1:5000/GetRestraunt'
	data = {'Name':Name}
	response = req.get(base_url,data)
	a=json.loads(response.text)
	return(a)
	