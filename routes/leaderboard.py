#!/usr/bin/env python3
"""
leaderboard module
"""
from flask import render_template
from models.users import User
from models.teams import FPLTeam
from models.basemodel import db
from routes import league_bp


@league_bp.route('/leaderboard')
def leaderboard():
    # Query the database to get the team name and total points of all users
    users = db.session.query(User, FPLTeam).join(FPLTeam).all()
    
    # Calculate the total points for each user
    user_points = []
    for user, team in users:
        total_points = sum(player.points for player in user.players)
        user_points.append({
            'username': user.username,
            'team_name': team.name,
            'total_points': total_points
        })

    return render_template('leaderboard.html', user_points=user_points)

