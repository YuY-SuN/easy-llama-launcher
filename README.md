## Japanese README: Easy Chat Llama CPP

### 概要
Easy Chat Llama CPPは、モデル管理とサーバー起動をサポートするPythonベースのアプリケーションです。ユーザーは、Hugging Faceからモデルをダウンロードし、指定したモデルでサーバーを起動することができます。

### 機能
- **モデルのダウンロード**: Hugging Faceから任意のモデルをダウンロードする。
- **サーバーの起動**: ダウンロードしたモデルを使用してサーバーを起動する。

### 使用方法
1. **モデルのダウンロード**
    ```
    python app.py download --chat-template [chat templateのnamespace] --namespace [ダウンロードするnamespace] --modelname [ダウンロードするファイル名] --nickname [ニックネーム]
    ```
2. **サーバーの起動**
    ```
    python app.py server --nickname [起動するモデル名またはニックネーム]
    ```

### 設定ファイル
- `llama_cpp_root`: Llama CPPのルートディレクトリ
- `llama_cpp_ctx`: コンテキストの大きさ
- `llama_cpp_port`: サーバーのポート番号
- `llm_db_name`: データベースファイルのパス

### リポジトリ
- `LLMRepository`: モデルデータの管理

---

## English README: Easy Chat Llama CPP

### Overview
Easy Chat Llama CPP is a Python-based application that supports model management and server launching. Users can download models from Hugging Face and launch a server using the specified model.

### Features
- **Model Downloading**: Download any model from Hugging Face.
- **Server Launching**: Launch a server using the downloaded model.

### Usage
1. **Download a Model**
    ```
    python app.py download --chat-template [chat template namespace] --namespace [download namespace] --modelname [download file name] --nickname [nickname]
    ```
2. **Launch a Server**
    ```
    python app.py server --nickname [model name or nickname]
    ```

### Configuration Files
- `llama_cpp_root`: Root directory for Llama CPP
- `llama_cpp_ctx`: Size of the context
- `llama_cpp_port`: Server port number
- `llm_db_name`: Path to the database file

### Repositories
- `LLMRepository`: Manages model data


