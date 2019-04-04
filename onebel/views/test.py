from . import tests

@tests.route('/test')
def hello():
	return 'hello world!'