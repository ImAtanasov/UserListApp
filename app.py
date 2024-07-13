from flask import Flask, render_template, request, redirect, url_for, flash
from forms import UserForm
from models import db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)


@app.route('/')
@app.route('/page/<int:page>')
def index(page=1):
    search = request.args.get('search', '')
    if search:
        users = User.query.filter(User.name.ilike(f'%{search}%')).paginate(page=page, per_page=5, error_out=False)
    else:
        users = User.query.paginate(page=page, per_page=5, error_out=False)
    return render_template('index.html', users=users)


@app.route('/add', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(name=form.name.data, email=form.email.data, phone=form.phone.data)
        db.session.add(new_user)
        db.session.commit()
        flash('User added successfully!', 'success')
        return redirect(url_for('index'))
    else:
        if form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Error in {getattr(form, field).label.text}: {error}", 'warning')
    return render_template('add_user.html', form=form)


@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
