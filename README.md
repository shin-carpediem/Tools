## 開発環境

### アーキテクチャ

![アーキテクチャ](https://user-images.githubusercontent.com/71208265/235643221-13511c53-6f23-407b-83b1-ef0aca5a8a02.png)

### 使用技術

- 言語: Python3.9
- デプロイターゲット: [Google App Engine(GAE)](https://cloud.google.com/appengine?hl=ja)
- 依存データベース: [Firebase](https://firebase.google.com/?hl=ja)

- パッケージマネージャ:
  | パッケージマネージャ名 | 用途 |
  | :---- | :---- |
  | [Pipenv](https://pipenv.pypa.io/en/latest/) | 開発環境でのパッケージの管理、仮想環境の構築 |
  | [pip](https://www.python.jp/install/windows/pip.html) | 本番環境(GAE)でのパッケージの管理 |

- 主な依存パッケージ:
  | 依存パッケージ名 | 用途 |
  | :---- | :---- |
  | [Bottle](https://bottlepy.org/docs/dev/tutorial.html) | アプリフレームワーク |
  | [ABC](https://docs.python.org/ja/3/library/abc.html) | インターフェース定義 |
  | [mypy](https://mypy.readthedocs.io/en/latest/index.html) | 型チェック |
  | [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) | テンプレートエンジン |
  | [firebase-admin-python](https://firebase.google.com/docs/reference/admin/python) | Firebase SDK |

### 環境構築の手順

クローンしたリポジトリ直下に、新たに `tmp` ディレクトリ、`resource` ディレクトリを作成してください。

クローンしたリポジトリ直下に、`.env` ファイル、`secret.yaml` ファイルを置いてください。

`resource` ディレクトリ内に、`hoge-dev.json`, `hoge-prod.json` ファイルを置いてください。

パッケージマネージャ `Pipenv` で仮想環境を構築するため、もう一つのパッケージマネージャ `pip` で Pipenv をインストールします。

```
$ pip install pipenv
```

Pipenv から仮想環境に入ります。

```
$ pipenv shell
```

`Pipfile.lock` に記載されている依存パッケージをインストールします。

```
$ pipenv install
```

ローカルで Bottle アプリケーションを立ち上げます。

```
$ python main.py
```

### デプロイ手順

以下コマンドを実行してください。

```
$ gcloud app deploy
```
