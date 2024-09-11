"""migration

Revision ID: 0d0bbded9d7c
Revises: 
Create Date: 2024-09-11 13:44:17.717543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d0bbded9d7c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Booktitle', sa.String(length=150), nullable=False))
        batch_op.drop_column('title')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.VARCHAR(length=150), autoincrement=False, nullable=False))
        batch_op.drop_column('Booktitle')

    # ### end Alembic commands ###