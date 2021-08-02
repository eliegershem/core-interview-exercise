# imports
from fastapi import FastAPI
import requests
import entities
import os
app = FastAPI()

# Status endpoint
@app.get("/v1/api/consulCluster/status")
def consul_status():
    try:
        requests.get('http://172.16.16.20:8500')
        status = "1"
        message = "Agent is running"
    except requests.ConnectionError:
        status = "0"
        message = "Agent is not running"

    return entities.Status(status, message)
     
# Summary endpoint
@app.get("/v1/api/consulCluster/summary")
def consul_summary():

    # Get number of Nodes
    r = requests.get('http://172.16.16.20:8500/v1/catalog/nodes')
    if r.content == b'No known Consul servers':
        nodes = 0
    else:
        nodes = len(r.json()[0])
    
    # Get number of Services
    r = requests.get('http://172.16.16.20:8500/v1/catalog/services')
    if r.content == b'No known Consul servers':
        services = 0
    else:
        services = len(r.json())

    # Get Leader IP
    r = requests.get('http://172.16.16.20:8500/v1/status/leader')
    if r.content == b'No known Consul servers':
        leader = "No known Consul leader"
    else:
        leader = r.content

    # Get Cluster Protocol
    r = requests.get('http://172.16.16.20:8500/v1/agent/self')
    cluster_protocol = r.json()['Member']['ProtocolCur']

    return entities.Summary(nodes, services, leader, cluster_protocol)


@app.get("/v1/api/consulCluster/systemInfo")
def consul_systemInfo():
    vCpus = os.cpu_count()
    MemoryGB = float(os.popen("cat /proc/meminfo | awk '/MemTotal/{print $2}'").read()) / 1024
    return entities.SystemInfo(vCpus, MemoryGB)
