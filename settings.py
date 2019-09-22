import os

HARMONY_BUCKET = "pub.harmony.one"
POLLING_FREQUENCY = 60
BASE_DIR = os.path.abspath(__file__).replace('settings.pyc', '').replace('settings.py', '')
RELEASE = 'release/linux-x86_64/master/'

wallet_files = "wallet libbls384_256.so libcrypto.so.10 libgmp.so.10 libgmpxx.so.4 libmcl.so".split(' ')

try:
    from local_settings import *
except ImportError:
    pass