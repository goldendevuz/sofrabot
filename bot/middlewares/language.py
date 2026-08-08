from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from asgiref.sync import sync_to_async

from bot.enums.language import Language
from webhook.models import BotUser


class I18nMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Awaitable[Any]:

        if not event.from_user:
            return await handler(event, data)

        telegram_id = event.from_user.id

        user = await sync_to_async(
            BotUser.objects.filter(user_id=telegram_id).first
        )()

        if user:
            # DB dan string keladi → Enum ga aylantiramiz
            language = Language(user.language)
        else:
            language = Language.from_locale(
                event.from_user.language_code
            )

            await sync_to_async(BotUser.objects.create)(
                user_id=telegram_id,
                name=event.from_user.full_name,
                username=event.from_user.username,
                language=language.value,  # DB ga string
            )

        # HAR DOIM Enum beramiz
        data["language"] = language

        return await handler(event, data)
