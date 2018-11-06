""" 
  author: Mateusz Zawadzki
  example use: python nvme.py /dev/nvme1n1
"""

import fcntl, sys
from ctypes import *

class Command(Structure):
  _fields_ = [
  ('opcode', c_uint8),
  ('something1', c_uint8 * 23),
  ('addr', c_uint64),
  ('metadata_len', c_uint32),
  ('data_len', c_uint32),
  ('cdw10', c_uint32),
  ('something2', c_uint32 * 7),
   ]


buf = create_string_buffer("", 4096)
cmd = Command(opcode = 0x06, addr = addressof(buf), data_len = sizeof(buf), cdw10 = 1)


with open(sys.argv[1], "rwb") as fd:
  fcntl.ioctl(fd, 0xC0484E41, cmd)
  print buf[3072:][:32].strip()
