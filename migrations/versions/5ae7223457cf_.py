"""empty message

Revision ID: 5ae7223457cf
Revises: 8b06064dc8b0
Create Date: 2023-08-14 08:38:59.530758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ae7223457cf'
down_revision = '8b06064dc8b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('starship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('names', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('starship')
    # ### end Alembic commands ###