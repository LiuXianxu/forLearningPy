from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
	return "hello_world"
@app.route('/user/<username>')
def show_user_profile(username):
    # 显示用户名
    return 'User {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据
    return 'Post {}'.format(post_id)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # 显示 /path/ 之后的路径名
    return 'Subpath {}'.format(subpath)

@app.route('/projects/')#这种方式比较好
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'