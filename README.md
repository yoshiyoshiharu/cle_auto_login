# 阪大CLE自動ログイン
阪大のCLEに自動ログインします。

# 使い方
まず,chromedriverをインストールしてください.

次に,pipからseleniumをインストールします.

```linux
pip install selenium
```

```linux
git clone https://github.com/yoshiyoshiharu/cle_auto_login
```

IDとパスワードを編集してください.
```python
USERID = 'あなたのユーザID'
PASSWORD = 'あなたのパスワード'
```

cle_auto_login.pyを実行してください.
```linux
cd cle_auto_login
python cle_auto_login.py
```

ショートカットをデスクトップに貼り,クリックするだけで実行できるようにすると便利です.
