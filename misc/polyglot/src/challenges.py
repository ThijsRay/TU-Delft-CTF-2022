from unicorn import *
from unicorn.x86_const import *
from unicorn.arm64_const import *

from config import ChallengeConfig, Testcase

def assert_eq(uc, reg, val, msg):
    if uc.reg_read(reg) != val & 0xFFFFFFFFFFFFFFFF:
        raise Exception(msg)

def set_regs(uc, list):
    for reg, val in list:
        uc.reg_write(reg, val)

CHALLENGES = [ChallengeConfig(
    name="Challenge 0: Introduction (beginner)",
    description="Let's get started! For this challenge, you simply need to write an assembly snippet that is valid for both ARM64 and x86_64. If your code runs on both architectures, you get the flag.",
    stack_size=0x1000,
    max_instruction_count=10,
    max_simulation_steps=10,
    disallowed_mnemonics=[],
    flag="TUDCTF{4ss3mbly_15_4lr3ady_h4rd_en0ugh_w1th0ut_4dd1ng_4n0th3r_4rch1t3ctur3}",
    testcases=[
        Testcase(
            set_initial_state_x86=lambda uc: 1,
            set_initial_state_arm64=lambda uc: 1,
            assert_final_state_x86=lambda uc: 1,
            assert_final_state_arm64=lambda uc: 1,
        )
    ]
    # nop nop nop nop    
), ChallengeConfig(
    name="Challenge 1: Multiplication (easy)",
    description="Nice! Now that you know how the UI works, let's get some actual work done. For this challenge, you simply need to multiply the 64-bit integers in RAX and RBX (x84_64), and X0 and X1 (ARM64). The resulting value must be stored in RAX (x86_64) or X0 (ARM64). The stack and any other registers may be modified as needed.",
    stack_size=0x1000,
    max_instruction_count=10,
    max_simulation_steps=10,
    disallowed_mnemonics=[],
    flag="TUDCTF{l0ts_0f_tr1cks_t0_m4k3_th1s_n0t_4s_h4rd_4s_1t_l00k3d}",
    testcases=[
        # simple
        Testcase(
            set_initial_state_x86=lambda uc: set_regs(uc, [(UC_X86_REG_RAX, 10), (UC_X86_REG_RBX, 5)]),
            set_initial_state_arm64=lambda uc: set_regs(uc, [(UC_ARM64_REG_X0, 10), (UC_ARM64_REG_X1, 5)]),
            assert_final_state_x86=lambda uc: assert_eq(uc, UC_X86_REG_RAX, 50, "Failed x86: RAX does not have the expected value"),
            assert_final_state_arm64=lambda uc: assert_eq(uc, UC_ARM64_REG_X0, 50, "Failed ARM64: RAX does not have the expected value"),
        ),
        # overflow
        Testcase(
            set_initial_state_x86=lambda uc: set_regs(uc, [(UC_X86_REG_RAX, 0x1234567890abcdef), (UC_X86_REG_RBX, 0xdeadbeefdeadbeef)]),
            set_initial_state_arm64=lambda uc: set_regs(uc, [(UC_ARM64_REG_X0, 0x1234567890abcdef), (UC_ARM64_REG_X1, 0xdeadbeefdeadbeef)]),
            assert_final_state_x86=lambda uc: assert_eq(uc, UC_X86_REG_RAX, 0x1234567890abcdef * 0xdeadbeefdeadbeef, "Failed x86: RAX does not have the expected value"),
            assert_final_state_arm64=lambda uc: assert_eq(uc, UC_ARM64_REG_X0, 0x1234567890abcdef * 0xdeadbeefdeadbeef, "Failed ARM64: RAX does not have the expected value"),
        ),
        # negative numbers
        Testcase(
            set_initial_state_x86=lambda uc: set_regs(uc, [(UC_X86_REG_RAX, -10), (UC_X86_REG_RBX, 50)]),
            set_initial_state_arm64=lambda uc: set_regs(uc, [(UC_ARM64_REG_X0, -10), (UC_ARM64_REG_X1, 50)]),
            assert_final_state_x86=lambda uc: assert_eq(uc, UC_X86_REG_RAX, -500, "Failed x86: RAX does not have the expected value"),
            assert_final_state_arm64=lambda uc: assert_eq(uc, UC_ARM64_REG_X0, -500, "Failed ARM64: RAX does not have the expected value"),
        )
    ]
    # mul rbx
    # nop
    # jmp a
    # nop
    # nop
    # .byte 0x00, 0x7c, 0x01, 0x9b  
    # a:     
), ChallengeConfig(
    name="Challenge 2: Fibonacci (medium)",
    description="Nice! You've hopefully figured out some tricks to make this a lot easier than it initially seemed. For this challenge, you must compute the n-th fibonacci number in x86_64. The input is given in RAX, and we expect the output to be in RAX too. Your ARM64 code may do anything, as long as it does not crash. The stack and any other registers may be modified as needed.",
    stack_size=0x1000,
    max_instruction_count=100,
    max_simulation_steps=10000,
    disallowed_mnemonics=[],
    flag="TUDCTF{f1b_in_4sm_1s_bl4z1ngly_f4st}",
    testcases=[
        Testcase(
            set_initial_state_x86=lambda uc: set_regs(uc, [(UC_X86_REG_RAX, 1)]),
            set_initial_state_arm64=lambda uc: 1,
            assert_final_state_x86=lambda uc: assert_eq(uc, UC_X86_REG_RAX, 0, "Failed x86: RAX != fib(1) != 0"),
            assert_final_state_arm64=lambda uc: 1,
        ),
        Testcase(
            set_initial_state_x86=lambda uc: set_regs(uc, [(UC_X86_REG_RAX, 2)]),
            set_initial_state_arm64=lambda uc: 1,
            assert_final_state_x86=lambda uc: assert_eq(uc, UC_X86_REG_RAX, 1, "Failed x86: RAX != fib(2) != 1"),
            assert_final_state_arm64=lambda uc: 1,
        ),
        Testcase(
            set_initial_state_x86=lambda uc: set_regs(uc, [(UC_X86_REG_RAX, 3)]),
            set_initial_state_arm64=lambda uc: 1,
            assert_final_state_x86=lambda uc: assert_eq(uc, UC_X86_REG_RAX, 1, "Failed x86: RAX != fib(3) != 1"),
            assert_final_state_arm64=lambda uc: 1,
        ),
        Testcase(
            set_initial_state_x86=lambda uc: set_regs(uc, [(UC_X86_REG_RAX, 4)]),
            set_initial_state_arm64=lambda uc: 1,
            assert_final_state_x86=lambda uc: assert_eq(uc, UC_X86_REG_RAX, 1, "Failed x86: RAX != fib(4) != 2"),
            assert_final_state_arm64=lambda uc: 1,
        ),
        Testcase(
            set_initial_state_x86=lambda uc: set_regs(uc, [(UC_X86_REG_RAX, 8)]),
            set_initial_state_arm64=lambda uc: 1,
            assert_final_state_x86=lambda uc: assert_eq(uc, UC_X86_REG_RAX, 13, "Failed x86: RAX != fib(8) != 13"),
            assert_final_state_arm64=lambda uc: 1,
        ),
    ]
), ChallengeConfig(
    name="Challenge 3: Constrained Multiplication (hard)",
    description="Back to the basics! For this challenge, you must do the same as for challenge 1: RAX = RAX * RBX (x86_64), and X0 = X0 * X1 (ARM64). However, we've blacklisted some instructions to make it a bit harder. You can see the full list of disallowed instructions above. Good luck!",
    stack_size=0x1000,
    max_instruction_count=10,
    max_simulation_steps=10,
    disallowed_mnemonics=[
        "nop",
        "adrp",
        "jmp"
    ],
    flag="TUDCTF{s0_m4ny_tr1cks_m4k3_4_bl4ckl1st_4lm0st_us3l355}",
    testcases=[
        # simple
        Testcase(
            set_initial_state_x86=lambda uc: set_regs(uc, [(UC_X86_REG_RAX, 10), (UC_X86_REG_RBX, 5)]),
            set_initial_state_arm64=lambda uc: set_regs(uc, [(UC_ARM64_REG_X0, 10), (UC_ARM64_REG_X1, 5)]),
            assert_final_state_x86=lambda uc: assert_eq(uc, UC_X86_REG_RAX, 50, "Failed x86: RAX does not have the expected value"),
            assert_final_state_arm64=lambda uc: assert_eq(uc, UC_ARM64_REG_X0, 50, "Failed ARM64: RAX does not have the expected value"),
        ),
        # overflow
        Testcase(
            set_initial_state_x86=lambda uc: set_regs(uc, [(UC_X86_REG_RAX, 0x1234567890abcdef), (UC_X86_REG_RBX, 0xdeadbeefdeadbeef)]),
            set_initial_state_arm64=lambda uc: set_regs(uc, [(UC_ARM64_REG_X0, 0x1234567890abcdef), (UC_ARM64_REG_X1, 0xdeadbeefdeadbeef)]),
            assert_final_state_x86=lambda uc: assert_eq(uc, UC_X86_REG_RAX, 0x1234567890abcdef * 0xdeadbeefdeadbeef, "Failed x86: RAX does not have the expected value"),
            assert_final_state_arm64=lambda uc: assert_eq(uc, UC_ARM64_REG_X0, 0x1234567890abcdef * 0xdeadbeefdeadbeef, "Failed ARM64: RAX does not have the expected value"),
        ),
        # negative numbers
        Testcase(
            set_initial_state_x86=lambda uc: set_regs(uc, [(UC_X86_REG_RAX, -10), (UC_X86_REG_RBX, 50)]),
            set_initial_state_arm64=lambda uc: set_regs(uc, [(UC_ARM64_REG_X0, -10), (UC_ARM64_REG_X1, 50)]),
            assert_final_state_x86=lambda uc: assert_eq(uc, UC_X86_REG_RAX, -500, "Failed x86: RAX does not have the expected value"),
            assert_final_state_arm64=lambda uc: assert_eq(uc, UC_ARM64_REG_X0, -500, "Failed ARM64: RAX does not have the expected value"),
        )
    ]     
)]