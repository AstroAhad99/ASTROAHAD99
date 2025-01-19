# Developing a simple web application on flask

from flask import Flask, render_template

app = Flask(__name__)

# Creating the global varaible containing the details of the post

posts = {
    0:{
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}



# This is first end point
@app.route('/') # This is a decorator that runs the home def
def home():
    return 'Hello, World!'


@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    #return f"Post {post['title']}, content:\n\n{post['content']}"
    #return render_template('post.html')
    if not post:
        return render_template('404.html', message=f'A post with id {post_id} was not found.')
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
