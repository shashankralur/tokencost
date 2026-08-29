import sys
import pytest
from tokencost.cli import main, parse_args

def test_parse_text_argument(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["tokencost", "Hello World"]
    )
    
    args = parse_args()
    
    assert args.text == "Hello World"
    assert args.file is None
    
    
def test_parse_file_argument(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["tokencost", "--file", "some_test_file.txt"],
    )
    
    args = parse_args()
    
    assert args.text is None
    assert args.file == "some_test_file.txt"

def test_cli_output(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        ["tokencost", "Hello World"]
    )
    
    main()
    
    captured = capsys.readouterr()
    assert "openai" in captured.out
    assert "gpt-4o-mini" in captured.out
    assert "Tokens" in captured.out
    assert "Cost" in captured.out
    

def test_no_input(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        ["tokencost"]
    )
    
    with pytest.raises(SystemExit) as exc_info:
        main()
    
    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    
    assert "provide text or use --file" in captured.err
    

def test_missing_file(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        ["tokencost", "--file", "does_noy_exist.txt"],
    )
    
    with pytest.raises(SystemExit) as exc_info:
        main()
        
    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "file not found" in captured.err
    
    
 