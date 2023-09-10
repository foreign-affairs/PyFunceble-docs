"""
The tool to check the availability or syntax of domain, IP or URL.

::


    ██████╗ ██╗   ██╗███████╗██╗   ██╗███╗   ██╗ ██████╗███████╗██████╗ ██╗     ███████╗
    ██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║████╗  ██║██╔════╝██╔════╝██╔══██╗██║     ██╔════╝
    ██████╔╝ ╚████╔╝ █████╗  ██║   ██║██╔██╗ ██║██║     █████╗  ██████╔╝██║     █████╗
    ██╔═══╝   ╚██╔╝  ██╔══╝  ██║   ██║██║╚██╗██║██║     ██╔══╝  ██╔══██╗██║     ██╔══╝
    ██║        ██║   ██║     ╚██████╔╝██║ ╚████║╚██████╗███████╗██████╔╝███████╗███████╗
    ╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ ╚══════╝╚══════╝

Provides the base to use while working with tests that require global mocking.

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Special thanks:
    https://pyfunceble.github.io/special-thanks.html

Contributors:
    https://pyfunceble.github.io/contributors.html

Project link:
    https://github.com/funilrys/PyFunceble

Project documentation:
    https://pyfunceble.readthedocs.io/en/dev/

Project homepage:
    https://pyfunceble.github.io/

License:
::


    Copyright 2017, 2018, 2019, 2020, 2022, 2023 Nissar Chababy

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

import copy
import unittest

from PyFunceble.dataset.iana import IanaDataset
from PyFunceble.dataset.public_suffix import PublicSuffixDataset
from PyFunceble.dataset.user_agent import UserAgentDataset
from PyFunceble.downloader.iana import IANADownloader
from PyFunceble.downloader.public_suffix import PublicSuffixDownloader
from PyFunceble.downloader.user_agents import UserAgentsDownloader

try:
    import pyf_test_dataset
except (ModuleNotFoundError, ImportError):  # pragma: no cover
    from . import pyf_test_dataset


class PyFuncebleTestsBase(unittest.TestCase):
    """
    Use when you want to avoid using the network to fetch crucial datasets.
    """

    IANA_DATASET = pyf_test_dataset.IANA_DATASETS
    USER_AGENT_DATASET = pyf_test_dataset.USER_AGENT_DATASETS
    PSL_DATASET = pyf_test_dataset.PSL_DATASETS

    def setUp(self) -> None:
        """
        Setups everything needed by the tests.
        """

        self.psl_downloader_patch = unittest.mock.patch.object(
            PublicSuffixDownloader, "start"
        )
        self.psl_downloader_start = self.psl_downloader_patch.start()
        self.psl_downloader_start.return_value = None

        self.psl_get_content_patch = unittest.mock.patch.object(
            PublicSuffixDataset, "get_content"
        )
        self.mock_psl_get_content = self.psl_get_content_patch.start()
        self.mock_psl_get_content.return_value = copy.deepcopy(self.PSL_DATASET)

        self.ua_downloader_patch = unittest.mock.patch.object(
            UserAgentsDownloader, "start"
        )
        self.ua_downloader_start = self.ua_downloader_patch.start()
        self.ua_downloader_start.return_value = None

        self.ua_get_content_patch = unittest.mock.patch.object(
            UserAgentDataset, "get_content"
        )
        self.mock_ua_get_content = self.ua_get_content_patch.start()
        self.mock_ua_get_content.return_value = copy.deepcopy(self.USER_AGENT_DATASET)

        self.iana_downloader_patch = unittest.mock.patch.object(IANADownloader, "start")
        self.mock_downloader_start = self.iana_downloader_patch.start()
        self.mock_downloader_start.return_value = None

        self.iana_get_content_patch = unittest.mock.patch.object(
            IanaDataset, "get_content"
        )
        self.mock_iana_get_content = self.iana_get_content_patch.start()
        self.mock_iana_get_content.return_value = copy.deepcopy(self.IANA_DATASET)

    def tearDown(self) -> None:
        """
        Destroys everything needed by the tests.
        """

        self.iana_get_content_patch.stop()
        self.iana_downloader_patch.stop()

        self.ua_get_content_patch.stop()
        self.ua_downloader_patch.stop()

        self.psl_downloader_patch.stop()
        self.psl_get_content_patch.stop()

        del self.mock_iana_get_content
        del self.mock_downloader_start
