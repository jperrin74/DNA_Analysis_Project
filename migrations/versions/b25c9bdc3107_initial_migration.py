"""Initial migration.

Revision ID: b25c9bdc3107
Revises: 17cf1226df13
Create Date: 2024-08-19 08:20:40.683178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b25c9bdc3107'
down_revision = '17cf1226df13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dna_sequence',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sequence', sa.Text(), nullable=False),
    sa.Column('analysis_result', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dna_sequence')
    # ### end Alembic commands ###
