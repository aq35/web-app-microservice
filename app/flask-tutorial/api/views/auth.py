import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, abort
)

from api.models.user import User
from pymysql.err import IntegrityError
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, ValidationError

auth_router = Blueprint('auth', __name__, url_prefix='/auth')


class RegistrationForm(FlaskForm):
    username = StringField('ユーザー名', validators=[InputRequired(message='ユーザー名は必須項目です。')])
    password = PasswordField('パスワード', validators=[
        InputRequired(message='パスワードは必須項目です。'),
        Length(min=8, message='パスワードは8文字以上で入力してください。')
    ])

    def validate_username(self, field):
        if User.user_by_username(username=field.data):
            raise ValidationError(f'会員登録 {field.data} は既に存在します。')


@auth_router.errorhandler(400)  # 追加
def error_handler(err):
    res = jsonify({
        'error': {'message': err.description['message']},
        'code': err.code
    })
    return res, err.code


# 登録（Register)
@auth_router.route('/register', methods=['POST'])
def register_api():
    data = request.get_json()
    form = RegistrationForm(data=data)
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        user.save()
        return jsonify({"success_message": "会員登録に成功しました。"}), 201
    else:
        return jsonify({"errors": form.errors,
                        "error_messages": ["入力項目を見直してください。"],
                        "request.form": request.form
                        }), 400


@auth_router.route('/register', methods=['GET'])
def register_page():
    return render_template('auth/register.html')


# ログイン
@auth_router.route('/login', methods=['POST'])
def login_api():
    username = request.json.get('username')
    password = request.json.get('password')
    error = None

    # Userテーブルから、ユーザー名が引数で与えられたユーザーを取得する
    user = User.user_by_username(username=username)

    if user is None:
        error = 'Incorrect username.'
    elif not user.check_password(password):
        error = 'Incorrect password.'

    if error is None:
        session.clear()
        session['user_id'] = user.id
        return jsonify({"message": "Login successful"}), 200

    return jsonify({"error": error}), 400


@auth_router.route('/login', methods=['GET'])
def login_page():
    return render_template('auth/login.html')


# ログアウト
@auth_router.route('/logout', methods=['POST'])
def logout_api():
    session.clear()
    return jsonify({"message": "Logout successful"}), 200


@auth_router.route('/logout', methods=['GET'])
def logout_page():
    return redirect(url_for('index'))


@auth_router.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.user_by_user_id(user_id)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login_page'))

        return view(**kwargs)

    return wrapped_view
