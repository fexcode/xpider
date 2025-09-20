class SpiderStopped(Exception):
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return "Spider stopped: %s" % self.reason
    
    def __repr__(self):
        return "SpiderStopped(%r)" % self.reason