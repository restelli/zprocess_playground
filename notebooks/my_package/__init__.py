from zprocess.process_tree import Process

class TestProcess(Process):
    def run(self):
        """Note: all print statements are commented because when this function is called by:
        
           python -m zprocess.remote -tui

        the std output does not know where to go and this causes warnings"""
        
        #print("Hello! I am the remote process called by ZeroMQ")
        #print("I'm going to do some math")
        item = self.from_parent.get()
        item = item**2
        #print("Sent back the square of input")
        self.to_parent.put(item)