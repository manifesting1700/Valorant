import tkinter as tk
import json, os, keyboard, time, requests, base64, ctypes, sys, wmi, datetime
from io import BytesIO
from PIL import ImageGrab, ImageTk, Image
from pynput import mouse
from ctypes import WinDLL
from cheese import *

XYZ_BUILD = "ARDUINO"

ABC = {
    '1': "0x31",
    '2': "0x32",
    '3': "0x33",
    '4': "0x34",
    '5': "0x35",
    '6': "0x36",
    '7': "0x37",
    '8': "0x38",
    '9': "0x39",
    '0': "0x30",
    'a': "0x41",
    'b': "0x42",
    'c': "0x43",
    'd': "0x44",
    'e': "0x45",
    'f': "0x46",
    'g': "0x47",
    'h': "0x48",
    'i': "0x49",
    'j': "0x4A",
    'k': "0x4B",
    'l': "0x4C",
    'm': "0x4D",
    'n': "0x4E",
    'o': "0x4F",
    'p': "0x50",
    'q': "0x51",
    'r': "0x52",
    's': "0x53",
    't': "0x54",
    'u': "0x55",
    'v': "0x56",
    'w': "0x57",
    'x': "0x58",
    'y': "0x59",
    'z': "0x5A",
    'tab': "0x09",
    'caps_lock': "0x14",
    'shift_l': "0xA0",
    'shift_r': "0xA1",
    'control_l': "0xA2",
    'control_r': "0xA3",
    'alt_l': "0xA4",
    "alt_r": "0xA5",
    "space": "0x20"
}

class A:
    def __init__(self, b, c, d, e, f, g, h, i):
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i

        self.j = []

        self.k()

        self.l = self.c + self.d / 2
        self.m = self.e + self.f / 2

        self.n = self.b.create_text(self.l, self.m, text=self.h, fill="white",
                                    font=("Helvetica", 12))

        self.b.bind("<Button-1>", self.o)

    def k(self):
        self.j.append(self.b.create_rectangle(
            self.c + self.f, self.e,
            self.c + self.d - self.f, self.e + self.f,
            fill=self.g,
            outline=self.g
        ))
        self.j.append(self.b.create_rectangle(
            self.c, self.e + self.f,
            self.c + self.d, self.e + self.f - self.f,
            fill=self.g,
            outline=self.g
        ))

        self.j.append(self.b.create_arc(
            self.c, self.e,
            self.c + self.f * 2, self.e + self.f * 2,
            start=90, extent=90,
            fill=self.g,
            outline=self.g
        ))
        self.j.append(self.b.create_arc(
            self.c + self.d - self.f * 2, self.e,
            self.c + self.d, self.e + self.f * 2,
            start=0, extent=90,
            fill=self.g,
            outline=self.g
        ))
        self.j.append(self.b.create_arc(
            self.c, self.e + self.f - self.f * 2,
            self.c + self.f * 2, self.e + self.f,
            start=180, extent=90,
            fill=self.g,
            outline=self.g
        ))
        self.j.append(self.b.create_arc(
            self.c + self.d - self.f * 2, self.e + self.f - self.f * 2,
            self.c + self.d, self.e + self.f,
            start=270, extent=90,
            fill=self.g,
            outline=self.g
        ))

    def o(self, p):
        if self.q(p):
            print("Button Clicked!")
            time.sleep(0.5)
            self.r()

    def r(self):
        self.b.focus_set()
        self.b.bind("<Key>", self.s)
        self.t = mouse.Listener(on_click=self.u)
        self.t.start()

    def s(self, p):
        if p.keysym.lower() == 'escape':
            self.b.unbind("<Key>")
            self.t.stop()
        else:
            v = p.keysym.lower()
            w = v2c(v)
            if w != -1:
                self.b.unbind("<Key>")
                self.t.stop()
                print(f"Hotkey set to: {v} (VK Code: {w})")
                self.v(w)
                self.i(w)
            else:
                print("cock")

    def u(self, a, b, c, d):
        if not d:
            return

        # mapped mouse keys
        x = {
            mouse.Button.left: "0x01",
            mouse.Button.right: "0x02",
            mouse.Button.middle: "0x04",
            mouse.Button.x1: "0x05",
            mouse.Button.x2: "0x06",
        }

        y = {
            mouse.Button.left: "left",
            mouse.Button.right: "right",
            mouse.Button.middle: "middle",
            mouse.Button.x1: "x1",
            mouse.Button.x2: "x2",
        }.get(c, "unknown")

        w = x.get(c, -1)
        if w != -1:
            v = f"Mouse {y}"
            keyboard.unhook_all()
            self.t.stop()
            print(f"Hotkey set to: {v} (VK Code: {w})")
            self.v(w)
            self.i(w)

    def v(self, z):
        self.h = z
        self.b.itemconfig(self.n, text=self.h)

    def q(self, p):
        return self.c <= p.x <= self.c + self.d and self.e <= p.y <= self.e + self.f

def v2c(a):
    return ABC.get(a, -1)
