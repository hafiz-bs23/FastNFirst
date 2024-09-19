"""Add phone number column for User table

Revision ID: 93511731db3e
Revises: 
Create Date: 2024-09-19 09:35:33.750208

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93511731db3e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(20),nullable=True))


def downgrade() -> None:
    op.drop_column(
        'users',
        'phone_number'
    )
