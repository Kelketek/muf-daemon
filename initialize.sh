#!/bin/bash
#This does some fiddling to compile the C code for the MUF prims that require it.
source="${BASH_SOURCE[0]}"
while [ -h "$source" ] ; do source="$(readlink "$source")"; done
dir="$( cd -P "$( dirname "$source" )" && pwd )"
gcc -c -fPIC "$dir"/muf_prims/smatch.c -o "$dir"/muf_prims/smatch.o
gcc -shared -Wl,-soname,smatch.so -o "$dir"/muf_prims/smatch.so  "$dir"/muf_prims/smatch.o
