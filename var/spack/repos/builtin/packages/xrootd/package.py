#  Spack package file for xrootd
#
from spack import *
import os

# We have a patch because the ordering of setting libraries is incorrect


class Xrootd(Package):
    """FIXME: XRootD provides high performance, scalable, fault tolerant access to data repositories."""
    homepage = "http://xrootd.org"
    url      = "http://xrootd.org/download/v4.2.3/xrootd-4.2.3.tar.gz"

    version('4.2.3', '7b04ae82684e165bf57d05cfe7e7e33d')

    depends_on('cmake @2.8.12:')
    depends_on('python @2.7.9')

    patch('xrootd-4.2.3.patch', when='@4.2.3')

    variant('cxx14', default=False, description='Build with C++14 support')
    variant('debug', default=False, description='Builds the library in debug mode')

    def setup_dependent_environment(self, module, spec, dep_spec):
        """Set XRDSYS"""
        os.environ['XRDSYS'] = self.prefix

    def install(self, spec, prefix):

        options = []
        options.extend(std_cmake_args)

        build_directory = join_path(self.stage.path, 'spack-build')
        source_directory = self.stage.source_path

        if '+cxx14' in spec:
            env['CXXFLAGS'] = self.compiler.cxx14_flag
            options.append('-DCMAKE_CXX_FLAGS=' + self.compiler.cxx14_flag)

        if '+debug' in spec:
            options.append('-DCMAKE_BUILD_TYPE:STRING=Debug')

        options.append('-DENABLE_LIBEVENT=FALSE')

        with working_dir(build_directory, create=True):
            cmake(source_directory, *options)
            make()
            make("install")
