#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "AdvancedSoftwareProject"
version = "1.0"

summary = "AirBnb Extension"
url     = "https://github.com/flruee/AdvancedSoftwareProject/tree/main"

description = """AirBnb extension: adds extra filter options customised to the user"""

authors      = [Author("Ben Murphy",            "16-714-925"),
                Author("Songyi Han",            "18-796-847"),
                Author("Florian Rüegsegger",    "14-714-737")
                ]
license      = "None"
default_task = "publish"

@init
def initialize(project):
    project.build_depends_on("mockito")

@init
def set_properties(project):
    pass
