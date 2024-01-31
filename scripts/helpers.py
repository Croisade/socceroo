def calc_feats(df, team):
    team_stats = dict()
    df_team = df[(df["Team"]==team)]
    team_shots = df_team.apply(lambda x: x["Sh"], axis=1).sum()
    team_shots_ot = df_team.apply(lambda x: x["SoT"], axis=1).sum()
    team_shots_sca = df_team.apply(lambda x: x["SCA"], axis=1).sum()
    team_shots_gca = df_team.apply(lambda x: x["GCA"], axis=1).sum()
    team_shots_npxG = df_team.apply(lambda x: x["npxG"], axis=1).sum()
    team_shots_xA = df_team.apply(lambda x: x["xA"], axis=1).sum()
    team_points = df_team.apply(lambda x: x["Pts"], axis=1).sum()

    team_stats["team"] = team
    team_stats["shots"] = team_shots
    team_stats["shots_ot"] = team_shots_ot
    team_stats["sca"] = team_shots_sca
    team_stats["gca"] = team_shots_gca
    team_stats["npxG"] = team_shots_npxG
    team_stats["xA"] = team_shots_xA
    team_stats["points"] = team_points
    return team_stats

def calc_feats_match(df, team):
    team_stats = dict()
    df_team = df[(df["Team"]==team)]
    team_shots = df_team.apply(lambda x: x["Sh"], axis=1).sum()
    team_shots_ot = df_team.apply(lambda x: x["SoT"], axis=1).sum()
    team_shots_sca = df_team.apply(lambda x: x["SCA"], axis=1).sum()
    team_shots_gca = df_team.apply(lambda x: x["GCA"], axis=1).sum()
    team_shots_npxG = df_team.apply(lambda x: x["npxG"], axis=1).sum()
    team_shots_xA = df_team.apply(lambda x: x["xA"], axis=1).sum()
    team_points = df_team.apply(lambda x: 3 if ((x["HomeTeam"] == team and x["FTR"].startswith("W")) or (x["AwayTeam"] == team and x["FTR"].startswith("L"))) else (1 if x["FTR"].startswith("D") else 0), axis=1).sum()

    team_stats["team"] = team
    team_stats["shots"] = team_shots
    team_stats["shots_ot"] = team_shots_ot
    team_stats["sca"] = team_shots_sca
    team_stats["gca"] = team_shots_gca
    team_stats["npxG"] = team_shots_npxG
    team_stats["xA"] = team_shots_xA
    team_stats["points"] = team_points
    return team_stats

