import pytest


@pytest.mark.usefixtures("setUp_meta")
class BaseTestMeta:
    pass


@pytest.mark.usefixtures("setUp_amazon")
class BaseTestAmazon:
    pass
