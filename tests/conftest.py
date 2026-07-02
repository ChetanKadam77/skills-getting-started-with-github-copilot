import copy

import pytest

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_activity_store():
    original_activities = copy.deepcopy(app_module.activities)
    app_module.activities = copy.deepcopy(original_activities)
    yield
    app_module.activities = copy.deepcopy(original_activities)
