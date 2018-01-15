#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__="Alan"

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(BASE_DIR)
#from modulefinder import login
from modules import login
# login.user_login()
# login.creditcard_login()
# login.admin_login()