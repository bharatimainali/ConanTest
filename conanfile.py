from conan import ConanFile

class MyTestProjectConan(ConanFile):
  name = "mytestproject"
  version = "0.0.0"
  description = "My test project example"
  license = "None"
  url = "None"
  settings = "os", "arch", "compiler", "build_type"
  generators = [
    "CMakeDeps"
  ]

  requires = [
    "spdlog/1.13.0"
  ]