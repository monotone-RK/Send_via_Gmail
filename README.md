Send_via_Gmail
==============
Gmailを使ってメールを送るPythonスクリプトです．python 2系対象です．

Gmail2段階認証を有効にしている方は，アプリケーション固有のバスワード
を発行する必要があります．

Setup
---------------------------------------
 1. python 2系をインストールしてください
 2. あなたのgmailアドレス，パスワード(FROM)を設定して下さい
 3. 送信先のアドレス(TO)を入力して下さい
 4. メール件名，本文に使用したい文字コード(to_enc)を入力してください．ISO-2022-JPだと日本語対応になります．

###Usage
    python gmailsender.py [option]

    opthions:
    -h, --help     show this help message and exit
    -v, --version  Show the version
    -l, --loop     Send message repeatedly
