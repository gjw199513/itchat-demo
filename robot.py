# -*- coding:utf-8 -*-

from wx_robot.handler import MonitorHandler, XiaodouHandler
from wx_robot.robot import WxRobot


if __name__ == '__main__':
    robot = WxRobot(hot_reload=True)

    monitor = MonitorHandler()
    robot.register_handler(monitor)

    xiaodou_key = 'RU85Mj04WFl3dkZQWUZpUj1Zc2lHN0ZhY2hRQUFBPT0'
    xiaodou = XiaodouHandler(xiaodou_key)
    robot.register_handler(xiaodou)

    robot.run()

