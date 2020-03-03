import DockerfileParser
import RequirementsParser

# DockerfileParser.parse("sample_dockerfile/files/", 50000)
RequirementsParser.reparseOutputRecursively("out.log")

# RequirementsParser.parse("sample_requirements/files/", 50000)
RequirementsParser.reparseOutputRecursively("reqout.log")