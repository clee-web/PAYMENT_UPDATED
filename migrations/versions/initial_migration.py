"""initial migration

Revision ID: initial_migration
Revises: 
Create Date: 2024-01-01 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'initial_migration'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create Student table
    op.create_table('student',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('phone', sa.String(length=20), nullable=False),
        sa.Column('residence', sa.String(length=100), nullable=False),
        sa.Column('class_name', sa.String(length=50), nullable=False),
        sa.Column('session', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id', name='pk_student')
    )

    # Create Teacher table
    op.create_table('teacher',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('phone', sa.String(length=20), nullable=False),
        sa.Column('email', sa.String(length=120), nullable=True),
        sa.Column('qualification', sa.String(length=200), nullable=True),
        sa.Column('subject', sa.String(length=100), nullable=True),
        sa.Column('joining_date', sa.DateTime(), nullable=True),
        sa.Column('credentials_file', sa.String(length=200), nullable=True),
        sa.PrimaryKeyConstraint('id', name='pk_teacher'),
        sa.UniqueConstraint('email', name='uq_teacher_email')
    )

    # Create Payment table
    op.create_table('payment',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('transaction_number', sa.String(length=20), nullable=False),
        sa.Column('amount', sa.Float(), nullable=False),
        sa.Column('payment_type', sa.String(length=50), nullable=False),
        sa.Column('date', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['student_id'], ['student.id'], name='fk_payment_student'),
        sa.PrimaryKeyConstraint('id', name='pk_payment'),
        sa.UniqueConstraint('transaction_number', name='uq_payment_transaction_number')
    )

def downgrade():
    op.drop_table('payment')
    op.drop_table('teacher')
    op.drop_table('student') 