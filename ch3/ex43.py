#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  ex43.py
@Time    :  2018/9/19 20:12
"""
'基本的面向对象分析和设计'

'分析一个简单的游戏引擎' \
'Gothons from Planet Percal #25'

'>1. 写或画出这个问题' \
'外星人乘坐一个宇宙飞船入侵,我们的英雄需要通过一个迷宫似的房间击败他们,然后他才能逃入一个逃生舱到达下面的行星。游戏将更像一个有着文本输出和有趣的死法的Zork或冒险类型游戏。游戏将包括一个引擎运行充满房间或场景的地图。 当玩家进入房间，每个房间将打印自己的描述,然后告诉引擎运行下一个地图。' \
'接下来描述每个场景：' \
'Death : 这是玩家死亡的场景，应该是有趣的。' \
'Central Corridor : 这是游戏的起点，在这里已经有一个外星人等待英雄的到来，它们需要被一个玩笑打败。' \
'Laser Weapon Armory : 这是英雄得到了中子弹获得的逃生舱之前要炸毁的船。它有一个需要英雄猜数的键盘。' \
'The Bridge : 和外星人战斗的另一个场景，英雄防止炸弹的地方。' \
'Escape Pod : 英雄逃脱的场景，但是需要英雄找对正确的逃生舱' \

'>2. 提取关键概念并研究他们' \
'Alien' \
'Player' \
'Ship' \
'Maze' \
'Room' \
'Scene' \
'Gothon' \
'Escape Pod' \
'Planet' \
'Map' \
'Engine' \
'Death' \
'Central Corridor（中央走廊）' \
'Laser Weapon Armory（激光武器兵工厂）' \
'The Bridge'

'>3. 创造一个层次结构的类和对象映射的概念' \
'- Map (-next_scene - opening_scene)' \
'- Engine: play' \
'- Scene: enter' \
'   - Death' \
'   - Central Corridor' \
'   - Laser Weapon Armory' \
'   - The Bridge' \
'   - Escape Pod'

'>4. 编码类和测试代码并运行它们'
'''
class Scene(object):
    def enter(self):
        pass

class Engine(object):
    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):
    def enter(self):
        pass

class CentralCorridor(Scene):
    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass
    def next_scene(self, scene_name):
        pass
    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
'''

'>5. 重复并精炼'

'>6. 自顶向下和自下而上'
'- 取一小块问题，编写一些代码，并让它勉强运行' \
'- 完善代码，将其转换成一些更正式的包含类的自动化测试的代码' \
'- 提取其中的关键概念，并尝试找出研究它们' \
'- 写出到底发生了什么的描述' \
'- 继续完善代码，也可能是把它扔掉，并重新开始' \
'- 移动到其他问题上，重复步骤'

'>7. “来自Percal 25号行星的哥顿人”的代码'
from sys import exit
from random import randint

class Scene(object):    # 基础类Scene（场景）
    def enter(self):
        print('This scene is not yet configured. Subclass it and implement enter().')
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

# 第一个场景：Death
class Death(Scene):
    quips = [
        'You died. You kinda suck at this.',
        'Your mom would be proud...if she were smarter.',
        'Such a luser.',
        'I have a small puppy that\'s better at this.'
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)

# 第二个场景：CentralCorridor
class CentralCorridor(Scene):
    def enter(self):
        print('The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew.')
        print('You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory,')
        print('put it in the bridge, and blow the ship up after getting into an escape pod.')
        print('\n')
        print('You\'re running down the central corridor to the Weapons Armory when a Gothon jumps out, ')
        print('red scaly skin, dark grimy teeth, and evil clown costume flowing around his hate filled body.')
        print('He\'s blocking the door to the Armory and about to pull a weapon to blast you.')

        action = input('> ')

        if action == 'shoot!':
            print('Quick on the draw you yank out your blaster and fire it at the Gothon.')
            print('His clown costume is flowing and moving around his body, which throws off your aim.')
            print('Your laser hits costume but missed him entirely.')
            print('This completely ruins his brand new costume his mother brought him,')
            print('which makes him fly into an insane rage and blast you repeatedly in the face until you are dead.')
            print('Then he eats you.')
            print('death')









