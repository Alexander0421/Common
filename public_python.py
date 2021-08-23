# -*- coding:utf-8 -*-
# Python public functions

import os
import contextlib
import subprocess


# Python executes shell commands and obtains execution status and output
def get_status_output(cmd):
    print("[info:] Execute shell command: {}".format(cmd))
    compile_pop = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    status = compile_pop.wait()
    data = compile_pop.stdout.read()
    return status, data


# Python executes the shell pushd command
# use with
@contextlib.contextmanager
def pushd(new_dir):
    print("[info:] work path : {}".format(new_dir))
    pre_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(pre_dir)

