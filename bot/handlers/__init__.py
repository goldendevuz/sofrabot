from aiogram import Router

from bot.filters import ChatPrivateFilter
from bot.middlewares.language import I18nMiddleware


def setup_routers() -> Router:
    from .users import admin, start, help, echo
    from .errors import error_handler

    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating
    start.router.message.filter(ChatPrivateFilter(chat_type=["private"]))
    start.router.message.middleware(I18nMiddleware())
    start.router.callback_query.middleware(I18nMiddleware())

    router.include_routers(admin.router, start.router, help.router, echo.router, error_handler.router)

    return router
