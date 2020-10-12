import os


def cmd_exist(cmd):
    def check(func):
        def wrapper(*args, **kwargs):
            cmd_pass = False
            for path in os.environ["PATH"].split(":"):
                if os.path.isdir(path) and cmd in os.listdir(path):
                    cmd_pass = True
                    break

            if not cmd_pass:
                raise SystemError("Can not find %s process." % cmd)

            return func(*args, **kwargs)
        return wrapper
    return check
