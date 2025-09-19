from __PKG_NAME__.cli import main

def test_main(capsys):
    main()
    out, _ = capsys.readouterr()
    assert "OK:" in out
