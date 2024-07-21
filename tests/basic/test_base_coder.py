import pytest
from aider.coders.base_coder import Coder

def test_fmt_system_prompt_with_cli_argument():
    coder = Coder(system_prompt="CLI system prompt")
    formatted_prompt = coder.fmt_system_prompt("Base system prompt")
    assert "CLI system prompt" in formatted_prompt

def test_fmt_system_prompt_with_yaml_config():
    coder = Coder(system_prompt="Yaml system prompt")
    formatted_prompt = coder.fmt_system_prompt("Base system prompt")
    assert "Yaml system prompt" in formatted_prompt
