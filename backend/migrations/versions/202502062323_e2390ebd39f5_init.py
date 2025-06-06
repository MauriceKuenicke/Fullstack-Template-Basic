"""test

Revision ID: e2390ebd39f5
Revises: 
Create Date: 2025-02-06 23:23:41.785183

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'e2390ebd39f5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE users (
            user_uuid TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL,
            PRIMARY KEY (user_uuid)
        )
    """)


def downgrade() -> None:
    op.execute("""
        DROP TABLE users CASCADE
    """)
