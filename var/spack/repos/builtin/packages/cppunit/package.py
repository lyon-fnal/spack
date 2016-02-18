# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install cppunit
#
# You can always get back here to change things with:
#
#     spack edit cppunit
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Cppunit(Package):
    """FIXME: put a proper description of your package here."""
    # FIXME: add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://sourceforge.net/projects/cppunit/files/cppunit/1.12.1/cppunit-1.12.1.tar.gz"

    version('1.12.1', 'bd30e9cf5523cdfc019b94f5e1d7fd19')

    # FIXME: Add dependencies if this package requires them.
    # depends_on("foo")

    variant('cxx14', default=False, description="Build with c++14 support")

    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.

        if '+cxx14' in spec:
            env['CXXFLAGS'] = self.compiler.cxx14_flag

        configure('--prefix=%s' % prefix)

        # FIXME: Add logic to build and install here
        make()
        make("install")
