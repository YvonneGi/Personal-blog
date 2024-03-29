"""Initial Migration

Revision ID: d1f65868d76c
Revises: 54ec0acae218
Create Date: 2019-10-01 16:38:44.947761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1f65868d76c'
down_revision = '54ec0acae218'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('subscriptions_user_id_fkey', 'subscriptions', type_='foreignkey')
    op.drop_column('subscriptions', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscriptions', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('subscriptions_user_id_fkey', 'subscriptions', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###
