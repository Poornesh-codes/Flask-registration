#importing
from flask import Flask, render_template,request
import os

#interaction
web = Flask(__name__)
picfolder=os.path.join('static')
web.config['UPLOAD_FOLDER']=picfolder
#mapping
@web.route('/')
#inputs
def home():
    pic = os.path.join(web.config['UPLOAD_FOLDER'], 'flask.jpg')
    return render_template('home.html',user_image=pic)
#mapping
@web.route('/register')
#inputs
def register():
    return render_template('register.html')
#mapping
@web.route('/confirmation', methods=['POST','GET'])
#inputs
def confirming():
    if request.method == 'POST':
        n=request.form.get('name')
        c=request.form.get('city')
        p=request.form.get('phone')
        return render_template('confirm.html', name=n, city=c, phone=p)
#MAin
if __name__ == '__main__':
    web.run(debug=True)
