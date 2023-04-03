import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, abort
)

from api.models.user import User

from pymysql.err import IntegrityError

auth_router = Blueprint('auth', __name__, url_prefix='/auth')


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
    username = request.json.get('username')
    password = request.json.get('password')

    error = None

    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'

    if error is None:
        # Userテーブルから、ユーザー名が引数で与えられたユーザーを取得する
        user = User.user_by_username(username=username)
        if user:
            error = f"会員登録 {username} は既に存在します。"
        else:
            try:
                user = User(username=username, password=password)
                user.save()
            except IntegrityError:
                error = f"会員 {username} は既に存在します。"
            else:
                return jsonify({"message": "会員登録に成功しました。"}), 201

    return jsonify({"error": error}), 400


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
