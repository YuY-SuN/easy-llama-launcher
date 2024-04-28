class LLMDTO:
    def __init__(self, model_namespace: str, model_name: str, namespace: str, nickname: str):
        self.model_namespace = model_namespace
        self.model_name = model_name
        self.namespace = namespace
        self.nickname = nickname

    def __repr__(self):
        return f"LLMDTO(model_namespace='{self.model_namespace}', model_name='{self.model_name}', namespace='{self.namespace}', nickname='{self.nickname}')"

