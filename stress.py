import multiprocessing
import subprocess

instance_ip = ""

def stress():
    while True:
        subprocess.Popen(["curl",f"{instance_ip}"])


p1 = multiprocessing.Process(target=stress)
p2 = multiprocessing.Process(target=stress)
p3 = multiprocessing.Process(target=stress)
p4 = multiprocessing.Process(target=stress)

p1.start()
p2.start()
p3.start()
p4.start()
