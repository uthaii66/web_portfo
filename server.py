from flask import Flask, render_template,redirect
from flask import request
import csv
app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
def messages(data):
    with open("datas.txt",mode="a") as datas:
        email =data["email"]
        sub = data["subject"]
        message = data["message"]
        datas.write(f"\n {email},{sub},{message}")

def message(data):
    with open("datas.csv",mode="a") as r:
        email =data["email"]
        sub = data["subject"]
        message = data["message"]
        # f = open("SalesJan2009.csv","r")
        cw = csv.writer(r)
        # r = next(cw)
        # print(r[0].upper()+"\t"+r[1].upper()+"\t"+r[2].upper()+"\t"+r[3].upper()+"\t"+r[4].upper())
        # for r in cr:
        #     print(r[0]+"\t"+r[1]+"\t"+r[2]+"\t"+r[3]+"\t"+r[4])
        cw.writerow([email,sub,message])




@app.route('/')
def blog():
    return render_template('index.html')


@app.route('/<string:pagename>')
def blog1(pagename):
    return render_template(pagename)

# @app.route('/work.html')
# def work():
#     return render_template('work.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/index.html')
# def index():
#     return render_template('index.html')


@app.route('/submit', methods=['POST', 'GET'])
def submitform():
    if request.method == 'POST':
        data =request.form.to_dict()
        message(data)
        return redirect("thanks.html")
    else:
        return "TRY AGAIN!!!"
