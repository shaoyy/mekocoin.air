# -*- encoding=utf8 -*-
__author__ = "hasee"

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from airtest.core.api import *

auto_setup(__file__)

def lookOnce():
    sleep(1)
    touch(Template(r"tpl1559389000627.png", record_pos=(0.329, 0.652), resolution=(1080, 1920)))
    sleep(0.8)
    touch(Template(r"tpl1559389026344.png", record_pos=(0.356, 0.297), resolution=(1080, 1920)))
    sleep(10)
    finded = False
    while(finded == False):
        sleep(1)
        finded = exists(Template(r"tpl1559389093366.png", record_pos=(0.4, 0.135), resolution=(1080, 1920)))
    touch(Template(r"tpl1559389124623.png", record_pos=(0.398, 0.135), resolution=(1080, 1920)))
    sleep(0.3)
    touch(Template(r"tpl1559389151158.png", record_pos=(0.006, 0.372), resolution=(1080, 1920)))
    keyevent("BACK")
    return None

while(True):
    lookOnce()

