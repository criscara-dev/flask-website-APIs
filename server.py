from flask import Flask, render_template, request, session, redirect, url_for, flash
from latin import latinizer
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, 
                    DateTimeField, RadioField, SelectField)
from wtforms.validators import DataRequired, Length


app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/signup') 
def signup():
    return render_template('signup.html')

@app.route('/thankyou') 
def thankyou():
    first = request.args.get('firstname')
    last = request.args.get('lastname')
    fullname = first + ' ' + last
    return render_template('thankyou.html',fullname=fullname)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404 

@app.route("/playground.html")
def playground():
    name = 'Cristian'
    api = { 'age':'42','language':'eng','height':'172'}
    a_list = [1,2,3,4,5]
    user_logged_in = True
    return render_template('playground.html',your_name=name,api=api,a_list=a_list,user_logged_in=user_logged_in)

@app.route( '/heroes/<name>')
def user_page(name):
    # return f'<h1>Hi, User: {name.upper()}!</h1>'
    return render_template('heroes.html',name=name)

# @app.route("/info")
# def info():
#     return "<p>lorem ipsum</p>"

# @app. route( '/puppy_latin/<name>')
# def other_page(name):
#     return latinizer(name)


@app.route('/validationform') 
def validationform(): 
    return render_template('validationform.html')

@app.route('/report') 
def report():
    # set vars to False
    lower = False
    upper = False
    num_end = False
    # get dat from form
    username = request.args.get('username') 
    lower = any(char.islower() for char in username)
    upper = any(char.isupper() for char in username)
    num_end = username[-1].isnumeric()    
    report = lower and upper and num_end 

    return render_template('report.html', report=report, lower=lower,upper=upper,num_end=num_end )

#############################
### USING FLASK WTR FORMS ###

app.config['SECRET_KEY'] = 'form_token_security_key'


class InfoForm(FlaskForm):
    planet = StringField('From which planet are you from?', validators= [DataRequired()])
    far_from_earth= BooleanField('Is it far fro m Earth?')
    planet_color = RadioField('What color is your planet?',
                    choices=[('r','red'),
                    ('b','blue'),
                    ('y','yellow')
                    ])
    super_hero_power = SelectField(u'What is your seperhero power?',
    choices=[('strenght','strenght'),
    ('brain','brain'),
    ('punch','  punch')
    ])
    submit = SubmitField('Submit')  

@app.route('/heroesform', methods=['GET','POST'])
def heroesform():
    #  planet = False
    form = InfoForm()

    if form.validate_on_submit():
        # planet = form.planet.data
        # form.planet.data = ''
        flash('Thank you for submitting the form!')
        session['planet'] = form.planet.data
        session['far_from_earth'] = form.far_from_earth.data
        session['planet_color'] = form.planet_color.data
        session['super_hero_power'] = form.super_hero_power.data
        return redirect(url_for('thankyou2'))

    return render_template('heroesform.html', form=form)

@app.route('/thankyou2') 
def thankyou2(): 
    return render_template('thankyou2.html')

### run if is the main file: ###
if __name__ == '__main__':
    app.run()  