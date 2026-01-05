import runpy

if __name__ != "__main__":
    from twodgs.scripts.eval_tnt.evaluate_single_scene import *  # noqa: F401,F403
else:
    runpy.run_module("twodgs.scripts.eval_tnt.evaluate_single_scene", run_name="__main__")
