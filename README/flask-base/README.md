#### Flaskのアプリケーションファクトリー関数内とは

Flaskアプリケーションを動的に生成するための関数のことです。
この方法を使用すると、複数のアプリケーションインスタンスを生成することができます。
また、アプリケーションの構成を一元化し、柔軟性を高めることができます。
通常
```
from flask import Flask

app = Flask(__name__)
```

アプリケーションファクトリー関数を使用
```
from flask import Flask

def create_app():
    app = Flask(__name__)
    # ルートやテンプレート、エラーハンドリングなどを定義する
    return app
```