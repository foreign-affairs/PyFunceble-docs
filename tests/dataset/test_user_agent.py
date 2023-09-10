"""
The tool to check the availability or syntax of domain, IP or URL.

::


    ██████╗ ██╗   ██╗███████╗██╗   ██╗███╗   ██╗ ██████╗███████╗██████╗ ██╗     ███████╗
    ██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║████╗  ██║██╔════╝██╔════╝██╔══██╗██║     ██╔════╝
    ██████╔╝ ╚████╔╝ █████╗  ██║   ██║██╔██╗ ██║██║     █████╗  ██████╔╝██║     █████╗
    ██╔═══╝   ╚██╔╝  ██╔══╝  ██║   ██║██║╚██╗██║██║     ██╔══╝  ██╔══██╗██║     ██╔══╝
    ██║        ██║   ██║     ╚██████╔╝██║ ╚████║╚██████╗███████╗██████╔╝███████╗███████╗
    ╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ ╚══════╝╚══════╝

Tests of the user agent dataset interaction.

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


    Copyright 2017, 2018, 2019, 2020, 2021, 2021 Nissar Chababy

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
import json
import tempfile
import unittest
import unittest.mock

from PyFunceble.config.loader import ConfigLoader
from PyFunceble.dataset.base import DatasetBase
from PyFunceble.dataset.user_agent import UserAgentDataset

try:
    from pyfunceble_tests_base import PyFuncebleTestsBase
except ModuleNotFoundError:  # pragma: no cover
    from ..pyfunceble_tests_base import PyFuncebleTestsBase


class TestUserAgentDataset(PyFuncebleTestsBase):
    """
    Tests the user agent dataset interaction.
    """

    def setUp(self) -> None:
        """
        Setups everything needed by the tests.
        """

        super().setUp()

        self.config_loader = ConfigLoader()

        self.tempfile = tempfile.NamedTemporaryFile()

        self.tempfile.write(json.dumps(self.USER_AGENT_DATASET).encode())
        self.tempfile.seek(0)

        self.user_agent_dataset = UserAgentDataset()
        self.user_agent_dataset.source_file = self.tempfile.name

        self.get_content_patch = unittest.mock.patch.object(DatasetBase, "get_content")
        self.mock_get_content = self.get_content_patch.start()
        self.mock_get_content.return_value = copy.deepcopy(self.USER_AGENT_DATASET)

    def tearDown(self) -> None:
        """
        Destroys everything needed by the tests.
        """

        self.get_content_patch.stop()
        del self.mock_get_content
        del self.tempfile
        del self.config_loader
        del self.user_agent_dataset

        super().tearDown()

    def test_contains(self) -> None:
        """
        Tests of the method which let us check if a given browser is into the
        dataset.
        """

        given = "chrome"
        expected = True

        actual = given in self.user_agent_dataset

        self.assertEqual(expected, actual)

    def test_not_contains(self) -> None:
        """
        Tests the method which let us check if a given platform is into the
        dataset.
        """

        given = "vivaldi"
        expected = False

        actual = given in self.user_agent_dataset

        self.assertEqual(expected, actual)

    def test_get_all_from_browser(self) -> None:
        """
        Tests the way to get every information of a given browser.
        """

        given = "chrome"
        expected = copy.deepcopy(self.USER_AGENT_DATASET[given])

        actual = self.user_agent_dataset[given]

        self.assertEqual(expected, actual)

    def test_get_all_from_unknown_browser(self) -> None:
        """
        Tests the way to get every information of a given browser.

        In this test, we try to get from something that does not exists.
        """

        given = "vivaldi"
        expected = dict()  # pylint: disable=use-dict-literal

        actual = self.user_agent_dataset[given]

        self.assertEqual(expected, actual)

    def test_is_supported_browser(self) -> None:
        """
        Tests the method which let us check if a browser is supported.
        """

        given = "chrome"
        expected = True

        actual = self.user_agent_dataset.is_supported_browser(given)

        self.assertEqual(expected, actual)

    def test_is_not_supported_browser(self) -> None:
        """
        Tests teh method which let us check if a browser is supported for the
        case that the given browser is not supported.
        """

        given = "vivaldi"
        expected = False

        actual = self.user_agent_dataset.is_supported_browser(given)

        self.assertEqual(expected, actual)

    def test_is_supported_browser_not_str(self) -> None:
        """
        Tests the method which let us check if a browser is supported for the
        case the given browser not is not a string.
        """

        given = ["Hello", "World"]

        self.assertRaises(
            TypeError, lambda: self.user_agent_dataset.is_supported_browser(given)
        )

    def test_is_supported(self) -> None:
        """
        Tests the method which let us check if a browser and platform is
        supported.
        """

        given_browser = "chrome"
        given_platform = "linux"
        expected = True

        actual = self.user_agent_dataset.is_supported(given_browser, given_platform)

        self.assertEqual(expected, actual)

    def test_is_supported_not_str_browser(self) -> None:
        """
        Tests the method which let us check if a browser and platform is
        supported.

        In this test, we check the case that the given browser is not a string.
        """

        given_browser = ["Hello", "World"]
        given_platform = "linux"

        self.assertRaises(
            TypeError,
            lambda: self.user_agent_dataset.is_supported(given_browser, given_platform),
        )

    def test_is_supported_not_str_platform(self) -> None:
        """
        Tests the method which let us check if a browser and platform is
        supported.

        In this test, we check the case that the given platform is not a string.
        """

        given_browser = "chrome"
        given_platform = ["Hello", "Worl"]

        self.assertRaises(
            TypeError,
            lambda: self.user_agent_dataset.is_supported(given_browser, given_platform),
        )

    def test_is_supported_unknown_browser(self) -> None:
        """
        Tests the method which let us check if a browser and platform is
        supported.

        In this test, we check the case that the given browser is not known.
        """

        given_browser = "vivaldi"
        given_platform = "linux"
        expected = False

        actual = self.user_agent_dataset.is_supported(given_browser, given_platform)

        self.assertEqual(expected, actual)

    def test_is_supported_unknown_platform(self) -> None:
        """
        Tests the method which let us check if a browser and platform is
        supported.

        In this test, we check the case that the given platform is not known.
        """

        given_browser = "chrome"
        given_platform = "bsd"
        expected = False

        actual = self.user_agent_dataset.is_supported(given_browser, given_platform)

        self.assertEqual(expected, actual)

    def test_is_supported_unknown_platform_and_browser(self) -> None:
        """
        Tests the method which let us check if a browser and platform is
        supported.

        In this test, we check the case that the given platform and browser
        are not known.
        """

        given_browser = "vivaldi"
        given_platform = "bsd"
        expected = False

        actual = self.user_agent_dataset.is_supported(given_browser, given_platform)

        self.assertEqual(expected, actual)

    def test_set_prefered(self) -> None:
        """
        Tests the method which let us set our prefered browser and platform.
        """

        given_browser = "chrome"
        given_platform = "win10"

        actual = self.user_agent_dataset.set_prefered(given_browser, given_platform)

        self.assertIsInstance(actual, UserAgentDataset)

        expected_platform = "win10"
        expected_browser = "chrome"
        actual_platform = self.user_agent_dataset.prefered_platform
        actual_browser = self.user_agent_dataset.prefered_browser

        self.assertEqual(expected_platform, actual_platform)
        self.assertEqual(expected_browser, actual_browser)

    def test_set_prefered_not_supported(self) -> None:
        """
        Tests the method which let us set our prefered browser and platform.

        In this test, we check that an exception is correctly raised when
        the platform or browser is not supported.
        """

        given_browser = "vivaldi"
        given_platform = "win10"

        self.assertRaises(
            ValueError,
            lambda: self.user_agent_dataset.set_prefered(given_browser, given_platform),
        )

        given_browser = "vivaldi"
        given_platform = "bsd"

        self.assertRaises(
            ValueError,
            lambda: self.user_agent_dataset.set_prefered(given_browser, given_platform),
        )

    def test_get_latest(self) -> None:
        """
        Tests the method which let us get the latest user agent known.
        """

        given_browser = "chrome"
        given_platform = "win10"

        expected = self.USER_AGENT_DATASET[given_browser][given_platform]

        self.user_agent_dataset.set_prefered(given_browser, given_platform)

        actual = self.user_agent_dataset.get_latest()

        self.assertEqual(expected, actual)

    def test_get_latest_from_config(self) -> None:
        """
        Tests the method which let us get the latest user agent known based
        on the settings from the configuration file.
        """

        given_browser = "firefox"
        given_platform = "win10"

        self.config_loader.custom_config = {
            "user_agent": {"platform": given_platform, "browser": given_browser}
        }
        self.config_loader.start()

        expected = self.USER_AGENT_DATASET[given_browser][given_platform]

        actual = self.user_agent_dataset.get_latest()

        self.assertEqual(expected, actual)

    def test_get_latest_from_config_custom(self) -> None:
        """
        Tests the method which let us get the latest user agent known based
        on the settings from the configuration file.
        """

        self.config_loader.custom_config = {"user_agent": {"custom": "Hello, World!"}}
        self.config_loader.start()

        expected = "Hello, World!"

        actual = self.user_agent_dataset.get_latest()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
