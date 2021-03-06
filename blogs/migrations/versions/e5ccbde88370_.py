"""empty message

Revision ID: e5ccbde88370
Revises: c5ebf0eeaed9
Create Date: 2018-12-12 15:06:18.850395

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e5ccbde88370'
down_revision = 'c5ebf0eeaed9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('info_user', sa.Column('email', sa.String(length=64), nullable=False))
    op.drop_index('mobile', table_name='info_user')
    op.create_unique_constraint(None, 'info_user', ['email'])
    op.drop_column('info_user', 'mobile')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('info_user', sa.Column('mobile', mysql.VARCHAR(length=11), nullable=False))
    op.drop_constraint(None, 'info_user', type_='unique')
    op.create_index('mobile', 'info_user', ['mobile'], unique=True)
    op.drop_column('info_user', 'email')
    # ### end Alembic commands ###
