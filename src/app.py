from wonda import Bot, Token

from src.blueprints import blueprints
from src.middlewares import middlewares


def init_bot() -> "Bot":
    bot = Bot(Token.from_env())
    setup_blueprints(bot)
    setup_middlewares(bot)
    return bot


def setup_blueprints(bot: Bot):
    for bp in blueprints:
        bp.load_into(bot)


def setup_middlewares(bot: Bot):
    for mw in middlewares:
        mw.load_into(bot)


bot = init_bot()
