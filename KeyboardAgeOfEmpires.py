import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

key = Keyboard(usb_hid.devices)
mou = Mouse(usb_hid.devices)

"""
https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/master/adafruit_hid/keycode.py
Layout
rechts: 22 - 18 - 19 - 17 - 16
links: 9 - 13 - 12 - 14 - 15
"""
btn_9 = digitalio.DigitalInOut(board.GP9)
btn_9.direction = digitalio.Direction.INPUT
btn_9.pull = digitalio.Pull.DOWN

btn_13 = digitalio.DigitalInOut(board.GP13)
btn_13.direction = digitalio.Direction.INPUT
btn_13.pull = digitalio.Pull.DOWN

btn_12 = digitalio.DigitalInOut(board.GP12)
btn_12.direction = digitalio.Direction.INPUT
btn_12.pull = digitalio.Pull.DOWN

btn_14 = digitalio.DigitalInOut(board.GP14)
btn_14.direction = digitalio.Direction.INPUT
btn_14.pull = digitalio.Pull.DOWN

btn_15 = digitalio.DigitalInOut(board.GP15)
btn_15.direction = digitalio.Direction.INPUT
btn_15.pull = digitalio.Pull.DOWN

btn_22 = digitalio.DigitalInOut(board.GP22)
btn_22.direction = digitalio.Direction.INPUT
btn_22.pull = digitalio.Pull.DOWN

btn_18 = digitalio.DigitalInOut(board.GP18)
btn_18.direction = digitalio.Direction.INPUT
btn_18.pull = digitalio.Pull.DOWN

btn_19 = digitalio.DigitalInOut(board.GP19)
btn_19.direction = digitalio.Direction.INPUT
btn_19.pull = digitalio.Pull.DOWN

btn_17 = digitalio.DigitalInOut(board.GP17)
btn_17.direction = digitalio.Direction.INPUT
btn_17.pull = digitalio.Pull.DOWN

btn_16 = digitalio.DigitalInOut(board.GP16)
btn_16.direction = digitalio.Direction.INPUT
btn_16.pull = digitalio.Pull.DOWN

# save last pressed button
# so a double press happens after a short time
global pressed_btn_old
global pressed_count
pressed_btn_old = None
pressed_btn = None
pressed_count = 0
print("START")

def hold(btn):
    global pressed_btn_old
    global pressed_count
    pressed_btn = btn
    if pressed_btn == -1:
        # no button is pressed
        pressed_count = 0
        pressed_btn_old = None
        return None
    if pressed_btn_old == pressed_btn:
        # same button
        # already send keycode once
        pressed_count += 1
    else:
        # different button
        # send keycode
        pressed_count = 0
        pressed_btn_old = pressed_btn
        return True
    if pressed_count >= 5:
        # holding key long engouh
        pressed_btn_old = pressed_btn
        return True
    else:
        pressed_btn_old = pressed_btn
        return False

global pressed
pressed = 0
def press_release():
    global pressed
    if pressed == 0:
        pressed = 1
    else:
        pressed = 0
    return pressed

while True:
    if btn_9.value or btn_13.value or btn_12.value or btn_14.value or btn_15.value or btn_22.value or btn_18.value or btn_19.value or btn_17.value or btn_16.value:
        # any key is true
        # check which one
        
        if btn_9.value: #SHIFT
            # shift
            print("press")
            key.press(Keycode.LEFT_SHIFT)
            #while btn_9.value:
            #    print("here")
            #    if btn_22.value:
                    # build menu
            #        key.send(Keycode.Q)
                    # build house
            #        key.send(Keycode.Q)
            #    if btn_18.value:
                    # build menu
            #        key.send(Keycode.Q)
                    # build farm
            #       key.send(Keycode.A)
            while btn_9.value:
                pass # hold shift while its pressed. Not possible to press other keys
            print("release")
            key.release(Keycode.LEFT_SHIFT)
        if btn_13.value:
            if hold(13):
                # last notification
                key.send(Keycode.A)
        if btn_12.value:
            if hold(12):
                # towncenter
                key.send(Keycode.SPACE)
        if btn_14.value:
            if hold(14):
                # light fire
                key.send(Keycode.ALT, Keycode.F)
        if btn_15.value:
            if hold(15):
                # fire
                key.send(Keycode.G)
            
        if btn_22.value:
            if hold(22):
                # build menu
                key.send(Keycode.Q)
                # build house
                key.send(Keycode.Q)
        if btn_18.value:
            if hold(18):
                # build menu
                key.send(Keycode.Q)
                # build farm
                key.send(Keycode.A)
        if btn_19.value:
            if hold(19):
                # non-working villager
                key.send(Keycode.E)
        if btn_17.value:
            if hold(17):
                # place in house
                key.send(Keycode.T)
        if btn_16.value:
            if hold(16):
                # key and mouse pressed
                # 1. town center SPACE
                # 2. create villager W
                # 3. create villager W
                key.send(Keycode.SPACE)
                key.send(Keycode.W)
                key.send(Keycode.W)
                key.send(Keycode.W)
                # 4. non-working villager E - snaps view to villager, have mouse in the middle, little left
                # 5. build menu Q
                # 6. house Q
                # 7. left mouse click build house
                # 8. non-working villager E - snaps view to villager, have mouse in the middle, little left
                # 9. build menu Q
                # 10. house Q
                # 11. left mouse click build house
                # 12. non-working villager E - snaps view to villager, have mouse in the middle, little left
                # 13. build menu Q
                # 14. house Q
                # 15. left mouse click build house
                u = 0
                while u <= 3:
                    u += 1
                    key.send(Keycode.E)
                    key.send(Keycode.Q)
                    key.send(Keycode.Q)
                    mou.click(Mouse.LEFT_BUTTON)
    else:
         hold(-1)
    time.sleep(0.05)


