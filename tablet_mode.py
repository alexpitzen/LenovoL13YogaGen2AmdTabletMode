import sys
from time import sleep
from evdev import UInput, ecodes as e, InputEvent, AbsInfo

def set_tablet_mode(mode: int):
    """
    :param mode: pass 1 for tablet mode, 0 for laptop mode
    """

    assert mode in [0, 1], "mode must be in [0, 1]"

    cap = {
        e.EV_SW: [e.SW_TABLET_MODE],
        e.EV_ABS: [
            (e.ABS_X, AbsInfo(0, -512, 512, 0, 0, 0)),
            (e.ABS_Y, AbsInfo(0, -512, 512, 0, 0, 0)),
            (e.ABS_Z, AbsInfo(0, -512, 512, 0, 0, 0)),
        ],
    }

    current_mode = InputEvent(1334414993, 274296, e.EV_SW, e.SW_TABLET_MODE, 1 - mode)
    new_mode = InputEvent(1334414993, 274296, e.EV_SW, e.SW_TABLET_MODE, mode)
    with UInput(cap) as ui:
        if mode == 0:
            # TODO do something better than guessing when iio-sensor-proxy will register our input
            sleep(0.5)
            ui.write_event(InputEvent(1334414993, 274296, e.EV_ABS, e.ABS_X, 0))
            ui.write_event(InputEvent(1334414993, 274296, e.EV_ABS, e.ABS_Y, -256))
            ui.write_event(InputEvent(1334414993, 274296, e.EV_ABS, e.ABS_Z, 0))
            ui.syn()
            # TODO do something better than guessing when iio-sensor-proxy will register our event
            sleep(0.5)

        # Setting back to laptop mode doesn't work if we don't
        # first set to tablet mode again for some reason
        ui.write_event(current_mode)
        ui.write_event(new_mode)
        ui.syn()


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ["0", "1"]:
        print("Usage: tablet_mode.py <mode>", file=sys.stderr)
        print("\tmode: 1 for tablet mode, 0 for laptop mode", file=sys.stderr)

    mode = int(sys.argv[1])
    set_tablet_mode(mode)
