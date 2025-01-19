# Developing a simple web application on flask

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Creating the global varaible containing the details of the post

posts = {
    0:{
        'post_id':0,
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

# Creating a form

# The above form end point create another link with the form 
# output so now we need to save the output and redirect
# the user to another page and for that we will create another
# page
@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id':post_id, 'title':title, 'content':content}

        return redirect(url_for('post', post_id=post_id)) 
    return render_template('create.html')

    # url_for function takes the function as 
    #input and a paramter (post_id) so to create a post

if __name__ == '__main__':
    app.run(debug=True)
