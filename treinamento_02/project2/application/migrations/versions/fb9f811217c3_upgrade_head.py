"""upgrade head

Revision ID: fb9f811217c3
Revises: 99a718f6b4c5
Create Date: 2025-04-06 01:14:01.935402

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb9f811217c3'
down_revision: Union[str, None] = '99a718f6b4c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
