import pytest

from testdatas import global_data as GD
from api.class_attend import ClassAttend


@pytest.fixture(scope='session', autouse=True)
def setup_session():
    ca = ClassAttend(GD.student[0], GD.student[1])
    ca.join_class('BG8W6H')