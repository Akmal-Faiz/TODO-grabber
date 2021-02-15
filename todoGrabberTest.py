from todoGrabber import *
import os

# listFiles test suite
cwd = os.getcwd()
lf = {
    'test/fail.txt',
    'test/test.txt',
    'test/todoGrabber.py',
    'test/testChild/fail.js',
    'test/testChild/test.js',
    'test/testChild/testGrandChild/fail.py',
    'test/testChild/testGrandChild/test.py',
    'test/testChild/testGrandChild/empty'
}
lf_windows = {
    'test\\fail.txt',
    'test\\test.txt',
    'test\\todoGrabber.py',
    'test\\testChild\\fail.js',
    'test\\testChild\\test.js',
    'test\\testChild\\testGrandChild\\fail.py',
    'test\\testChild\\testGrandChild\\test.py',
    'test\\testChild\\testGrandChild\\empty'
}
lf = {cwd + '/' + i for i in lf}
lf_windows = {cwd + '\\' + i for i in lf_windows}

# checkTODO test suite
check = {
    'test/fail.txt': False,
    'test/test.txt': True,
    'test/todoGrabber.py': True,
    'test/testChild/fail.js': False,
    'test/testChild/test.js': True,
    'test/testChild/testGrandChild/fail.py': False ,
    'test/testChild/testGrandChild/test.py': True,
    'test/testChild/testGrandChild/empty': False
}

# grabTODOs test suite
gtd = {
    'test/test.txt',
    'test/testChild/test.js',
    'test/testChild/testGrandChild/test.py'
}
gtd_windows = {
    'test\\test.txt',
    'test\\testChild\\test.js',
    'test\\testChild\\testGrandChild\\test.py'
}
gtd = {cwd + '/' + i for i in gtd}
gtd_windows = {cwd + '\\' + i for i in gtd_windows}

if __name__ == '__main__':
    if os.name != 'nt':
        assert(set(listFiles(cwd + '/test/')) == lf),'listFiles test failed'
    else:
        assert(set(listFiles(cwd + '\\test\\')) == lf_windows),'listFiles  test failed'
    
    for f in check:
        assert(checkTODO(f) == check[f]), 'checkTODO  test failed for %s' % f
    
    if os.name != 'nt':
        assert(set(grabTODOs(cwd + '/test/')) == gtd),'grabTODOs test failed'
    else:
        assert(set(grabTODOs(cwd + '\\test\\')) == gtd_windows),'grabTODOs test failed'
    