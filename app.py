from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")
@app.route('/members')
def member():
    return 'hello member '

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score<50:
        res="FAIL"
    else:
        res="PASS"
    obj={'res':res,"score":score}
    return render_template('result.html',result=obj)
@app.route('/fail/<int:score>')
def fail(score):
    return 'the person has failed and the marks are '+str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=''
    if marks<50:
        result="fail"
    else:
        result="success"
    return redirect(url_for(result,score=marks))
    # return result


@app.route('/submit',methods=['POST'])
def submit():
    total_score=0
    if request.method=='POST':
        s=float(request.form['science'])
        m=float(request.form['maths'])
        c=float(request.form['c'])
        ds=float(request.form['data science'])
        total_score=(s+m+c+ds)/4
    return redirect(url_for('success',score=total_score))

if __name__=='__main__':
    app.run(debug=True)