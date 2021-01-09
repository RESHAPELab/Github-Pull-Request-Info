import importlib

def pipeline_data(inp, pipeline):
    out = inp
    for pipe in pipeline:
        pipe_mod = importlib.import_module('pipes.'+ pipe)
        out = pipe_mod.run(inp)
    return out