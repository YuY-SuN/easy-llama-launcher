from repository.llm_repository import LLMRepository
from huggingface_hub import hf_hub_download
import subprocess
import config
import os
from dto.llm_dto import LLMDTO

class LLMService:
    ## TODO: ほんとうはRepositoryはIF化すべき
    def __init__(self, llm_repo: LLMRepository):
        self.llm_repo = llm_repo

    def download_model(self, llm_dto: LLMDTO):
        # モデルのダウンロードロジック（ダミー）
        self.download_model_from_source(llm_dto.namespace, llm_dto.model_name)
        
        # リポジトリにDTOを保存
        self.llm_repo.set(llm_dto)

    def start_server(self, nickname: str):
        # ニックネームに基づくモデルでサーバーを起動するロジック（ダミー）
        llm_dto = self.llm_repo.get_by_nickname(nickname)
        if llm_dto is not None:
            self.start_model_server(llm_dto)
        else:
            raise ValueError("No model found with the given nickname")

    def download_model_from_source(self, namespace: str, model_name: str):
        print(f"Downloading model: {model_name}")
        ## TODO: 多分失敗すると何かがおきる
        hf_hub_download( repo_id=namespace, filename=model_name, local_dir="./")

    def start_model_server(self, llm_dto: LLMDTO):
        print(f"Starting server for model: {llm_dto.model_name} with nickname: {llm_dto.nickname}")
        ## TODO: configから各種パラメータを拾ってきたいところ
        process = subprocess.Popen([f'{config.llama_cpp_root}/server', '-m', llm_dto.model_name, '-c', str(config.llama_cpp_ctx), '--port', str(config.llama_cpp_port)], 
                                   stdin=subprocess.DEVNULL, 
                                   stdout=subprocess.DEVNULL, 
                                   stderr=subprocess.DEVNULL,
                                   preexec_fn=os.setpgrp)
                
