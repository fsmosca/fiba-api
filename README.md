# FIBA API
FIBA API on world cup game results. It uses fastapi framework and is hosted by fly.io.

If you want to test this locally, clone this repo, install the libraies in requirements.txt and send the command `uvicorn main:app --reload`.

## Endpoints

* https://apifiba.fly.dev/worldcup/2023/championship
* https://apifiba.fly.dev/worldcup/2023/qualifier

The `championship` endpoint has a single query parameter called team. While the `qualifier` has two namely zone and team.

Examples:

https://apifiba.fly.dev/worldcup/2023/championship?team=ger

https://apifiba.fly.dev/worldcup/2023/qualifier?zone=africa

You can access the api docs at https://apifiba.fly.dev/docs

## Usage

### Get all game results from the world cup 2023 championship

```
https://apifiba.fly.dev/worldcup/2023/championship
```

### Get all game results from the world cup 2023 championship of a given team

```
https://apifiba.fly.dev/worldcup/2023/championship?team=usa
```

output

```
[
  {
    "C1": "USA",
    "C1S": 99,
    "C2": "NZL",
    "C2S": 72,
    "GI": 1,
    "DP": "2023.08.26",
    "LOC": "City, Arena: Manila (PHI), Mall of Asia Arena",
    "EVENT": "FIBA World Cup 2023"
  },
  {
    "C1": "GRE",
    "C1S": 81,
    "C2": "USA",
    "C2S": 109,
    "GI": 2,
    "DP": "2023.08.28",
    "LOC": "City, Arena: Manila (PHI), Mall of Asia Arena",
    "EVENT": "FIBA World Cup 2023"
  },
  {
    "C1": "USA",
    "C1S": 110,
    "C2": "JOR",
    "C2S": 62,
    "GI": 3,
    "DP": "2023.08.30",
    "LOC": "City, Arena: Manila (PHI), Mall of Asia Arena",
    "EVENT": "FIBA World Cup 2023"
  },
  {
    "C1": "USA",
    "C1S": 85,
    "C2": "MNE",
    "C2S": 73,
    "GI": 4,
    "DP": "2023.09.01",
    "LOC": "City, Arena: Manila (PHI), Mall of Asia Arena",
    "EVENT": "FIBA World Cup 2023"
  },
  {
    "C1": "USA",
    "C1S": 104,
    "C2": "LTU",
    "C2S": 110,
    "GI": 5,
    "DP": "2023.09.03",
    "LOC": "City, Arena: Manila (PHI), Mall of Asia Arena",
    "EVENT": "FIBA World Cup 2023"
  },
  {
    "C1": "ITA",
    "C1S": 63,
    "C2": "USA",
    "C2S": 100,
    "GI": 6,
    "DP": "2023.09.05",
    "LOC": "City, Arena: Manila (PHI), Mall of Asia Arena",
    "EVENT": "FIBA World Cup 2023"
  },
  {
    "C1": "USA",
    "C1S": 111,
    "C2": "GER",
    "C2S": 113,
    "GI": 7,
    "DP": "2023.09.08",
    "LOC": "City, Arena: Manila (PHI), Mall of Asia Arena",
    "EVENT": "FIBA World Cup 2023"
  },
  {
    "C1": "USA",
    "C1S": 118,
    "C2": "CAN",
    "C2S": 127,
    "GI": 8,
    "DP": "2023.09.10",
    "LOC": "City, Arena: Manila (PHI), Mall of Asia Arena",
    "EVENT": "FIBA World Cup 2023"
  }
]
```

### Get all game results from the world cup 2023 qualifier

```
https://apifiba.fly.dev/worldcup/2023/qualifier
```

### Get all game results from the world cup 2023 qualifier from europe zone

```
https://apifiba.fly.dev/worldcup/2023/qualifier?zone=europe
```

Other valid zone values are: africa, americas and asia

### Get all game results from the world cup 2023 qualifier of team Germany

```
https://apifiba.fly.dev/worldcup/2023/qualifier?team=ger
```

## Credits

* [FIBA](https://www.fiba.basketball/)
* [Fly.io](https://fly.io/)
* [FastAPI](https://fastapi.tiangolo.com/)

