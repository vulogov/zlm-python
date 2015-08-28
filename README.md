zlm-python
==============

The `zlm-python` loadable module is a way to extend `zabbix_agentd` daemon
with Python. The main goal is to avoid costly and slow exec calls and
loading of the interpreter.

## Installation.

There are bugs. There are undetected issues.

* Run `BUILD.sh`.

* Copy `python.so` to the directory defined by `LoadModulePath` in
`zabbix_agentd.conf`

* Create subdirectory `pymodules` in the directory where your
configuration file is installed

* Install the Python Zabbix modules in this directory.

* Add `LoadModule=python.so` in your `zabbix_agentd.conf`.


* Set the `PYTHONPATH` as:

```
export PYTHONPATH=`python -c "import sys; print ':'.join(sys.path)"`
```

This is not mandatory anymore, if PYTHONPATH is not defined, module
will discover it from Python interpreter.

* Restart `zabbix_agentd`


## Zabbix Python module

This is a regular python module, where you shall define function
main(*args). All arguments passed from Zabbix to an agent, will be
passed to a main() functions as srings. The return value will be returned
to Zabbix. Only Int, Long, Float and String information types are supported as return values.

## "Special" Zabbix modules

These modules perform some special actions.

* `ZBX_startup.py` - module, which main() function will be executed during
`zabbix_agentd` startup

* `ZBX_finish.py` - module, which main() function will be executed during
`zabbix_agentd` finish

## Python interface

The following item keys are supported:

* `python.ping` - no parameters. Return 1 if embedded Python is initialized
* `python.version` - returns version of the embedded Python interpreter
* `py[]` -  routing  module interface through ZBX_call.py. 
In addition to a calling `main()` function of the module, can call any
function and also read data from pre-spawned agents and a Redis queues.

