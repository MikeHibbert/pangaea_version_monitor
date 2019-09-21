import os

HARMONY_BUCKET = "pub.harmony.one"
POLLING_FREQUENCY = 60

wallet_files = "wallet libbls384_256.so libcrypto.so.10 libgmp.so.10 libgmpxx.so.4 libmcl.so".split(' ')

try:
    from local_settings import *
except ImportError:
    pass