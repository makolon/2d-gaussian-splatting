import runpy

if __name__ != "__main__":
    from twodgs.scripts.eval_tnt.plot import *  # noqa: F401,F403
else:
    runpy.run_module("twodgs.scripts.eval_tnt.plot", run_name="__main__")
