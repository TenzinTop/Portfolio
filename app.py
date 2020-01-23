from flask import Flask, render_template, request
import json
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    comment_text = db.Column(db.String(200),unique=False)

    def __repr__(self):
        return f"{self.name} has commented {self.comment_text}"



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')    

@app.route('/blogs')
def blogs():
    return render_template('aboublogst.html')    

@app.route('/comment',  methods=['GET', 'POST'])
def comment():
    
    if request.method == "POST":
        name = request.form['name']
        comment = request.form['comment']
        obj = User(name=name, comment_text=comment)
        db.session.add(obj)
        db.session.commit()  
                
        return render_template('comment.html')
    elif request.method == "GET":
        return render_template('comment.html')

@app.route('/api/comments')
def commentlist():
    comments_list = []
    comment_dict = {}
    for comment in COMMENTS:
        comment_dict['id'] = comment.id
        comment_dict['name'] = comment.name
        comment_dict['comment'] = comment.comment_text
        comments_list.append(comment_dict)
    return json.dumps(comments_list)

if __name__ == "__main__":
    app.run(debug=True)



