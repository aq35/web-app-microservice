import os
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, flash
)
# メール送信拡張:flask-mail
from flask_mail import Mail, Message

# メールバリデーション拡張:email-validator
from email_validator import EmailNotValidError, validate_email

from flaskr.auth import login_required

bp = Blueprint('contact', __name__)


@bp.route('/contact', methods=('GET', 'POST'))
@login_required
def create():

    return render_template('contact/create.html')


@bp.route("/contact/complete", methods=["GET", "POST"])
@login_required
def contact_complete():
    if request.method == "POST":
        # form属性を使ってフォームの値を取得する
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # 入力チェック
        is_valid = True
        if not username:
            flash("ユーザ名は必須です")
            is_valid = False

        if not email:
            flash("メールアドレスは必須です")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式で入力してください")
            is_valid = False

        if not description:
            flash("問い合わせ内容は必須です")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact.create"))

        # 問い合わせ完了エンドポイントへリダイレクトする
        flash("問い合わせ内容はメールにて送信しました。問い合わせありがとうございます。")

        # contactエンドポイントへリダイレクトする
        return redirect(url_for("contact.contact_complete"))
    return render_template("contact/complete.html")


def send_email(to, subject, template, **kwargs):
    """メールを送信する関数"""
    # msg = Message(subject, recipients=[to])
    # msg.body = render_template(template + ".txt", **kwargs)
    # msg.html = render_template(template + ".html", **kwargs)
    # mail.send(msg)
