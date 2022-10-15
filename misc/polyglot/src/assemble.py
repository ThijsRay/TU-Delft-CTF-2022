from typing import *
from capstone import *
from keystone import *
from const import *

def format_insn(insn: CsInsn) -> str:
    return f'0x{insn.address:04x} {insn.bytes.hex():14} {insn.mnemonic} {insn.op_str}'

def disassemble(code: bytes, capstone: Cs) -> str:
    try:
        insns = list(capstone.disasm(code, CODE_ADDRESS))
    except Exception as ex:
        return f'Failed to disassemble: {ex}'

    insns_str = "\n".join(map(format_insn, insns))
    total_length_disassembled = sum(map(lambda insn: insn.size, insns))
    if total_length_disassembled < len(code):
        insns_str += "\n... (failed to disassemble %d bytes)" % (len(code) - total_length_disassembled)

    return insns_str.strip()

# assemble the given assembly code using the given keystone instance,
# then disassemble it in both x86 and arm64 mode. Return the disassembled
# code in both architectures, plus a hexdump of the assembled code.
def assemble_and_display(code: bytes, keystone: Union[Ks, None]) -> Tuple[str, str, str]:
    assembled = code
    if keystone is not None:
        try:
            assembled, count = keystone.asm(code, CODE_ADDRESS)
            if assembled is None:
                return "Failed to assemble", "", ""
            assembled = bytes(assembled)
        except Exception as ex:
            return f'Failed to assemble: {ex}', '', ''

    x86_disassembled = disassemble(assembled, capstone_x64())
    arm64_disassembled = disassemble(assembled, capstone_arm64())

    return x86_disassembled, arm64_disassembled, assembled.hex()