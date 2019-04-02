# 動かし方

ソースを落としたらプロジェクトディレクトリの直下にて以下を実施する。

- 仮想環境の作成

```bash
$ pipenv install
```

- 仮想環境に入る

```bash
$ pipenv shell
```

- DBのマイグレーション

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- 簡易サーバの起動

```bash
$ python manage.py runserver
```

コマンド実行後に表示されるURLでアプリにアクセスできる。