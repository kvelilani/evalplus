import hashlib
import json
import os
from typing import Dict
from evalplus.data.utils import (
    stream_jsonl,
    make_cache
)

def get_custom_dataset(path: str) -> Dict[str, Dict]:
    """
    Args:
        path
    Returns:
        List[Dict[str, str]]: List of dicts with keys "task_id", "prompt", "contract", "canonical_solution", "base_input"
    Notes:
        "task_id" is the identifier string for the task
        "prompt" is the function signature with docstring
        "contract" is the assertions for the function's input (validity)
        "canonical_solution" is the ground-truth implementation for diff-testing
        "base_input" is the test inputs from original HumanEval
        "plus_input" is the test inputs brought by EvalPlus
        "atol" is the absolute tolerance for diff-testing
    """
    make_cache(path)

    custom = {task["task_id"]: task for task in stream_jsonl(path)}
    return custom

def get_custom_dataset_hash(path) -> str:
    """Get the hash of HumanEvalPlus.
    Returns:
        str: The hash of HumanEvalPlus
    """
    
    with open(path, "rb") as f:
        plus = f.read()
    return hashlib.md5(plus).hexdigest()
