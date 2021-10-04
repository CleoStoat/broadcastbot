from helpers.command_helpers import CommandData
from service_layer.commands_handlers.broadcast import broadcast_cmd
from service_layer.commands_handlers.start import start_cmd
from service_layer.commands_handlers.stop import stop_cmd
from service_layer.commands_handlers.add_staff import add_staff_cmd
from service_layer.commands_handlers.del_staff import del_staff_cmd


COMMANDS = [
    CommandData(
        callback=broadcast_cmd,
        name="retransmitir",
        description="Retransmite un mensaje",
    ),
    CommandData(
        callback=start_cmd,
        name="iniciar_retransmisor",
        description="Inicia el bot",
    ),
    CommandData(
        callback=add_staff_cmd,
        name="retranmisor_agrega_staff",
        description="Agrega un usuario al staff",
    ),
    CommandData(
        callback=del_staff_cmd,
        name="retranmisor_borra_staff",
        description="Borra un usuario del staff",
    ),
    CommandData(
        callback=stop_cmd,
        name="detener_retransmisor",
        description="Detener retransimsión en este chat",
    ),
]
