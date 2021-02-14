from todoGrabber import *
import os

# listFiles test suite
lf = {
    'test/fail.txt',
    'test/test.txt',
    'test/testChild/fail.js',
    'test/testChild/test.js',
    'test/testChild/testGrandChild/fail.py',
    'test/testChild/testGrandChild/test.py'
}
lf_windows = {
    'test\\fail.txt',
    'test\\test.txt',
    'test\\testChild\\fail.js',
    'test\\testChild\\test.js',
    'test\\testChild\\testGrandChild\\fail.py',
    'test\\testChild\\testGrandChild\\test.py'
}


# checkTODO test suite
check = {
    'test/fail.txt': False,
    'test/test.txt': True,
    'test/testChild/fail.js': False,
    'test/testChild/test.js': True,
    'test/testChild/testGrandChild/fail.py': False ,
    'test/testChild/testGrandChild/test.py': True
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

if __name__ == '__main__':
    
    if os.name != 'nt':
        assert(set(listFiles('./test/')) == lf),'listFiles test failed'
    else:
        assert(set(listFiles('./test/')) == lf_windows),'listFiles test failed'
    
    for f in check:
        assert(checkTODO(f) == check[f]), 'checkTODO  test failed for %s' % f
    
    if os.name != 'nt':
        assert(set(grabTODOs('./test/')) == gtd),'grabTODOs test failed'
    else:
        assert(set(grabTODOs('./test/')) == gtd_windows),'grabTODOs test failed'
    