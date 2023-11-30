# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class GccRuntime(Package):
    homepage = "https://example.com"
    has_code = False
    tags = ["runtime"]
    requires("%gcc")
