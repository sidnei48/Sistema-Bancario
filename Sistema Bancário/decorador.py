from datetime import datetime
from functools import wraps

logs = []

# Registro de Ação

def registrar_acao(func):
    @wraps(func)
    def acao(*args, **kwargs):
        agora = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        usuario = None
        if args and isinstance(args[0], dict):
            usuario = args[0].get("nome") or args[0].get("cpf", "")

        log_msg = f'{agora} | {func.__name__}' + (f' | usuario: {usuario}' if usuario else '')
        logs.append(log_msg) # registra o log da ação

        return func(*args, **kwargs)
    return acao
       