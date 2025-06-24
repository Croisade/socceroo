from enum import Enum
import re

class MatchLogTypes(Enum):
    Shooting = "shooting"
    GoalKeeping ="keeper"
    Passing = "passing"
    PassTypes = "passing_types"
    GoalAndShotCreation = "gca"
    DefensiveActions = "defense"
    Possession = "possession"
    Misc = "misc"

class Club(Enum):
    Philadelphia = "Philadelphia-Union"
    Cincinnati = "FC-Cincinnati"
    Nashville = "Nashville-SC"
    Columbus = "Columbus-Crew"
    Orlando = "Orlando-City"
    Miami = "Inter-Miami"
    NYCFC = "New-York-City-FC"
    NYRB = "New-York-Red-Bulls"
    Charlotte = "Charlotte-FC"
    Chicago = "Chicago-Fire"
    NewEngland = "New-England-Revolution"
    DC = "DC-United"
    Atlanta = "Atlanta-United"
    Toronto = "Toronto-FC"
    Montreal = "CF-Montreal"
    Vancouver = "Vancouver-Whitecaps-FC"
    SanDiego = "San-Diego-FC"
    Minnesota = "Minnesota-United"
    Portland = "Portland-Timbers"
    LAFC = "Los-Angeles-FC"
    Seattle = "Seattle-Sounders"
    Austin = "Austin-FC"
    SanJose = "San-Jose-Earthquakes"
    Colorado = "Colorado-Rapids"
    Dallas = "FC-Dallas"
    Houston = "Houston-Dynamo"
    SaltLake = "Real-Salt-Lake"
    KansasCity = "Sporting-Kansas-City"
    StLouis = "St-Louis-City"
    LosAngeles = "LA-Galaxy"

class Features(Enum):
    Sh = "SH"
    SoT = "SoT"
    SCA = "SCA"
    GCA = "GCA"
    GF = "GF"
    npxG = "npxG"
    Pts = "Pts"
    Result = "Result"
    Team = "Team"

class OddsMatchColumn(Enum):
    SEASON = "Season"
    DATE = "Date"
    HOME_TEAM = "Home Team"
    AWAY_TEAM = "Away Team"
    RESULT = "Full Time Result"
    AWAY_ODDS = "Industry Average Away Team Win Odds (American)"
    DRAW_ODDS = "Industry Average Draw Odds (American)"
    HOME_ODDS = "Industry Average Home Team Win Odds (American)"

def get_data_url(club: Club, logType, year):
    code = club_code[club]
    return f"https://fbref.com/en/squads/{code}/{year}/matchlogs/all_comps/{logType}/{club.value}-Match-Logs-All-Competitions"

def get_data_directory_matches(year):
    return f"../../data/MLS_Matches_fb_ref_{year}.csv"

def get_features():
    features = []
    for feature in Features:
        if feature == Features.Team or feature == Features.Pts or feature == Features.Result:
            continue
        features.append(feature.value)
    return features

def extract_number(val):
    if isinstance(val, str):
        match = re.match(r"(\d+)", val)
        return int(match.group(1)) if match else None
    return val  # already numeric

DIRECTORY_COMBINED_MATCHES_CLEAN_AGG = "../../data/MLS_Matches_fb_ref_combined_clean_agg.csv"

DIRECTORY_COMBINED_MATCHES_CLEAN = "../../data/MLS_Matches_fb_ref_combined.csv"

DIRECTORY_COMBINED_MATCHES_WITH_FEATURES = "../../data/MLS_Matches_fb_ref_combined_matches.csv"

DIRECTORY_MLS_MODEL = "../../data/mls_model.joblib"

DIRECTORY_MLS_MATCHES_ODDS = "../../data/MLS_Matches_odds_clean.csv"

club_code = {
    Club.Philadelphia: "46024eeb",
    Club.Cincinnati: "e9ea41b2",
    Club.Nashville: "35f1b818",
    Club.Columbus: "529ba333",
    Club.Orlando: "46ef01d0",
    Club.Miami: "cb8b86a2",
    Club.NYCFC: "64e81410",
    Club.NYRB: "69a0fb10",
    Club.Charlotte: "eb57545a",
    Club.Chicago: "f9940243",
    Club.NewEngland: "3c079def",
    Club.DC: "44117292",
    Club.Atlanta: "1ebc1a5b",
    Club.Toronto: "130f43fa",
    Club.Montreal: "fc22273c",
    Club.Vancouver: "ab41cb90",
    Club.SanDiego: "91b092e1",
    Club.Minnesota:"99ea75a6",
    Club.Portland: "d076914e",
    Club.LAFC: "81d817a3",
    Club.Seattle: "6218ebd4",
    Club.Austin: "b918956d",
    Club.SanJose: "ca460650",
    Club.Colorado: "415b4465",
    Club.Dallas: "15cf8f40",
    Club.Houston: "0d885416",
    Club.SaltLake: "f7d86a43",
    Club.KansasCity: "4acb0537",
    Club.StLouis: "bd97ac1f",
    Club.LosAngeles: "d8b46897"
}

TEAM_NAME_TO_CLUB = {
    "Philadelphia Union": Club.Philadelphia,
    "FC Cincinnati": Club.Cincinnati,
    "Nashville SC": Club.Nashville,
    "Columbus Crew": Club.Columbus,
    "Orlando City": Club.Orlando,
    "Inter Miami": Club.Miami,
    "New York City": Club.NYCFC,
    "New York Red Bulls": Club.NYRB,
    "Charlotte": Club.Charlotte,
    "Chicago Fire": Club.Chicago,
    "New England Revolution": Club.NewEngland,
    "DC United": Club.DC,
    "Atlanta United": Club.Atlanta,
    "Atlanta Utd": Club.Atlanta,
    "Toronto FC": Club.Toronto,
    "CF Montreal": Club.Montreal,
    "Club de Foot Montreal": Club.Montreal,
    "Montreal Impact": Club.Montreal,
    "Vancouver Whitecaps": Club.Vancouver,
    "Seattle Sounders": Club.Seattle,
    "Portland Timbers": Club.Portland,
    "Austin FC": Club.Austin,
    "FC Dallas": Club.Dallas,
    "Colorado Rapids": Club.Colorado,
    "San Jose Earthquakes": Club.SanJose,
    "Los Angeles FC": Club.LAFC,
    "LA Galaxy": Club.LosAngeles,
    "Los Angeles Galaxy": Club.LosAngeles,
    "Houston Dynamo": Club.Houston,
    "Real Salt Lake": Club.SaltLake,
    "Sporting Kansas City": Club.KansasCity,
    "St. Louis City": Club.StLouis,
    "Minnesota United": Club.Minnesota,
    "Chivas USA": Club.LAFC  # ✅ special case
}


ATTR = {"id": "matchlogs_for"}

CURR_YEAR = 2025

LINEAR_COLS = ['SCA', 'GCA', 'GF_x', 'Sh_x','SoT', 'npxG', 'Result_x']

RELEVANT_YEARS = [2021,2022,2023,2024,2025]

POINTS_MAP = {'W': 3, 'D': 1, 'L': 0}

ODDS_COLUMN_VALUES = [col.value for col in OddsMatchColumn]