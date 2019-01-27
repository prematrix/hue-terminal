#!/usr/bin/python3
import sys
from hue_api import Hapi


IP = "192.168.0.174"
USER = "3vpkddP3zb9UfpxvDa66YuWjr7oelUbZC-8x9z1o"
GROUP = "1"

HUE = Hapi(IP, USER, GROUP)


def main(args):
    args.pop(0)
    if not len(args) > 0:
        return HUE.lights_on()

    action = {
        'lights': ligths,
        'on': HUE.lights_on,
        'off': HUE.lights_off,
        'bri': brightness,
        'scene': scenes
    }
    return action[args[0]](args)


def ligths(args):
    hue_lights = HUE.lights()
    print("Available lights:")
    for light in hue_lights:
        state = 'on' if hue_lights[light]['state']['on'] else 'off'
        print("{} {}".format(light, state))


def brightness(args):
    if len(args) is 1:
        print("Please provide valid brightness percentage (0-100)")
        return

    bri = round((254 / 100) * int(args[1]))
    HUE.group_brightness(bri)


def scenes(args):
    raw_scenes = HUE.scenes()
    hue_scenes = {}
    index = 1
    for scene in raw_scenes:
        hue_scenes[str(index)] = scene
        index += 1
    if len(args) is 1:
        for key, value in hue_scenes.items():
            print("{}. {}".format(key, raw_scenes[value]['name']))
        return
    if len(args) is 2:
        HUE.choose_scene(hue_scenes[args[1]])


if __name__ == "__main__":
    main(sys.argv)
