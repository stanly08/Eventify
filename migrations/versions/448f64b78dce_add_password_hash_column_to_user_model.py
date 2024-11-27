"""Add description to Event model

Revision ID: e42e962d3359
Revises: 448f64b78dce
Create Date: 2024-11-27 13:25:36.676243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e42e962d3359'
down_revision = '448f64b78dce'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.Text(), nullable=True))

    op.execute('UPDATE event SET description = "" WHERE description IS NULL')

    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.alter_column('description', existing_type=sa.Text(), nullable=False)


def downgrade():
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.drop_column('description')
