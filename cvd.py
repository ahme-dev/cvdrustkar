from flask import Flask, render_template, request, redirect, send_from_directory
from libdocx import *
import secrets

app = Flask(__name__)

OUTPUT_DIR = 'out/'


# root route
@app.route('/', methods=['GET', 'POST'])
def handle():
	if request.method == 'POST':

		# get form values

		# get basic info
		info_list = [
			str(request.form['name']).strip(),
			str(request.form['address']).strip(),
			str(request.form['number']).strip(),
			str(request.form['email']).strip(),
		]

		# get experience info
		exp_list = list()
		for i in range(1, 4):
			y = str(request.form['exp-start-year-' + str(i)])
			z = str(request.form['exp-end-year-' + str(i)])
			a = y + ' - ' + z
			b = str(request.form['exp-place-' + str(i)])
			c = str(request.form['exp-about-' + str(i)])

			#if empty then stop
			if not b or b.isspace():
				break

			# append trimmed input
			exp_list.append(experience(a.strip(), b.strip(), c.strip()))

		# get education info
		edu_list = list()
		for i in range(1, 4):
			a = str(request.form['edu-year-' + str(i)])
			b = str(request.form['edu-degree-' + str(i)])
			c = str(request.form['edu-place-' + str(i)])
			d = str(request.form['edu-about-' + str(i)])

			#if empty then stop
			if not c or c.isspace():
				break

			# append trimmed input
			edu_list.append(education(a.strip(), b.strip(), c.strip(), d.strip()))

		# get skills info
		ski_list = list()
		for i in range(1, 8):
			a = str(request.form['ski-name-' + str(i)])
			b = str(request.form['ski-about-' + str(i)])

			# if empty then stop
			if not a or a.isspace():
				break

			# append trimmed input
			ski_list.append(skill(a.strip(), b.strip()))

		# make cv with info at rand url
		FILENAME = secrets.token_urlsafe() + '.docx'
		make_file(OUTPUT_DIR, FILENAME, "blue", info_list, exp_list, edu_list, ski_list)

		# direct to rand url
		return redirect(OUTPUT_DIR + FILENAME)
	else:
		# direct to a lang
		return redirect('/kur')


@app.route('/kur', methods=['GET'])
def lang_kur():
	# serve kurdish
	return render_template('kur.html')


@app.route('/eng', methods=['GET'])
def lang_eng():
	# serve english
	return render_template('eng.html')


# route for downloading generated cvs
@app.route('/'+OUTPUT_DIR+'<string:fn>', methods=['GET'])
def get(fn):
    return send_from_directory(OUTPUT_DIR, fn)


if __name__ == '__main__':
    app.run(debug=True)
