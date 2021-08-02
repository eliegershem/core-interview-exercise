class Status():
    def __init__(self, s, message):
        self.status = s
        self.message = message


class Summary():
    def __init__(self, nodes, services, leader, cluster_protocol):
        self.registered_nodes = nodes
        self.registered_services = services
        self.leader = leader
        self.cluster_protocol = cluster_protocol

class SystemInfo():
    def __init__(self, vCpus, MemoryGB):
        self.vCpus = vCpus
        self.MemoryGB = MemoryGB