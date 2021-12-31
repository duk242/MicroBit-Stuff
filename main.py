def on_mes_dpad_controller_id_microbit_evt():
    pass
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MICROBIT_EVT_ANY,
    on_mes_dpad_controller_id_microbit_evt)

def on_forever():
    pass
basic.forever(on_forever)
