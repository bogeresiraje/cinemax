"""empty message

Revision ID: 18d7a7725a6c
Revises: 0beb7b2e16f8
Create Date: 2018-11-13 02:24:24.408971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18d7a7725a6c'
down_revision = '0beb7b2e16f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show_time', sa.Column('seats_remained', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('show_time', 'seats_remained')
    # ### end Alembic commands ###
