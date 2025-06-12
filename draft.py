league = {"01":["Colo-Colo"], "02":["Universidad de Chile"],
"03":["Universidad Católica"], "04":["Union Española"], "05":["Magallanes"]}

for key, teams in league.items():
    print(key, teams[0])

for i in league:
    print(league[i])