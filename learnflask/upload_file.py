import os
from flask import Flask,request
from werkzeug import secure_filename #get file name that u want to upload

UPLOAD_FOLDER='/home/enmu/Desktop/forLearningPy/learnflask'
ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS
@app.route('/',methods=['GET','POST'])
def upload_file():
	if request.methods == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			return '{} upload successed!'.format(filename)
	return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''