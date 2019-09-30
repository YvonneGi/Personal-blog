from flask import render_template,request,redirect,url_for,flash,abort
from . import main
from .. import db
from .forms import PostForm, CommentForm, SubscriptionForm
from ..models import User,Writer,Post,Comment,Subscription
from flask_login import login_required,current_user
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    '''
    @login_manager.user_loader Passes in a writer_id to this function
    Function queries the database and gets a user's id as a response
    '''
    return User.query.get(user_id)

@main.route("/")
@main.route("/home")
def home():
    posts = Post.query.all()
    # page = request.args.get('page', 1, type=int)
    # posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    
    return render_template('home.html', posts=posts)


@main.route('/')
def about():

    posts=Post.query.all()

    return render_template('about.html', posts=posts)

@main.route('/post', methods=['GET','POST'])
def new_post():
    '''
    New Post Page
    '''
    post_form = PostForm()

    if post_form.validate_on_submit():
        title = post_form.title.data
        body = post_form.body.data
        new_post = Post(title=title,body = body)

        new_post.save_post()
        return redirect(url_for('main.index'))

    title = f'{Post.title}'
    return render_template('post.html',title= title, post_form=post_form)


@main.route('/comments/<int:id>', methods=['GET', 'POST'])
@login_required
def comments(id):
    comment_form = CommentForm()
    comment = Comment.query.order_by('-id').all()

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data()
        new_comment = Comment(comment=comment,users=current_user.username)
        new_comment.save_comment()
        return redirect(url_for('main.comments',id = post.id))
    return render_template('comments.html')

@main.route('/delete/<int:id>')
@login_required
def delete(id):
    del_comment = Comment.query.get(id)
    db.session.delete(del_comment)
    db.session.commit()
    return redirect(url_for('main.layout'))

@main.route('/subscription',methods = ["GET","POST"])
def subscriber():

    form= SubscriptionForm()


    if form.validate_on_submit():
        email = form.email.data
        date = form.date.data

        new_subscriber = Subscription(email=email,date = date,user_id=current_user.id)

        new_subscriber.save_subscriber()
        return redirect(url_for('subscriber'))


    return render_template('layout.html',email= email, subscribe_form=form )
