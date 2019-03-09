# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import requests

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Rocket" to a unique name for your skill
class RocketSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(RocketSkill, self).__init__(name="RocketSkill")

    @intent_handler(IntentBuilder("").require("Launch").require("Rocket"))
    def handle_launch_rocket_intent(self, message):
        requests.get('http://10.0.0.149:9080/api.php?action=brightness&value=240')
        self.speak_dialog("deployed")

def create_skill():
    return RocketSkill()
