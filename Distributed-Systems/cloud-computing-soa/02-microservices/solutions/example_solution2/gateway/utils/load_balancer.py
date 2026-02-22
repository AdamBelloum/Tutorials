from itertools import cycle


# Bonus: Load Balancer for scaling out
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.pool = cycle(servers)

    def round_robin(self):
        return next(self.pool)
