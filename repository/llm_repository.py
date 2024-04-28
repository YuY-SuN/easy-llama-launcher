from model.llm import LLM
from dto.llm_dto import LLMDTO
from . import Session

class LLMRepository:
    def __init__(self, session: Session):
        self.session = session

    def set(self, llm_dto: LLMDTO):
        # DTOからモデルインスタンスを作成して追加
        llm = LLM(model_name=llm_dto.model_name, namespace=llm_dto.namespace, nickname=llm_dto.nickname)
        self.session.add(llm)
        self.session.commit()

    def get_by_model_name(self, model_name: str) -> LLMDTO:
        # モデル名に基づいてレコードを検索し、DTOで返す
        llm = self.session.query(LLM).filter_by(model_name=model_name).first()
        return LLMDTO(model_namespace="", model_name=llm.model_name, namespace=llm.namespace, nickname=llm.nickname) if llm else None

    def get_by_nickname(self, nickname: str) -> LLMDTO:
        # ニックネームに基づいてレコードを検索し、DTOで返す
        llm = self.session.query(LLM).filter_by(nickname=nickname).first()
        return LLMDTO(model_namespace="", model_name=llm.model_name, namespace=llm.namespace, nickname=llm.nickname) if llm else None

    def get_by_namespace(self, namespace: str) -> LLMDTO:
        # ネームスペースに基づいてレコードを検索し、DTOで返す
        llm = self.session.query(LLM).filter_by(namespace=namespace).first()
        return LLMDTO(model_namespace="", model_name=llm.model_name, namespace=llm.namespace, nickname=llm.nickname) if llm else None
