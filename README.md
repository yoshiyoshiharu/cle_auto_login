# 阪大CLE自動ログイン
阪大のCLEに自動ログインします。

## 使い方
まず,chromedriverをインストールしてください.

次に,pipからseleniumをインストールします.

```linux
pip install selenium
```

git cloneします.
```linux
git clone https://github.com/yoshiyoshiharu/cle_auto_login
```

cle_auto_login.pyでchromedriverへのパス,CLEのID,パスワードを編集してください.
```python:cle_auto_login.py
//
driver = webdriver.Chrome(executable_path='chromedriverへのパス')
//
USERID = 'あなたのユーザID'
PASSWORD = 'あなたのパスワード'
```

cle_auto_login.pyを実行してください.
```linux
cd cle_auto_login
python cle_auto_login.py
```

ショートカットをデスクトップに貼り,クリックするだけで実行できるようにすると便利です.
