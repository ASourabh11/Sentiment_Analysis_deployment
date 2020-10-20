from flask import Flask
from flask import request
from flask import Flask, render_template, request
app = Flask(__name__)
app.config["DEBUG"]=True

import pickle
model = pickle.load(open('twitter_nlp.pkl', 'rb'))
vectorizer = pickle.load(open('countvectorizer.pkl','rb'))
#model = load_model('House_price_prediction_model.h5')


@app.route('/')
def home():
    #return'<h1>hello app</h1>'
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		a = 'It is a negative tweet'
		b = 'It is a Positive tweet'

		data = request.form['twitt']
		data = [data]
		data = vectorizer.transform(data).toarray()
		pkl_predict = model.predict(data)
		if pkl_predict == 0: output = a
		elif pkl_predict == 4:output = b

		return render_template('result.html', Decision ='{}'.format(output))






	    #a = 'It is a negative tweet'
		##b = 'It is a Positive tweet'
		#if pkl_predict == 0:output = a
		#elif pkl_predict == 4:output = b
		#return render_template('result.html', Decision ='{}'.format(output))

	#return render_template('result.html', Decision ='{}'.format(pkl_predict))
		

	
	    
	    
	
	
	#return str(output) 
	    
	

      
    



if __name__ == '__main__':
    app.run(debug=True)