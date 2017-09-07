#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier


train = pd.read_csv('./dataset/train.csv')
test = pd.read_csv('./dataset/test.csv')

