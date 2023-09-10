import copy
import json
import tempfile
import unittest
from PyFunceble.dataset.base import DatasetBase

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
