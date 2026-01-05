import runpy

if __name__ != "__main__":
    from twodgs.scripts.train import *  # noqa: F401,F403
else:
    runpy.run_module("twodgs.scripts.train", run_name="__main__")
