from flask import Flask ,jsonify,render_template,request
import player_scout as ps
from PIL import Image
import pickle
import numpy as np


app = Flask(__name__)
clf=pickle.load(open('player_scout.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/player_scouter',methods=['POST'])
def player_scouter():

    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=clf.predict(final_features)

    output=prediction
    return render_template('index.html',player_scouter='This is a {} player'.format(output))
    
    
    
    """if request.method=="POST":
        Goals=request.form['Goals']
        player_scout=ps.scout(Goals)
        print(player_scout)""

    return render_template('index.html' )

"""
"""@app.route('/sub',methods =['POST'])
def submit():
    if request.method == "POST":
        name =request.form["username"]
    
    return render_template("sub.html",n= na 
    

"""
if __name__ == "__main__":
    app.run(debug=True)