# -*- coding:utf-8 -*-
# Python public functions

import os
import contextlib
import subprocess


# Python executes shell commands and obtains execution status and output
def get_status_output(cmd):
    print("[info:] Execute shell command: {}".format(cmd))
    compile_pop = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    status = compile_pop.wait()
    prc_data = compile_pop.stderr.read() # 过程输出
    out_data = compile_pop.stdout.read() # 结果输出
    return status, prc_data, out_data


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

