from flask import Flask
from flask import request


app = Flask(__app__)


@app.route('/', methods=['GET','POST'])
def home():
	return ''' <h1> hello</h1>
			   <h2> welcome to Lane's web </h2>'''

			   
@app.route('/',methods=['GET']
def signin_form():
	return '''<form action="signin" method="post"
	           <p><input name="username"></p>                                       
			   <p><input name="passport" type="passport"></p>
			   <p><button type ="submit:>Sign In </button></p>
			   </form>'''
		
		
@app.route('/signin',method=['POST'])
def signin():
	if request.form['username']=='lulane' and request.form['passport']=='passport':
		return '<h3> Hello,lulane</h3>'
	return '<h3>user is nor exit or username and password nor match</h3>'
	

if __name__ =='__main__':
	app.run()
			
