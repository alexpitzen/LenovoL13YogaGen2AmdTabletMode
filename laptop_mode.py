from evdev import UInput, AbsInfo, ecodes as e, InputEvent
import time

cap = {
	e.EV_SW: [e.SW_TABLET_MODE]
}

ev = InputEvent(1334414993, 274296, e.EV_SW, e.SW_TABLET_MODE, 0)
ev2 = InputEvent(1334414993, 274296, e.EV_SW, e.SW_TABLET_MODE, 1)
with UInput(cap) as ui:
	ui.write_event(ev2)
	ui.write_event(ev)
	ui.syn()
