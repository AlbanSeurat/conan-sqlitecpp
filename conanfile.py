from conans import ConanFile, CMake

class SQLiteCppConan(ConanFile):

    name = "SQLiteCpp"
    version = "2.2.0"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/AlbanSeurat/conan-sqlitecpp"
    license = "MIT"
    options = {"lint": [True, False]}
    default_options = "lint=False"
    exports = "FindSQLiteCpp.cmake"

    def source(self):
        self.run("git clone https://github.com/SRombauts/SQLiteCpp.git")
        self.run("cd SQLiteCpp && git checkout %s" % (self.version))

    def build(self):
        cmake = CMake(self)
        if self.options.lint:
            cmake.definitions["SQLITECPP_RUN_CPPLINT"] = 1
        cmake.configure(source_folder="SQLiteCpp")
        cmake.build()
        #self.run('cmake %s/SQLiteCpp %s %s' % (self.conanfile_directory, cmake.command_line, lint))
        #self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("FindSQLiteCpp.cmake", ".", ".")
        self.copy("*.h", dst="include", src="SQLiteCpp/include")
        self.copy("*.lib", dst="lib", src=".", keep_path=False)
        self.copy("*.a", dst="lib", src=".", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["SQLiteCpp", "sqlite3"]
        if not self.settings.os == "Windows":
            self.cpp_info.libs.append("pthread")
            self.cpp_info.libs.append("dl")
