import pytest
from aider.args import get_parser

def test_system_prompt_argument():
    parser = get_parser([], None)
    args = parser.parse_args(["--system-prompt", "Additional system prompt"])
    assert args.system_prompt == "Additional system prompt"

def test_system_prompt_yaml_config(tmp_path):
    config_file = tmp_path / ".aider.conf.yml"
    config_file.write_text("system_prompt: Yaml system prompt")
    parser = get_parser([str(config_file)], None)
    args = parser.parse_args([])
    assert args.system_prompt == "Yaml system prompt"
