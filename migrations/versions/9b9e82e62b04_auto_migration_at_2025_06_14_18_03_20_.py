"""Auto migration at 2025-06-14_18-03-20 (commit 9432efa)

Revision ID: 9b9e82e62b04
Revises: 
Create Date: 2025-06-14 18:03:24.984936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b9e82e62b04'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('cooking_method', sa.String(length=100), nullable=False),
    sa.Column('ingredients', sa.JSON(), nullable=False),
    sa.Column('seasoning', sa.JSON(), nullable=True),
    sa.Column('cooking_time', sa.Integer(), nullable=False),
    sa.Column('instructions', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipes')
    # ### end Alembic commands ###
