#!/usr/bin/python

"""
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
   http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import distutils.core
import os

long_description = "Placeholder in case of missing README.md."

if os.path.exists("README.md"):
    with open("README.md") as readme:
        long_description = readme.read()

distutils.core.setup(
    name="goPyServer",
    version="1.0.0",
    packages=["goPyServer"],
    author="Nikhil Chawla",
    author_email="chawlanikhil24@gmail.com",
    url="https://github.com/chawlanikhil24/goPyServer",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    description="This project is an implementation of the JSON-RPC Server " +
        "which can easily cross communicate with Golang Client using goPy client Library",
    long_description=long_description)
