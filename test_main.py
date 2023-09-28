"""Tests endpoints

pip install httpx
"""


from fastapi.testclient import TestClient
from main import app


WC2023_CHAMPIONSHIP_USA = [{"C1":"USA","C1S":99,"C2":"NZL","C2S":72,"GI":1,"DP":"2023.08.26","LOC":"City, Arena: Manila (PHI), Mall of Asia Arena","EVENT":"FIBA World Cup 2023"},{"C1":"GRE","C1S":81,"C2":"USA","C2S":109,"GI":2,"DP":"2023.08.28","LOC":"City, Arena: Manila (PHI), Mall of Asia Arena","EVENT":"FIBA World Cup 2023"},{"C1":"USA","C1S":110,"C2":"JOR","C2S":62,"GI":3,"DP":"2023.08.30","LOC":"City, Arena: Manila (PHI), Mall of Asia Arena","EVENT":"FIBA World Cup 2023"},{"C1":"USA","C1S":85,"C2":"MNE","C2S":73,"GI":4,"DP":"2023.09.01","LOC":"City, Arena: Manila (PHI), Mall of Asia Arena","EVENT":"FIBA World Cup 2023"},{"C1":"USA","C1S":104,"C2":"LTU","C2S":110,"GI":5,"DP":"2023.09.03","LOC":"City, Arena: Manila (PHI), Mall of Asia Arena","EVENT":"FIBA World Cup 2023"},{"C1":"ITA","C1S":63,"C2":"USA","C2S":100,"GI":6,"DP":"2023.09.05","LOC":"City, Arena: Manila (PHI), Mall of Asia Arena","EVENT":"FIBA World Cup 2023"},{"C1":"USA","C1S":111,"C2":"GER","C2S":113,"GI":7,"DP":"2023.09.08","LOC":"City, Arena: Manila (PHI), Mall of Asia Arena","EVENT":"FIBA World Cup 2023"},{"C1":"USA","C1S":118,"C2":"CAN","C2S":127,"GI":8,"DP":"2023.09.10","LOC":"City, Arena: Manila (PHI), Mall of Asia Arena","EVENT":"FIBA World Cup 2023"}]
WC2023_QUALIFIER_ZONE_ASIA = [{"C1":"IRI","C1S":82,"C2":"BRN","C2S":66,"GI":1,"DP":"2021.11.26","LOC":"City, Arena: Tehran (IRI), Azadi Basketball Hall","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"JOR","C1S":68,"C2":"KSA","C2S":61,"GI":1,"DP":"2021.11.26","LOC":"City, Arena: Amman (JOR), Prince Hamza","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"LBN","C1S":96,"C2":"INA","C2S":38,"GI":1,"DP":"2021.11.26","LOC":"City, Arena: Zouk Mikael (LBN), Nouhad Nawfal Sports Complex","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"KAZ","C1S":84,"C2":"SYR","C2S":74,"GI":1,"DP":"2021.11.26","LOC":"City, Arena: Astana (KAZ), Republican Velodrome Saryarka","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"CHN","C1S":79,"C2":"JPN","C2S":63,"GI":1,"DP":"2021.11.27","LOC":"City, Arena: Sendai (JPN), Xebio Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"JPN","C1S":73,"C2":"CHN","C2S":106,"GI":2,"DP":"2021.11.28","LOC":"City, Arena: Sendai (JPN), Xebio Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"BRN","C1S":64,"C2":"IRI","C2S":100,"GI":2,"DP":"2021.11.29","LOC":"City, Arena: Manama (BRN), Khalifa Sport City","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"KSA","C1S":72,"C2":"JOR","C2S":64,"GI":2,"DP":"2021.11.29","LOC":"City, Arena: Jeddah (KSA), King Abdullah Sports City","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"INA","C1S":64,"C2":"LBN","C2S":110,"GI":2,"DP":"2021.11.29","LOC":"City, Arena: Zouk Mikael (LBN), Nouhad Nawfal Sports Complex","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"SYR","C1S":71,"C2":"KAZ","C2S":81,"GI":2,"DP":"2021.11.29","LOC":"City, Arena: Damascus (SYR), Al Fayhaa Stadium","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"NZL","C1S":101,"C2":"IND","C2S":46,"GI":1,"DP":"2022.02.24","LOC":"City, Arena: Quezon (PHI), Araneta Coliseum","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"IRI","C1S":69,"C2":"KAZ","C2S":73,"GI":3,"DP":"2022.02.24","LOC":"City, Arena: Tehran (IRI), Azadi Basketball Hall","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"KSA","C1S":95,"C2":"INA","C2S":66,"GI":3,"DP":"2022.02.24","LOC":"City, Arena: Jeddah (KSA), King Abdullah Sports City","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"JOR","C1S":74,"C2":"LBN","C2S":63,"GI":3,"DP":"2022.02.24","LOC":"City, Arena: Amman (JOR), Prince Hamza","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"BRN","C1S":64,"C2":"SYR","C2S":80,"GI":3,"DP":"2022.02.24","LOC":"City, Arena: Manama (BRN), Khalifa Sport City","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"IND","C1S":64,"C2":"PHI","C2S":88,"GI":1,"DP":"2022.02.25","LOC":"City, Arena: Quezon (PHI), Araneta Coliseum","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"AUS","C1S":98,"C2":"TPE","C2S":61,"GI":1,"DP":"2022.02.25","LOC":"City, Arena: Okinawa (JPN), Okinawa Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"TPE","C1S":71,"C2":"JPN","C2S":76,"GI":2,"DP":"2022.02.26","LOC":"City, Arena: Okinawa (JPN), Okinawa Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"NZL","C1S":88,"C2":"PHI","C2S":63,"GI":2,"DP":"2022.02.27","LOC":"City, Arena: Quezon (PHI), Araneta Coliseum","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"JOR","C1S":94,"C2":"INA","C2S":64,"GI":4,"DP":"2022.02.27","LOC":"City, Arena: Amman (JOR), Prince Hamza","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"AUS","C1S":80,"C2":"JPN","C2S":64,"GI":4,"DP":"2022.02.27","LOC":"City, Arena: Okinawa (JPN), Okinawa Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"BRN","C1S":48,"C2":"KAZ","C2S":95,"GI":4,"DP":"2022.02.27","LOC":"City, Arena: Manama (BRN), Khalifa Sport City","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"KSA","C1S":68,"C2":"LBN","C2S":81,"GI":4,"DP":"2022.02.27","LOC":"City, Arena: Jeddah (KSA), King Abdullah Sports City","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"IRI","C1S":80,"C2":"SYR","C2S":68,"GI":4,"DP":"2022.02.27","LOC":"City, Arena: Tehran (IRI), Azadi Basketball Hall","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"IND","C1S":60,"C2":"NZL","C2S":95,"GI":3,"DP":"2022.02.28","LOC":"City, Arena: Quezon (PHI), Araneta Coliseum","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"TPE","C1S":71,"C2":"AUS","C2S":90,"GI":3,"DP":"2022.02.28","LOC":"City, Arena: Okinawa (JPN), Okinawa Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"AUS","C1S":76,"C2":"CHN","C2S":69,"GI":3,"DP":"2022.06.30","LOC":"City, Arena: Melbourne (AUS), John Cain Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"PHI","C1S":60,"C2":"NZL","C2S":106,"GI":3,"DP":"2022.06.30","LOC":"City, Arena: Auckland (NZL), EventFinda Stadium","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"CHN","C1S":94,"C2":"TPE","C2S":58,"GI":4,"DP":"2022.07.01","LOC":"City, Arena: Melbourne (AUS), John Cain Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"JPN","C1S":52,"C2":"AUS","C2S":98,"GI":5,"DP":"2022.07.01","LOC":"City, Arena: Melbourne (AUS), John Cain Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"KAZ","C1S":68,"C2":"IRI","C2S":60,"GI":5,"DP":"2022.07.01","LOC":"City, Arena: Astana (KAZ), Republican Velodrome Saryarka","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"INA","C1S":67,"C2":"KSA","C2S":69,"GI":5,"DP":"2022.07.01","LOC":"City, Arena: Jakarta (INA), Istora Senayan","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"LBN","C1S":89,"C2":"JOR","C2S":70,"GI":5,"DP":"2022.07.01","LOC":"City, Arena: Zouk Mikael (LBN), Nouhad Nawfal Sports Complex","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"SYR","C1S":67,"C2":"BRN","C2S":76,"GI":5,"DP":"2022.07.01","LOC":"City, Arena: Aleppo (SYR), Al Hamadaniyeh Stadium","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"PHI","C1S":79,"C2":"IND","C2S":63,"GI":4,"DP":"2022.07.03","LOC":"City, Arena: Manila (PHI), Mall of Asia Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"CHN","C1S":48,"C2":"AUS","C2S":71,"GI":5,"DP":"2022.07.03","LOC":"City, Arena: Melbourne (AUS), John Cain Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"JPN","C1S":89,"C2":"TPE","C2S":49,"GI":5,"DP":"2022.07.03","LOC":"City, Arena: Melbourne (AUS), John Cain Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"INA","C1S":52,"C2":"JOR","C2S":77,"GI":6,"DP":"2022.07.04","LOC":"City, Arena: Jakarta (INA), Istora Senayan","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"KAZ","C1S":51,"C2":"BRN","C2S":62,"GI":6,"DP":"2022.07.04","LOC":"City, Arena: Astana (KAZ), Republican Velodrome Saryarka","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"LBN","C1S":90,"C2":"KSA","C2S":60,"GI":6,"DP":"2022.07.04","LOC":"City, Arena: Zouk Mikael (LBN), Nouhad Nawfal Sports Complex","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"SYR","C1S":56,"C2":"IRI","C2S":91,"GI":6,"DP":"2022.07.04","LOC":"City, Arena: Aleppo (SYR), Al Hamadaniyeh Stadium","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"TPE","C1S":56,"C2":"CHN","C2S":97,"GI":6,"DP":"2022.07.04","LOC":"City, Arena: Melbourne (AUS), John Cain Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"KSA","C1S":65,"C2":"NZL","C2S":80,"GI":5,"DP":"2022.08.25","LOC":"City, Arena: Dammam (KSA), Dammam Green Hall","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"LBN","C1S":85,"C2":"PHI","C2S":81,"GI":5,"DP":"2022.08.25","LOC":"City, Arena: Beirut (LBN), Nouhad Nawfal Sports Complex","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"BRN","C1S":50,"C2":"AUS","C2S":104,"GI":7,"DP":"2022.08.25","LOC":"City, Arena: Manama (BRN), Khalifa Sport City","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"JOR","C1S":80,"C2":"IND","C2S":64,"GI":7,"DP":"2022.08.25","LOC":"City, Arena: Amman (JOR), Prince Hamza","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"IRI","C1S":79,"C2":"JPN","C2S":68,"GI":7,"DP":"2022.08.25","LOC":"City, Arena: Tehran (IRI), Azadi Basketball Hall","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"KAZ","C1S":56,"C2":"CHN","C2S":68,"GI":7,"DP":"2022.08.25","LOC":"City, Arena: Astana (KAZ), Republican Velodrome Saryarka","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"NZL","C1S":100,"C2":"JOR","C2S":72,"GI":6,"DP":"2022.08.29","LOC":"City, Arena: Auckland (NZL), EventFinda Stadium","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"PHI","C1S":84,"C2":"KSA","C2S":46,"GI":6,"DP":"2022.08.29","LOC":"City, Arena: Manila (PHI), Mall of Asia Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"CHN","C1S":80,"C2":"BRN","C2S":67,"GI":8,"DP":"2022.08.29","LOC":"City, Arena: Astana (KAZ), Republican Velodrome Saryarka","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"AUS","C1S":98,"C2":"IRI","C2S":68,"GI":8,"DP":"2022.08.29","LOC":"City, Arena: Bendigo (AUS), Bendigo Stadium","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"IND","C1S":63,"C2":"LBN","C2S":95,"GI":8,"DP":"2022.08.29","LOC":"City, Arena: Bengaluru (IND), Sree Kanteerava Indoor Stadium","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"JPN","C1S":73,"C2":"KAZ","C2S":48,"GI":8,"DP":"2022.08.30","LOC":"City, Arena: Okinawa (JPN), Okinawa Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"LBN","C1S":77,"C2":"NZL","C2S":65,"GI":7,"DP":"2022.11.10","LOC":"City, Arena: Beirut (LBN), Pierre Gemayel Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"JOR","C1S":66,"C2":"PHI","C2S":74,"GI":7,"DP":"2022.11.10","LOC":"City, Arena: Amman (JOR), Prince Hamza","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"KSA","C1S":85,"C2":"IND","C2S":54,"GI":9,"DP":"2022.11.10","LOC":"City, Arena: Jeddah (KSA), King Abdullah Sports City","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"IRI","C1S":72,"C2":"CHN","C2S":81,"GI":9,"DP":"2022.11.11","LOC":"City, Arena: Tehran (IRI), Azadi Basketball Hall","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"BRN","C1S":74,"C2":"JPN","C2S":87,"GI":9,"DP":"2022.11.11","LOC":"City, Arena: Manama (BRN), Khalifa Sport City","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"KAZ","C1S":50,"C2":"AUS","C2S":97,"GI":9,"DP":"2022.11.11","LOC":"City, Arena: Astana (KAZ), Republican Velodrome Saryarka","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"JOR","C1S":92,"C2":"NZL","C2S":75,"GI":8,"DP":"2022.11.13","LOC":"City, Arena: Amman (JOR), Prince Hamza","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"KSA","C1S":63,"C2":"PHI","C2S":76,"GI":8,"DP":"2022.11.13","LOC":"City, Arena: Jeddah (KSA), King Abdullah Sports City","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"LBN","C1S":103,"C2":"IND","C2S":74,"GI":10,"DP":"2022.11.13","LOC":"City, Arena: Beirut (LBN), Pierre Gemayel Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"BRN","C1S":67,"C2":"CHN","C2S":80,"GI":10,"DP":"2022.11.14","LOC":"City, Arena: Manama (BRN), Khalifa Sport City","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"IRI","C1S":20,"C2":"AUS","C2S":0,"GI":10,"DP":"2022.11.14","LOC":"City, Arena: Tehran (IRI), Azadi Basketball Hall","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"KAZ","C1S":61,"C2":"JPN","C2S":81,"GI":10,"DP":"2022.11.14","LOC":"City, Arena: Astana (KAZ), Republican Velodrome Saryarka","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"AUS","C1S":83,"C2":"BRN","C2S":51,"GI":11,"DP":"2023.02.23","LOC":"City, Arena: Melbourne (AUS), State Basketball Centre","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"JPN","C1S":96,"C2":"IRI","C2S":61,"GI":11,"DP":"2023.02.23","LOC":"City, Arena: Takasaki (JPN), Takasaki Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"CHN","C1S":71,"C2":"KAZ","C2S":59,"GI":11,"DP":"2023.02.23","LOC":"City, Arena: Hong Kong (HKG), Tsuen Wan Stadium","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"NZL","C1S":110,"C2":"KSA","C2S":63,"GI":9,"DP":"2023.02.24","LOC":"City, Arena: Christchurch (NZL), Christchurch Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"PHI","C1S":107,"C2":"LBN","C2S":96,"GI":9,"DP":"2023.02.24","LOC":"City, Arena: Bulacan (PHI), Philippine Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"IND","C1S":63,"C2":"JOR","C2S":98,"GI":11,"DP":"2023.02.24","LOC":"City, Arena: Bengaluru (IND), Sree Kanteerava Indoor Stadium","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"CHN","C1S":86,"C2":"IRI","C2S":74,"GI":12,"DP":"2023.02.26","LOC":"City, Arena: Hong Kong (HKG), Tsuen Wan Stadium","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"JPN","C1S":95,"C2":"BRN","C2S":72,"GI":12,"DP":"2023.02.26","LOC":"City, Arena: Takasaki (JPN), Takasaki Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"AUS","C1S":98,"C2":"KAZ","C2S":53,"GI":12,"DP":"2023.02.26","LOC":"City, Arena: Melbourne (AUS), State Basketball Centre","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"NZL","C1S":106,"C2":"LBN","C2S":91,"GI":10,"DP":"2023.02.27","LOC":"City, Arena: Wellington (NZL), TSB Bank Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"PHI","C1S":90,"C2":"JOR","C2S":91,"GI":10,"DP":"2023.02.27","LOC":"City, Arena: Bulacan (PHI), Philippine Arena","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"},{"C1":"IND","C1S":60,"C2":"KSA","C2S":71,"GI":12,"DP":"2023.02.27","LOC":"City, Arena: Bengaluru (IND), Sree Kanteerava Indoor Stadium","EVENT":"FIBA World Cup 2023 Qualifier Asia","ZONE":"Asia"}]


client = TestClient(app)


def test_championship_team_usa():
    response = client.get("/worldcup/2023/championship?team=usa")
    assert response.status_code == 200
    assert response.json() == WC2023_CHAMPIONSHIP_USA


def test_qualifier_zone_asia():
    response = client.get("/worldcup/2023/qualifier?zone=asia")
    assert response.status_code == 200
    assert response.json() == WC2023_QUALIFIER_ZONE_ASIA