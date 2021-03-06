"""empty message

Revision ID: ee2756b74bf0
Revises: 78aff81c79fe
Create Date: 2018-12-12 15:15:20.349627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee2756b74bf0'
down_revision = '78aff81c79fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('info_user', sa.Column('email', sa.String(length=128), nullable=False))
    op.create_unique_constraint(None, 'info_user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'info_user', type_='unique')
    op.drop_column('info_user', 'email')
    # ### end Alembic commands ###
