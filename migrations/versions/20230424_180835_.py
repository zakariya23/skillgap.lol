"""empty message

Revision ID: f9737b49945a
Revises: ffdc0a98111c
Create Date: 2023-04-24 18:08:35.492274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9737b49945a'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('players',
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('summoner_id', sa.String(), nullable=False),
    sa.Column('summoner_name', sa.String(), nullable=False),
    sa.Column('account_id', sa.String(), nullable=False),
    sa.Column('region', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('player_id'),
    sa.UniqueConstraint('account_id'),
    sa.UniqueConstraint('summoner_id')
    )
    op.create_table('champion_stats',
    sa.Column('champion_stats_id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('champion_id', sa.Integer(), nullable=False),
    sa.Column('champion_name', sa.String(), nullable=False),
    sa.Column('champion_points', sa.Integer(), nullable=False),
    sa.Column('champion_level', sa.Integer(), nullable=False),
    sa.Column('champion_mastery_score', sa.Integer(), nullable=False),
    sa.Column('last_play_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['player_id'], ['players.player_id'], ),
    sa.PrimaryKeyConstraint('champion_stats_id')
    )
    op.create_table('comparisons',
    sa.Column('comparison_id', sa.Integer(), nullable=False),
    sa.Column('player1_id', sa.Integer(), nullable=True),
    sa.Column('player2_id', sa.Integer(), nullable=True),
    sa.Column('winner_id', sa.Integer(), nullable=True),
    sa.Column('comparison_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['player1_id'], ['players.player_id'], ),
    sa.ForeignKeyConstraint(['player2_id'], ['players.player_id'], ),
    sa.ForeignKeyConstraint(['winner_id'], ['players.player_id'], ),
    sa.PrimaryKeyConstraint('comparison_id')
    )
    op.create_table('player_stats',
    sa.Column('stats_id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('queue_type', sa.String(), nullable=False),
    sa.Column('tier', sa.String(), nullable=False),
    sa.Column('rank', sa.String(), nullable=False),
    sa.Column('league_points', sa.Integer(), nullable=False),
    sa.Column('wins', sa.Integer(), nullable=False),
    sa.Column('losses', sa.Integer(), nullable=False),
    sa.Column('win_rate', sa.Float(), nullable=False),
    sa.Column('kda', sa.Float(), nullable=False),
    sa.Column('cs_per_min', sa.Float(), nullable=False),
    sa.Column('update_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['player_id'], ['players.player_id'], ),
    sa.PrimaryKeyConstraint('stats_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player_stats')
    op.drop_table('comparisons')
    op.drop_table('champion_stats')
    op.drop_table('players')
    # ### end Alembic commands ###