import ZapApi
import json
import pytest

from ZapApi import app

@pytest.fixture
def client(request):
	test_client = app.test_client()

	def teardown():
		pass

	request.addfinalizer(teardown)
	return test_client

def testrest(client):
	response = client.get('http://localhost:5000/GetRestraunt?Name=California')
	
	assert(b'Bawarchi' in response.data)

	