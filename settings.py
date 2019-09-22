import os
import platform

HARMONY_BUCKET = "pub.harmony.one"
POLLING_FREQUENCY = 60
BASE_DIR = os.path.abspath(__file__).replace('settings.pyc', '').replace('settings.py', '')
RELEASE = 'release/linux-x86_64/master/'

WALLET_FILES = "wallet libbls384_256.so libcrypto.so.10 libgmp.so.10 libgmpxx.so.4 libmcl.so".split(' ')

if "linux" in platform.system().lower():
    NODE_FILES = "".split('harmony libbls384_256.so libcrypto.so.10 libgmp.so.10 libgmpxx.so.4 libmcl.so md5sum.txt')
else:
    NODE_FILES = "".split('harmony libbls384_256.dylib libcrypto.1.0.0.dylib libgmp.10.dylib libgmpxx.4.dylib libmcl.dylib md5sum.txt')

try:
    from local_settings import *
except ImportError:
    pass