from capstone import *
from unicorn import *
from unicorn.x86_const import *
from unicorn.arm64_const import *
from config import ChallengeConfig, Testcase
from const import *

def validate_assembly(code: bytes, config: ChallengeConfig, cs: Cs):
    insns = list(cs.disasm(code, CODE_ADDRESS))
    if len(insns) > config.max_instruction_count:
        raise Exception("Too many instructions: %d > %d" % (len(insns), config.max_instruction_count))

    total_length = 0

    for insn in insns:
        if insn.mnemonic in config.disallowed_mnemonics:
            raise Exception("Use of disallowed instruction: %s" % insn.mnemonic)

        total_length += insn.size

    if total_length != len(code):
        raise Exception("Failed to disassemble all input bytes: successfully dissembled %d bytes, out of %d total" % (total_length, len(code)))

def run_testcase(code: bytes, config: ChallengeConfig, testcase: Testcase):
    x86_unicorn = Uc(UC_ARCH_X86, UC_MODE_64)
    arm64_unicorn = Uc(UC_ARCH_ARM64, UC_MODE_ARM + UC_MODE_LITTLE_ENDIAN)

    def setup_memory(unicorn: Uc):
        align_size = (config.stack_size + 0x1000) & ~0xfff
        unicorn.mem_map(CODE_ADDRESS, align_size)
        unicorn.mem_map(STACK_ADDRESS, config.stack_size)
        unicorn.mem_write(CODE_ADDRESS, code)

    # setup memory regions
    setup_memory(x86_unicorn)
    setup_memory(arm64_unicorn)

    # setup stack registers
    x86_unicorn.reg_write(UC_X86_REG_RSP, STACK_ADDRESS + config.stack_size - 8)
    x86_unicorn.reg_write(UC_X86_REG_RBP, STACK_ADDRESS + config.stack_size - 8)
    arm64_unicorn.reg_write(UC_ARM64_REG_SP, STACK_ADDRESS + config.stack_size - 8)

    # setup initial state
    testcase.set_initial_state_x86(x86_unicorn)
    testcase.set_initial_state_arm64(arm64_unicorn)

    # run emulation
    try:
        x86_unicorn.emu_start(CODE_ADDRESS, CODE_ADDRESS + len(code), count=config.max_simulation_steps)
    except Exception as e:
        raise Exception("Failed to emulate x86: %s" % e)

    try:
        arm64_unicorn.emu_start(CODE_ADDRESS, CODE_ADDRESS + len(code), count=config.max_simulation_steps)
    except Exception as e:
        raise Exception("Failed to emulate ARM64: %s" % e)

    # check final state
    testcase.assert_final_state_x86(x86_unicorn)
    testcase.assert_final_state_arm64(arm64_unicorn)

def run_challenge(input: bytes, config: ChallengeConfig):
    try:
        validate_assembly(input, config, capstone_x64())
    except Exception as ex:
        raise Exception("Failed to validate x64 assembly: %s" % ex)
    try:
        validate_assembly(input, config, capstone_arm64())
    except Exception as ex:
        raise Exception("Failed to validate ARM64 assembly: %s" % ex)

    for testcase in config.testcases:
        try:
            run_testcase(input, config, testcase)
        except Exception as e:
            raise Exception("One or more testcases failed for your code: %s" % e)
