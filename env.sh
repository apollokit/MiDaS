#!/bin/bash
set -e

SCRIPT_DIR=$(dirname $(realpath $0))

source $SCRIPT_DIR/source_virtualenv

VINCI_LIB_DIR=$(realpath $SCRIPT_DIR/../vinci/lib)
PROJ_DIR=$(realpath $SCRIPT_DIR/..)

PYTHONPATH=$PYTHONPATH:$PROJ_DIR:$VINCI_LIB_DIR "$@"