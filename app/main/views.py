from flask import render_template,request,redirect,url_for,flash,abort
from . import main
from .. import db,photos
from .. requests import get_quote
from .forms import PostForm, CommentForm, SubscriptionForm,UpdatePost,UpdateProfile
from ..models import User,Post,Comment,Subscription
from flask_login import login_required,current_user
from ..email import mail_message




@main.route('/',methods = ['GET','POST'])
def index():
    
    title = 'Home'
    posts=Post.query.all()
    quote=get_quote()

    
    return render_template('index.html', posts=posts,title=title,quote=quote)

# @main.route("/")
# @main.route("/home")
# def home():
#     posts = Post.query.all()
#     # page = request.args.get('page', 1, type=int)
#     # posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    
#     return render_template('home.html', posts=posts)

# @main.route("/about")
# def about():
#     return render_template('about.html', title='About')


@main.route('/post/<int:id>', methods=['GET', 'POST'])
def single_line(id):
    '''
    View function to return a single article
    '''
    post = Post.query.get(id)
    title = "article"
    comments = Comment.get_comments(id)

    return render_template('post.html', post=post, title=title, comments=comments)

@main.route('/new/post', methods=['GET', 'POST'])
def new_post():
    '''
    route to avail form for writing a new post
    '''
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.body.data
        new_post = Post(title=title, body=post)
        new_post.save_post()
        return redirect(url_for('main.index'))
    return render_template('new_post.html', form=form)

@main.route('/delete/post/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_post(id):
    """
    view route to delete a selected post
    """
    post = Post.query.filter_by(id=id).first()

    if post is not None:

        post.delete_post()
        return redirect(url_for('main.index'))

@main.route("/update/post/<int:id>", methods=['GET', 'POST'])
@login_required
def update_post(id):
    post=Post.query.filter_by(id=id).first()
    if post is None:
        abort(404)

    form = UpdatePost()
    if form.validate_on_submit():
        post.body = form.body.data
        db.session.add(post)
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('main.index'))
    
        return render_template('new_post.html',form=form)    


@main.route('/post/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    '''
    View new comment function that returns a page with a form to create a comment for the specified post
    '''
    post = Post.query.filter_by(id=id).first()

    if post is None:
        abort(404)

    form = CommentForm()

    if form.validate_on_submit():
        body = form.body.data
        new_comment = Comment(
            body=body, post_id=id, user_id=current_user.id)
        new_comment.save_comment()

        return redirect(url_for('main.index'))

    title = 'New Comment'
    return render_template('new_comment.html', title=title, comment_form=form)

@main.route('/delete/comment/<int:id>',methods = ['GET','POST'])
@login_required
def delete(id):
    comment = Comment.query.filter_by(id=id).first()
    if comment is not None:
        comment.delete_comment()
        
        return redirect(url_for('main.index'))

@main.route('/subscription/fill',methods = ["GET","POST"])
def subscriber():

    form= SubscriptionForm()


    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        new_subscriber = Subscription(email=email,name=name)
        db.session.add(new_subscriber)
        db.session.commit()

        mail_message("Thank you for subscribing","email/welcome_user",new_subscriber.email,new_subscriber=new_subscriber)
        return redirect(url_for('main.index'))
    return render_template('subscription.html', form=form )

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


