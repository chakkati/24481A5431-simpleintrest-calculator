from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__)#app is object of flask

@app.route('/')
def welcome():
    return "welcome to Flakapp<=> routing"

#dynamic routing

@app.route('/greet/<uname>')
def greet(uname):
    return f"Good Morning,{uname}!"

#typed dynamic route---for selected operations only use
@app.route('/delete/<int:roll>')
def delete(roll):
    return f"deleted -{roll}"

#@app.route('/delete_user/<int:roll>')
#def delete_user(roll):
    #return redirect(url_for('/greet/<uname>'))

@app.route('/calculate', methods=['GET', 'POST'])
def si():
    if request.method == 'POST':
        p = float(request.form['p'])
        r = float(request.form['r'])
        t = float(request.form['t'])

        si = (p * r * t) / 100
        total_amount = p + si

        return render_template(
            'index.html',
            simple_interest=si,
            total_amount=total_amount,
            p=p,
            r=r,
            t=t,
            result=True
        )

    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True,port=3500)
