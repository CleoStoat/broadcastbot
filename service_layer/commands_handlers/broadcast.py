from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from service_layer.unit_of_work import AbstractUnitOfWork
import config


def broadcast_cmd(
    update: Update, context: CallbackContext, uow: AbstractUnitOfWork
) -> None:
    # Comprobar que es el dueño o es parte del staff
    user_id = update.effective_user.id
    staff_members = []

    with uow:
        staff_members = uow.repo.get_staff()
        uow.commit()

    if not (user_id == config.get_bot_owner_user_id() or user_id in [x.user_id for x in staff_members]):
        # Responder que no es parte del staff
        text = "Debes ser parte del staff para usar este comando"
        update.effective_message.reply_text(text=text, quote=True)
        return
    
    if update.effective_message.reply_to_message is None:
        text = "Usa el comando respondiendo al mensaje que quieres retransmitir"
        update.effective_message.reply_text(text=text, quote=True)
        return

    with uow:
        for chat in uow.repo.get_chats():
            try:
                context.bot.copy_message(                
                    chat_id=chat.chat_id, 
                    from_chat_id=update.effective_chat.id,
                    message_id=update.effective_message.reply_to_message.message_id,
                )
            except Exception:
                pass
        uow.commit()

    
    
    
    
