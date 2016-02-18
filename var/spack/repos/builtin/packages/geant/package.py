# Geant
#
from spack import *

class Geant(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://geant4.cern.ch"
    url      = "http://geant4.web.cern.ch/geant4/support/source/geant4.9.6.p04.tar.gz"

    version('4.9.6.p04', '105271674d63fbc67b7eb36fa527533c')

    depends_on_inherit("clhep @2.2.0.5", inherit=['cxx14', 'debug'], when='@4.9.6.p04')
    depends_on_inherit("clhep @2.3.0.0", inherit=['cxx14', 'debug'], when='@4.10.2')
    depends_on("xerces-c")
    depends_on("cmake @2.8.10:")

    variant('cxx14', default=False, description='Build with C++14 support')
    variant('debug', default=False, description='Builds the library in debug mode')

    def install(self, spec, prefix):

        options = []
        options.extend(std_cmake_args)

        build_directory = join_path(self.stage.path, 'spack-build')
        source_directory = self.stage.source_path

        if '+cxx14' in spec:
            env['CXXFLAGS'] = self.compiler.cxx14_flag
            options.append('-DCMAKE_CXX_FLAGS=' + self.compiler.cxx14_flag)
            options.append('-DGEANT4_BUILD_CXXSTD=c++11') #4.9.6 can't handle c++14

        if '+debug' in spec:
            options.append('-DCMAKE_BUILD_TYPE:STRING=Debug')

        options.extend(['-DGEANT4_USE_SYSTEM_CLHEP=ON', '-DGEANT4_USE_OPENGL_X11=ON',
                        '-DGEANT4_USE_GDML=ON', '-DGEANT4_INSTALL_DATA=ON'])

        with working_dir(build_directory, create=True):
            cmake(source_directory, *options)
            make()
            make("install")
