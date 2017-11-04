from conans import ConanFile


class BitseryConan(ConanFile):
    name = "cereal"
    version = "1.2.2"
    license = "BSD"
    description = "cereal is a header-only C++11 serialization library."
    url = "https://github.com/USCiLab/cereal"
    settings = "os", "compiler", "build_type", "arch"
    options = {}
    default_options = ""
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/USCiLab/cereal.git --branch v{version} --depth 1".format(version=self.version))

    def build(self):
        pass

    def package(self):
        self.copy("*.hpp", dst="include", src="cereal/include")

    def package_info(self):
        pass
