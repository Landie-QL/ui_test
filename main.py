import pytest

pytest.main(["--alluredir=outputs/allure",
             "--clean-alluredir",
             "-m not smokey"])