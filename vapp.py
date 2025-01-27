from flask import Flask, request, render_template
from views import views
import helper


app = Flask(__name__)
app.register_blueprint(views, url_prefix = "/views")

@app.route('/')
def structure():
    return render_template('structure.html', name = 'appa')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    helper.update_dna_sequence(user_input)
    image_url = '/static/images/sadappa.jpg'
    return render_template('output.html', user_input=user_input, image_url= image_url)

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
