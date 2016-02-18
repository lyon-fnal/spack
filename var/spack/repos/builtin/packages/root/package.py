# Root
#
from spack import *

class Root(Package):
    """ROOT"""
    homepage = "http://root.cern.ch"
    url      = "https://root.cern.ch/download/root_v5.34.25.source.tar.gz"

    version('5.34.25', '4f9de4cb686c393fc7dc0850bb20de8e',
            url='https://root.cern.ch/download/root_v5.34.25.source.tar.gz')

    # FIXME: Add dependencies if this package requires them.
    # depends_on("foo")
    depends_on("fftw")
    depends_on("libxml2")
    depends_on("python @2.7.9")
    depends_on("gsl @1.16", when='@5.34.25')
    depends_on("gsl", when='@5.35:')
    depends_on_inherits('xrootd', inherits=['cxx14', 'debug'])
    depends_on("libpng")
    depends_on("jpeg")
    depends_on("libtiff")
    depends_on("cmake @2.8.10:")

    variant('cxx14', default=False, description='Build with C++14 support')
    variant('debug', default=False, description='Builds the library in debug mode')

    def setup_dependent_environment(self, module, spec, dep_spec):
        """Root wants to set ROOTSYS"""
        os.environ['ROOTSYS'] = self.prefix

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

        # You'll get build errors with shadowpw turned on. We don't need
        # authentication capabilities, so we can turn it off
        options.append('-Dshadowpw:BOOL=OFF')

        with working_dir(build_directory, create=True):
            cmake(source_directory, *options)
            make()
            make("install")
