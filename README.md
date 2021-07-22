# Discord-Processngbot
discordのチャットに`!processing`コマンドを付けてProcessingのコードを書くと、コードを自動的に取得してスケッチを実行し、出力をgifにして数秒程度のプレビューとして返してくれるbotです。

# 動作環境
- Python 3.9.5
- Processing 3.5.3

    (Processingは環境変数を通しておくProcessing-javaが実行できるようにする必要があります。)

# 使い方
1. botソースコードのルートにconfig.iniを作成し
    ```
    [TOKEN]
    token="ここに取得したbotトークンを入れる"
    ```
    と記述します。

2. `processing-discord.py`を実行します。コンソールに`logged-in as (bot名)`と表示されれば成功です。

3. Discordチャンネルに`!processing`と入れ、改行後にソースコードを入力します。
4. botが自動でコマンドに反応し、ソースコードを取得した後コマンドラインを通じてスケッチを実行します。スケッチの録画には少し時間がかかりますのでお待ち下さい。
5.スケッチの録画が完了するとbotが"Here is a code result"というメッセージと共にスケッチのGIFサンプルをチャンネルへ添付します。