#!/usr/bin/env python3
"""
Retrieving players from database
"""
from flask import jsonify, render_template, redirect, url_for, request, flash
from models.players import Player
from models.teams import FPLTeam
from models.basemodel import app
from routes import create_bp
from flask_login import login_required, current_user



@create_bp.route('/create_team',  methods=['GET'], strict_slashes=False)
@login_required
def index():
    clubs = ["Spurs", "Wolves", "Man Utd", "Crystal Palace", "Newcastle", "Sheffield Utd", "Brentford", "Burnley",
             "Luton", "Chelsea", "Fulham", "Bournemouth", "Nott'm Forest", "Everton", "Brighton", "Aston Villa", "Man City",
             "Arsenal", "Liverpool", "West Ham"]
             
    user = current_user

    # check if user has a team
    if user.team:
        return redirect(url_for('my_team.index'))

    players = Player.query.all()
    player_data = [{
        'id': player.id,
        'name': player.name,
        'position': player.position,
        'point': player.point,
        'cost': player.cost,
        'image': player.image,
        'selected_by_percentage': player.selected_by_percentage,
        'points_per_game': player.points_per_game,
    } for player in players]
    
    return render_template('create-team.html', player_data=player_data, clubs=clubs)

@create_bp.route("/save_team", methods=['POST'])
@login_required
def save_team():
    user = current_user

    if user.team:
        return redirect(url_for('my_team.index'))

    team_name = request.form.get('team_name')
    player_ids = request.form.get('player_ids')
    player_ids_arr = player_ids.split(',')

    if len(player_ids_arr) != 15:
        flash('select 15 players', 'danger')
        return redirect(url_for('team_create.index'))
    
    if not team_name:
        flash('Enter team name', 'danger')
        return redirect(url_for('team_create.index'))

    # check if player ids are valid
    players = Player.query.filter(Player.id.in_(player_ids_arr)).all()
    if len(players) != 15:
        flash('invalid player ids', 'danger')
        return redirect(url_for('team_create.index'))

    points = 0
    costs = 0
    for player in players:
        points += player.point
        costs += player.cost

    if costs > 100:
        flash('total cost cannot exceed $100', 'danger')
        return redirect(url_for('team_create.index'))

    team = FPLTeam(
        name=team_name,
        user_id=user.id,
        points=points,
        budget=costs,
        players=players,
        user=user
    )

    for i in range(0, 11):
        team.starting_players.append(players[i], { "position": str(i + 1) })

    for i in range(11, 15):
        team.bench_players.append(players[i])

    team.save()
    return redirect(url_for('my_team.index'))
