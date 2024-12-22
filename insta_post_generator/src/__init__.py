
from flask import Flask, render_template, request
from src.insta_post_generator.main import run
from src.insta_post_generator.image_generation import img_gen


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        images=None
        if request.method == 'POST':
            topic = request.form['topic']
            details = request.form['details']
            input = {'topic':{topic},'details' : {details}}
            response_llm = run(input)
            img1 = img_gen(response_llm["prompt1"])
            img2 = img_gen(response_llm["prompt2"])
            img3 = img_gen(response_llm["prompt3"])

            images = [img1, img2, img3]
            return render_template('index.html', images = images)
        
        return render_template('index.html', images = images)
     

    return app