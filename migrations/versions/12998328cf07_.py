"""empty message

Revision ID: 12998328cf07
Revises: 
Create Date: 2020-09-02 13:40:49.976677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12998328cf07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('portfolio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('symbol', sa.String(length=120), nullable=False),
    sa.Column('companyName', sa.String(length=120), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('shares', sa.Integer(), nullable=False),
    sa.Column('totalReturn', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('symbol', sa.String(length=120), nullable=False),
    sa.Column('transactionName', sa.String(length=120), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=80), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction')
    op.drop_table('portfolio')
    op.drop_table('user')
    # ### end Alembic commands ###
