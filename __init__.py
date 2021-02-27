from mycroft import MycroftSkill, intent_file_handler
import subprocess

class MycroftFoxyTurtleInit(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('init.turtle.foxy.mycroft.intent')
    def handle_init_turtle_foxy_mycroft(self, message):
        self.speak_dialog('init.turtle.foxy.mycroft')
        subprocess.call((["ros2 run turtlesim turtlesim_node"]),shell=True)

def create_skill():
    return MycroftFoxyTurtleInit()

