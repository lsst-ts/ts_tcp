"""Sphinx configuration file for an LSST stack package.

This configuration only affects single-package Sphinx documentation builds.
"""

from documenteer.conf.pipelinespkg import *  # noqa
import lsst.ts.tcpip  # noqa

project = "ts_tcpip"
html_theme_options["logotext"] = project  # type: ignore # noqa
html_title = project
html_short_title = project
# Avoid warning: Could not find tag file _doxygen/doxygen.tag
doxylink = {}  # type: ignore
