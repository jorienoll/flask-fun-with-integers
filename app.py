from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def display_numbers():
	n = 0
	if request.method == 'POST':
		n = int(request.form.get('number'))
		result = ''
		i = 1
		if int(n) > 0:
			while i <= n:
				result += str(i) + ' ';
				i = i + 1;
		else:
			while i >= n:
				result += str(i) + ' ';
				i = i - 1;
		return render_template('range.html', result=result)
	else:
		n = request.form.get('number')
		return render_template('range.html')

@app.route('/odd', methods=['GET', 'POST'])
def display_odd_numbers():
	n = 0
	if request.method == 'POST':
		n = int(request.form.get('number'))
		result = ''
		i = 1
		while i <= n:
			if(i % 2 != 0):
				result += str(i) + ' ';
			i = i + 1;
		# else:
		# 	while i >= n:
		# 		if(i % 2 != 0):
		# 			result += str(i) + ' ';
		# 		i = i - 1;
		return render_template('odd.html', result=result)
	else:
		return render_template('odd.html')

@app.route('/even', methods=['GET', 'POST'])
def display_even_numbers():
	n = 0
	if request.method == 'POST':
		n = int(request.form.get('number'))
		result = ''
		i = 1
		if int(n) > 0:
			while i <= n:
				if(i % 2 == 0):
					result += str(i) + ' ';
				i = i + 1;
		# else:
		# 	while i >= n:
		# 		if(i % 2 == 0):
		# 			result += str(i) + ' ';
		# 		i = i - 1;
		return render_template('even.html', result=result)
	else:
		return render_template('even.html')

@app.route('/prime', methods=['GET', 'POST'])
def display_prime_numbers():
	n = 0
	if request.method == 'POST':
		n = int(request.form.get('number'))
		result = ''
		for i in range(2, int(n)+1):
			isPrime = True
			for j in range(2, i):
				if i % j == 0:
					isPrime = False
			if isPrime:
				result += str(i) + ' ';
		return render_template('prime.html', result=result)
	else:
		return render_template('prime.html')
