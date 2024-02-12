from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Your existing code from 7-db_setup.py

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        try:
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'error')

    return render_template('add_user.html')

@app.route('/users')
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
