"""Add password_hash column to User model

Revision ID: 448f64b78dce
Revises: 792edc8a6762
Create Date: 2024-11-27 13:15:36.676243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '448f64b78dce'
down_revision = '792edc8a6762'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_superadmin', sa.Boolean(), nullable=True))
        batch_op.create_foreign_key('fk_admin_user_id', 'user', ['id'], ['id'])
        batch_op.drop_column('email')
        batch_op.drop_column('username')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password_hash')

    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=150), nullable=False))
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=150), nullable=False))
        batch_op.drop_constraint('fk_admin_user_id', type_='foreignkey')
        batch_op.drop_column('is_superadmin')

    # ### end Alembic commands ###

    # ### end Alembic commands ###