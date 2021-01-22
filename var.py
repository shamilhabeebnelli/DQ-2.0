import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    pass
else:
    from local_config import Development as Config


Var = Config
