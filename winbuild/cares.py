from .utils import *
from .builder import *

class CaresBuilder(StandardBuilder):
    def build(self):
        if not self.whether_to_build():
            return
        cares_dir = self.standard_fetch_extract(
            'http://c-ares.haxx.se/download/c-ares-%(my_version)s.tar.gz')
        with in_dir(cares_dir):
            with self.execute_batch() as b:
                b.add("nmake -f Makefile.msvc CFG=lib-release ALL")

                # assemble dist
                b.add('mkdir dist dist\\include dist\\lib')
                if self.bconf.cares_version_tuple < (1, 14, 0):
                    subdir = 'ms%s0' % self.bconf.vc_version
                else:
                    subdir = 'msvc'
                b.add('cp %s/cares/lib-release/*.lib dist/lib' % subdir)
                b.add('cp include/*.h dist/include')

