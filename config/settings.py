from enum import Enum


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

def get_data_url(club: Club, logType, year):
    code = club_code[club]
    return f"https://fbref.com/en/squads/{code}/{year}/matchlogs/all_comps/{logType}/{club.value}-Match-Logs-All-Competitions"

attr = {"id": "matchlogs_for"}