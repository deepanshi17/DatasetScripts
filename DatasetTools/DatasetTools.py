from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.base import runTouchApp
from pathlib import Path
import shutil
import json
import os
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.properties import NumericProperty
import random
from jsonmerge import merge


class MainMenu(Screen):
    name = StringProperty('main_menu')


class OtherMenu(Screen):
    name = StringProperty('other_menu')


class MergeMenu(Screen):
    name = StringProperty('merge_menu')


class RootWidget(Widget):
    state = StringProperty('set_main_menu_state')
    screen_manager = ObjectProperty(None)
    files = StringProperty('')

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

    def on_state(self, instance, value):
        if value == 'main_menu':
            self.screen_manager.current = 'main_menu'

    def set_state(self, state, option):
        if state == 'main_menu':
            if option == 1:
                self.screen_manager.current = 'other_menu'
            if option == 2:
                self.screen_manager.current = 'merge_menu'

        if state == 'other_menu':
            self.screen_manager.current = 'main_menu'

        if state == 'merge_menu':
            self.screen_manager.current = 'main_menu'

    def merged(self, num, path1, path2, path3, path4, output):
        filepaths = [path1, path2, path3, path4]
        exists = True
        for i in range(0, int(num)):
            if not os.path.exists(filepaths[i]):
                print("Path not accessible: " + filepaths[i])
                exists = False

        if not os.path.exists(output):
            print("Path not accessible: " + output)
            exists = False

        if exists:
            shutil.copy2(path1 + '/camera.json', output)
            shutil.copy2(path1 + '/obj.ply', output)
            os.mkdir(output + '/depth/')
            os.mkdir(output + '/mask/')
            os.mkdir(output + '/rgb/')

            prev = json.load(open(filepaths[0] + '/truthData.json'))
            for i in range(1, int(num)):
                os.mkdir(output + '/tempdepth/')
                os.mkdir(output + '/tempmask/')
                os.mkdir(output + '/temprgb/')
                offset = len(prev)
                os.chdir(filepaths[i] + '/depth/')
                for x in os.listdir(filepaths[i] + '/depth/'):
                    src = x
                    shutil.copy2(src, output + '/tempdepth/')
                os.chdir(output + '/tempdepth/')
                for tempfile in os.listdir(output + '/tempdepth/'):
                    src = tempfile
                    filename = Path(tempfile).stem
                    dst = str(int(filename) + offset) + '.jpg'
                    os.rename(src, dst)
                    src = str(int(filename) + offset) + '.jpg'
                    shutil.copy2(src, output + '/depth/')
                os.chdir(filepaths[i] + '/mask/')
                for y in os.listdir(filepaths[i] + '/mask/'):
                    src = y
                    shutil.copy2(src, output + '/tempmask/')
                os.chdir(output + '/tempmask/')
                for tempfile in os.listdir(output + '/tempmask/'):
                    src = tempfile
                    filename = Path(tempfile).stem
                    dst = str(int(filename) + offset) + '.jpg'
                    os.rename(src, dst)
                    src = str(int(filename) + offset) + '.jpg'
                    shutil.copy2(src, output + '/mask/')
                os.chdir(filepaths[i] + '/rgb/')
                for z in os.listdir(filepaths[i] + '/rgb/'):
                    src = z
                    shutil.copy2(src, output + '/temprgb/')
                os.chdir(output + '/temprgb/')
                for tempfile in os.listdir(output + '/temprgb/'):
                    src = tempfile
                    filename = Path(tempfile).stem
                    dst = str(int(filename) + offset) + '.jpg'
                    os.rename(src, dst)
                    src = str(int(filename) + offset) + '.jpg'
                    shutil.copy2(src, output + '/rgb/')

                f = json.load(open(filepaths[i] + '/truthData.json'))
                for data in f:
                    data["Frame"] += offset
                prev = prev + f
                shutil.rmtree(output + '/tempdepth/')
                shutil.rmtree(output + '/tempmask/')
                shutil.rmtree(output + '/temprgb/')

            os.chdir(filepaths[0] + '/depth/')
            for image in os.listdir(filepaths[0] + '/depth/'):
                shutil.copy2(image, output + '/depth/')

            os.chdir(filepaths[0] + '/mask/')
            for image in os.listdir(filepaths[0] + '/mask/'):
                shutil.copy2(image, output + '/mask/')

            os.chdir(filepaths[0] + '/rgb/')
            for image in os.listdir(filepaths[0] + '/rgb/'):
                shutil.copy2(image, output + '/rgb/')

            open(output + '/truthData.json', "w").write(json.dumps(prev, sort_keys=True, indent=4, separators=(',', ': ')))

    def trim(self, frame, filepath, output, start, end):
        exists = True
        if not os.path.exists(output):
            print("Path not accessible: " + output)
            exists = False

        if not os.path.exists(filepath):
            print("Path not accessible: " + filepath)
            exists = False

        if exists:
            shutil.copy2(filepath + '/camera.json', output)
            shutil.copy2(filepath + '/obj.ply', output)
            os.mkdir(output + '/depth/')
            os.mkdir(output + '/mask/')
            os.mkdir(output + '/rgb/')
            f = json.load(open(filepath + '/truthData.json'))

            if start == '' or end == '':
                f = random.sample(f, int(frame))
            else:
                f = f[int(start):int(end) + 1]

            open(output + '/truthData.json', "w").write(json.dumps(f, sort_keys=True, indent=4, separators=(',', ': ')))
            for frame in f:
                shutil.copy2(filepath + '/depth/' + str(frame['Frame']) + '.png', output + '/depth/')
                shutil.copy2(filepath + '/mask/' + str(frame['Frame']) + '.png', output + '/mask/')
                shutil.copy2(filepath + '/rgb/' + str(frame['Frame']) + '.png', output + '/rgb/')


class TestApp(App):

    def build(self):
        pass


if __name__ == '__main__':
    TestApp().run()
