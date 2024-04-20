"""Trips

Revision ID: 907ede9189e0
Revises: 839fb4aed346
Create Date: 2024-04-20 17:55:42.279345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '907ede9189e0'
down_revision = '839fb4aed346'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trips',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('departure_time', sa.DateTime(), nullable=False),
    sa.Column('arrival_time', sa.DateTime(), nullable=False),
    sa.Column('route', sa.String(length=100), nullable=False),
    sa.Column('bus_identifier', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(length=20), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('role')

    op.drop_table('trips')
    # ### end Alembic commands ###
