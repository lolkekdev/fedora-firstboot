import subprocess


def console():
    subprocess.call(["sh", "chmod +x console.sh"])
    subprocess.call(["sh", "./console.sh"])


def codecs():
    subprocess.call(["sh", "chmod +x codecs.sh"])
    subprocess.call(["sh", "./codecs.sh"])


def greendrivers():
    subprocess.call(["sh", "chmod +x nvidia.sh"])
    subprocess.call(["sh", "./nvidia.sh"])
