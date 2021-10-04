from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from service_layer.unit_of_work import AbstractUnitOfWork
import config


def start_cmd(
    update: Update, context: CallbackContext, uow: AbstractUnitOfWork
) -> None:
    if update.effective_user.id != config.get_bot_owner_user_id():
        # Si no es el dueño, no le responde nada y retorna
        return

    chat_id = update.effective_chat.id

    with uow:
        result = uow.repo.add_chat(chat_id)

        if result == False:
            text = "Ya se encontraba iniciado"
            update.effective_message.reply_text(text=text, quote=True)
        else:
            text = "Inició correctamente"
            update.effective_message.reply_text(text=text, quote=True)

        uow.commit()