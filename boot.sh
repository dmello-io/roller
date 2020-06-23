#!/bin/bash
screen -d -m -S roller bash -c 'source env/bin/activate && ./roller_web.py'