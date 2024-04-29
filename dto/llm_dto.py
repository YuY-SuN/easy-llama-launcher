class LLMDTO:
    def __init__(self, namespace: str, model_name: str, chat_template: str, nickname: str):
        self.namespace = namespace
        self.model_name = model_name
        self.chat_template = chat_template
        self.nickname = nickname

    def __repr__(self):
        return f"LLMDTO(namespace='{self.namespace}', model_name='{self.model_name}', chat_template='{self.chat_template}', nickname='{self.nickname}')"

