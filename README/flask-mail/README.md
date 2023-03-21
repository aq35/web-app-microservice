#### Gmailを使ってアプリケーションからメールを送信する

2段階認証後に発行したGmailのパスワード

2段階認証プロセス
[https://](https://myaccount.google.com/signinoptions/two-step-verification/enroll-welcome)

アプリ用パスワードの取得
生成ボタン押下後、パスワードが生成される。.envの MAIL_PASSWORD に設定します。


#### flaskでMailクラスのコンフィグを追加する方法は？

FlaskのMail拡張機能を使用する場合、Mailオブジェクトを作成し、Mailの設定を追加する必要があります。
```
from flask_mail import Mail

mail = Mail()
```

・Flaskのアプリケーションファクトリー関数内で、Mailオブジェクトを作成します。
```
import os

app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")
```

Mailオブジェクトに、Flaskアプリケーションを初期化します。
```
mail.init_app(app)
```
これで、MailクラスのコンフィグがFlaskアプリケーションに追加されました。

メールを送信する場合は、Mailオブジェクトのsendメソッドを使用してください。例えば、以下のようになります。
```
from flask_mail import Message

msg = Message('Subject', recipients=['recipient@example.com'])
msg.body = 'Message body'
mail.send(msg)
```

SMTPSenderRefusedエラーは、SMTPサーバーがメールを送信するユーザーまたはメールアドレスを拒否した場合に発生する可能性があります。このエラーの一般的な原因としては、次のことが考えられます。

認証情報が誤っている：メールを送信するために使用する認証情報が正しくない場合、SMTPサーバーは送信を拒否する場合があります。認証情報を確認してください。
送信元アドレスが間違っている：送信元アドレスが誤っている場合、SMTPサーバーは送信を拒否する場合があります。送信元アドレスを確認してください。
メールアドレスがブロックされている：SMTPサーバーが、送信しようとしているメールアドレスをブロックしている場合、このエラーが発生する可能性があります。SMTPサーバーの設定を確認してください。
ポートがブロックされている：SMTPサーバーが使用するポートがブロックされている場合、このエラーが発生する可能性があります。ポート番号を確認して、ファイアウォールやその他のセキュリティ設定でブロックされていないことを確認してください。