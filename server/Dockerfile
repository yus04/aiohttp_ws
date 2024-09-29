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

# コンテナ外部からのアクセスを許可するためにポート8080を公開
EXPOSE 8080

# アプリケーションを実行
CMD ["python", "server.py"]
