"""empty message

Revision ID: b0826d4affba
Revises: fb7cd547da7a
Create Date: 2018-11-02 18:05:10.774220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0826d4affba'
down_revision = 'fb7cd547da7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('show_time', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show_time', sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
