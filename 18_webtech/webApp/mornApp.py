from flask import Flask
from flask import request
app = Flask(__name__)
from flask import render_template

# Form page to submit text
#============================================
# create page with a form on it
@app.route('/')
def submission_page():
    #content = 'hello'
    return render_template('template.html')

@app.route('/about')
def about_page():
    #content = 'hello'
    return render_template('about.html')

    '''
    '''
# <form action="/word_counter" method='POST' >
#         <input type="text" name="user_input" />
#         <input type="submit" />
#     </form>
# My word counter app
#==============================================
# create the page the form goes to
@app.route('/word_counter', methods=['POST','GET'] )
def word_counter():
#     if request.method == 'POST':
#         return ''
    # get data from request form, the key is the name you set in your form
    data = request.form['user_input']

    # convert data to list
    data = [data]

    import pickle
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfTransformer
    from sklearn.naive_bayes import MultinomialNB
    
    clf2 = pickle.load(open( "data/my_model.pkl", "rb" ) )
    count_vect2 = pickle.load(open( "data/my_vectorizer.pkl", "rb" ) )
    tfidf_transformer2 = pickle.load(open ( "data/my_transformer.pkl", "rb" ))

    #process new data
    X_new_counts = count_vect2.transform(data)
    X_new_tfidf = tfidf_transformer2.transform(X_new_counts)
    predicted = clf2.predict(X_new_tfidf)
    
    #output the category that the text is in
    categories = ['alt.atheism', 'comp.graphics', 'sci.med', 'soc.religion.christian']
    for doc, category in zip(data, predicted):
        #return('%r => %s' % (doc, categories[category]))
        return render_template('template2.html', doc=doc, category=categories[category])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)