"""empty message

Revision ID: 42a30f9ea82f
Revises: 6c3f4289fc9d
Create Date: 2022-06-18 19:36:21.330761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42a30f9ea82f'
down_revision = '6c3f4289fc9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('phone', sa.String(length=13), nullable=True),
    sa.Column('email', sa.String(length=320), nullable=True),
    sa.Column('message', sa.String(length=3000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact_message')
    # ### end Alembic commands ###
