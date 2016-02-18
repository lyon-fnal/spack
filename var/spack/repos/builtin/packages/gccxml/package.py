from spack import *

class Gccxml(Package):
    homepage = "https://github.com/gccxml/gccxml"
    url      = "https://github.com/gccxml/gccxml"

    version('2013-07-31', git='https://github.com/gccxml/gccxml.git', commit='3afa')

    depends_on('cmake @2.8.12.2:')

    def install(self, spec, prefix):
        cmake(*std_cmake_args)
        make()
        make("install")
