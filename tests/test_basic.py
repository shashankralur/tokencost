# test_main.py
from tokencost.cli import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Token Cost Is Active Now...\n"