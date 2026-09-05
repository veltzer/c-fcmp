#!/usr/bin/env python

""" Build libfcmp.so and its pkg-config file, replacing the autotools build.

The old Makefile.am built a libtool library from fcmp.c with -Wall -Werror
and versioned it 1.2.2 (configure.ac); fcmp.pc.in was filled in by configure.
This reproduces both: the shared object gets the soname the libtool version
info implied (current 2, age 0 -> libfcmp.so.2) and the .pc file assumes the
/usr/local prefix that configure defaulted to. """

import os
import subprocess
import sys

VERSION = "1.2.2"
SONAME = "libfcmp.so.2"
PREFIX = "/usr/local"
OUT = "out"


def main():
    """ main entry point """
    os.makedirs(OUT, exist_ok=True)
    lib = os.path.join(OUT, "libfcmp.so")
    ret = subprocess.call([
        "gcc", "-Wall", "-Werror", "-fPIC", "-shared",
        f"-Wl,-soname,{SONAME}",
        "-o", lib, "fcmp.c", "-lm",
    ])
    if ret != 0:
        sys.exit(ret)
    with open(os.path.join(OUT, "fcmp.pc"), "w", encoding="utf-8") as handle:
        handle.write(
            f"prefix={PREFIX}\n"
            "exec_prefix=${prefix}\n"
            "libdir=${exec_prefix}/lib\n"
            "includedir=${prefix}/include\n"
            "\n"
            "Name: fcmp\n"
            "Description: Comparison of floats\n"
            f"Version: {VERSION}\n"
            "Libs: -L${libdir} -lfcmp\n"
            "Cflags: -I${includedir}\n"
        )


if __name__ == "__main__":
    main()
