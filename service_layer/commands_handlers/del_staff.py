from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from service_layer.unit_of_work import AbstractUnitOfWork
import config


def del_staff_cmd(
    update: Update, context: CallbackContext, uow: AbstractUnitOfWork
) -> None:
    if update.effective_user.id != config.get_bot_owner_user_id():
        # Si no es el dueño, no le responde nada y retorna
        return

    if update.effective_message.reply_to_message is None:
        text = "Usa el comando respondiendo a un mensaje de la persona a la cual quieres quitar del staff"
        update.effective_message.reply_text(text=text, quote=True)
        return

    user_id = update.effective_message.reply_to_message.from_user.id
    user_fullname = update.effective_message.reply_to_message.from_user.full_name

    with uow:
        result = uow.repo.del_staff(user_id)

        if result == False:
            text = "El usuario no era parte del staff"
            update.effective_message.reply_text(text=text, quote=True)
        else:
            text = f"({user_id}) {user_fullname} quitado del staff correctamente"
            update.effective_message.reply_text(text=text, quote=True)

        uow.commit()