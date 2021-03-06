"""Add Bio and Profile Photo Columns

Revision ID: f8378c2d37e3
Revises: 722facb54158
Create Date: 2020-05-03 14:51:47.039999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8378c2d37e3'
down_revision = '722facb54158'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_photo_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_photo_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
