#!/usr/bin/env python3
"""
team selection from squad
"""
from flask import jsonify, render_template, request, flash, redirect, url_for
from models.players import Player
from models.basemodel import app
from routes import pick_bp
from flask_login import login_required, current_user
from models.teams import FPLTeam


@pick_bp.route('/my_team',  methods=['GET'], strict_slashes=False)
@login_required
def index():
    user = current_user

    # check if user has created a team
    if not user.team:
        return redirect(url_for('team_create.index'))

    team = {
        'name': user.team.name,
        'points': user.team.points,
        'budget': user.team.budget,
        'players': [{
            'id': player.id,
            'name': player.name,
            'position': player.position,
            'point': player.point,
            'cost': player.cost,
            'image': player.image,
            'selected_by_percentage': player.selected_by_percentage,
            'points_per_game': player.points_per_game,
        } for player in user.team.players],
        'starting_players': [{
            'id': player.id,
            'name': player.name,
            'position': player.position,
            'point': player.point,
            'cost': player.cost,
            'image': player.image,
            'selected_by_percentage': player.selected_by_percentage,
            'points_per_game': player.points_per_game,
            # 'position': position
        } for player in user.team.starting_players],
        'bench_players': [{
            'id': player.id,
            'name': player.name,
            'position': player.position,
            'point': player.point,
            'cost': player.cost,
            'image': player.image,
            'selected_by_percentage': player.selected_by_percentage,
            'points_per_game': player.points_per_game,
        } for player in user.team.bench_players],
    }

    return render_template('pick-team.html', team=team)


@pick_bp.route('/save_my_team',  methods=['POST'])
@login_required
def save_my_team():
    user = current_user

    # check if user has created a team
    if not user.team:
        return redirect(url_for('team_create.index'))

    starting_players = request.form.get('starting_players')
    bench_players = request.form.get('bench_players')
    staring_players_arr = starting_players.split(',')
    bench_players_arr = bench_players.split(',')

    if len(staring_players_arr) != 11:
        print("select 11 starting players")
        flash('select 11 starting players', 'danger')
        return redirect(url_for('my_team.index'))

    if len(bench_players_arr) != 4:
        print("select 4 bench players")
        flash('select 4 bench players', 'danger')
        return redirect(url_for('my_team.index'))
    
    players = {}

    for player in user.team.players:
        players[player.id] = player

    user.team.starting_players = []
    user.team.bench_players = []

    for player_id in staring_players_arr:
        if player_id not in players:
            flash('invalid player ids', 'danger')
            return redirect(url_for('my_team.index'))
        else:
            user.team.starting_players.append(players[player_id])

    for player_id in bench_players_arr:
        if player_id not in players:
            flash('invalid player ids', 'danger')
            return redirect(url_for('my_team.index'))
        else:
            user.team.bench_players.append(players[player_id])

    user.team.save()
    return redirect(url_for('my_team.index'))
