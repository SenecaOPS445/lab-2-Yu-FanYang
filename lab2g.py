#!/usr/bin/env python3

#Author: Yu-Fan Yang
#Author ID: 154742225
#Date Created: 2025/01/18

import sys

if len(sys.argv) == 1:
    Timer = 3
else:
    Timer = int(sys.argv[1])

while Timer > 0:
    print(Timer)
    Timer = Timer - 1

print('blast off!')