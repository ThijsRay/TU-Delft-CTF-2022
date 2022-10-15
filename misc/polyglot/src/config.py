from typing import List, Callable, Any
from unicorn import Uc
from pydantic import BaseModel

class Testcase(BaseModel):
    set_initial_state_x86: Callable[[Uc], Any]
    set_initial_state_arm64: Callable[[Uc], Any]

    assert_final_state_x86: Callable[[Uc], Any]
    assert_final_state_arm64: Callable[[Uc], Any]

class ChallengeConfig(BaseModel):
    name: str
    description: str

    stack_size: int

    max_instruction_count: int
    max_simulation_steps: int
    disallowed_mnemonics: List[str]

    flag: str
    testcases: List[Testcase]
