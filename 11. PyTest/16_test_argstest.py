
def test_argstest01(CmdOpt):
    # print("read config file " + CmdOpt.readline())
    assert CmdOpt.readline().index('lab12')