from capstone import *
from keystone import *

CODE_ADDRESS = 0x1000
STACK_ADDRESS = 0x4000_0000

def capstone_x64():
    return Cs(CS_ARCH_X86, CS_MODE_64)

def capstone_arm64():
    return Cs(CS_ARCH_ARM64, CS_MODE_ARM + CS_MODE_LITTLE_ENDIAN)

def keystone_x64():
    return Ks(KS_ARCH_X86, KS_MODE_64)

def keystone_arm64():
    return Ks(KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN)