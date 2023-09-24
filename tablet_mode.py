import sys
from evdev import UInput, ecodes as e, InputEvent

def set_tablet_mode(mode: int):
    """
    :param mode: pass 1 for tablet mode, 0 for laptop mode
    """

    assert mode in [0, 1], "mode must be in [0, 1]"

    cap = {
        e.EV_SW: [e.SW_TABLET_MODE]
    }

    current_mode = InputEvent(1334414993, 274296, e.EV_SW, e.SW_TABLET_MODE, 1 - mode)
    new_mode = InputEvent(1334414993, 274296, e.EV_SW, e.SW_TABLET_MODE, mode)
    with UInput(cap) as ui:
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
