from conans import ConanFile
import os
from os import path
from conans.tools import download, unzip, check_sha256


class ArbitraryName(ConanFile):
    name = "catch"
    version = "1.6.0"
    branch = "stable"
    license = "Boost"
    url = "http://github.com/jlgerber/conan-catch"
    settings = None

    ZIP_FOLDER_NAME = "Catch-1.6.0"
    ZIP_URL_NAME = 'v1.6.0.zip'
    FILE_SHA = '391e5e1d62bba85a9dfd6685f96d5673e7cca217c3d0756120e78c8496946764'

    def source(self):
        zip_name = "catch.zip"
        download("https://github.com/philsquared/Catch/archive/%s" % self.ZIP_URL_NAME, zip_name)
        check_sha256(zip_name, self.FILE_SHA)
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy("catch.hpp", "include", path.join(self.ZIP_FOLDER_NAME, 'single_include'))
        self.copy("catch_with_main.hpp", "include", path.join(self.ZIP_FOLDER_NAME, 'include'))

    def package_info(self):
        self.cpp_info.libdirs = []
