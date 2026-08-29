# test_main.py
from tokencost.cli import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    
    assert "Token Cost Is Active Now...\n" in captured.out
    assert "token ->" in captured.out