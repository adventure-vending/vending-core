# Main.py
from time import sleep
from light_system_manager import LightSystemManager

class Main():
    def test(self):
        self.init_machine()
        print "started"
        #LightSystemManager.open_box(1)
        sleep(4)
        LightSystemManager.select_box(2)
        sleep(999)
        print "ending.."
        self.cleanup()
        print "end"

    def init_machine(self):
        LightSystemManager.setup()

    def cleanup(self):
        # Sleep to finish any trigger quickly
        sleep(0.5)
        LightSystemManager.cleanup()

if __name__ == "__main__":
    Main().test()
