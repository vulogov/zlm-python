import imp
import traceback
import posixpath
try:
    import cPickle as pickle
except:
    import pickle

def main(cmd, *args):
    p_cmd = cmd.split(".")
    name = p_cmd[0]
    try:
        method = p_cmd[1]
    except:
        method = "main"
    try:
        params = tuple(p_cmd[2:])
    except:
        params = ()
    try:
        fp, pathname, description = imp.find_module(name)
        if posixpath.dirname(pathname).split("/")[-1] != "pymodules":
            ## If discovered module isn't in pymodules, we don't want to call it
            raise ImportError, name
    except:
        return (0,"Python module not exists",traceback.format_exc())
    try:
        mod = imp.load_module(name, fp, pathname, description)
    except:
        return (0,"Python module can not be loaded",traceback.format_exc())
    finally:
        fp.close()
    try:
        ret = apply(getattr(mod, method), args+params)
    except:
        return (0,"Python module threw traceback",traceback.format_exc())
    return (1, ret, None)
