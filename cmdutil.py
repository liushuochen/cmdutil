import platform
import os
import utils


@utils.cmd_exist("uname")
def kernal():
    info = {
        "name": os.popen("uname -s").read().strip(),
        "version": os.popen("uname -r").read().strip(),
        "version_detail": os.popen("uname -v").read().strip(),
        "node_name": os.popen("uname -n").read().strip()
    }
    return info


def system_info():
    info = {
        "platform": platform.platform(),
        "kernal": kernal()
    }
    return info
