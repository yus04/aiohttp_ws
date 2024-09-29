# ベースイメージを指定 (公式のPythonイメージを使用)
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルをコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . .

# アプリケーションを実行
ENTRYPOINT ["python", "client.py"]

# CMD でデフォルトの引数を指定
CMD ["--address", "127.0.0.1:8080"]
