from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine import reflection

def upgrade():
    # Reflect the current state of the database
    bind = op.get_bind()
    inspector = reflection.Inspector.from_engine(bind)

    # Get the columns in the dna_sequence table
    columns = inspector.get_columns('dna_sequence')
    op.add_column('dna_sequence', sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.current_timestamp()))

    # Check if the analysis column exists
    if not any(column['name'] == 'analysis' for column in columns):
        with op.batch_alter_table('dna_sequence') as batch_op:
            batch_op.add_column(sa.Column('analysis', sa.Text(), nullable=False, server_default='No analysis'))

def downgrade():
    with op.batch_alter_table('dna_sequence') as batch_op:
        batch_op.drop_column('analysis')
        op.drop_column('dna_sequence', 'created_at')
