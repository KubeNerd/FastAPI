import pytest
from application.database.connection import Session

@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()