from typing import Optional, List, Dict

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import pandas as pd


ZONES = ['africa', 'americas', 'asia', 'europe']


app = FastAPI()


@app.get("/worldcup/2023/championship")
async def wordcup_2023_championship(team: Optional[str] = None) -> List[Dict]:
    """## Gets FIBA world cup 2023 championship game results.

    If team is not specified, all results will be returned.

    Args:  
        &nbsp;&nbsp;team: The country code according to IOC such as
        USA, ESP, AUS, etc.

    Returns:  
        &nbsp;&nbsp;A dataframe of match results.    
    """
    csvfn = './data/worldcup/2023/championship/worldcup_2023.csv'
    df = pd.read_csv(csvfn)
    if team is None:
        df = df.sort_values(by=['DP', 'GI'], ascending=[True, True])
        return df.to_dict('records')

    df_left = df.loc[df['C1'].str.lower() == team.lower()]
    df_right = df.loc[df['C2'].str.lower() == team.lower()]
    df_all = pd.concat([df_left, df_right], ignore_index=True)

    if len(df_all) <= 0:
        raise HTTPException(
            status_code=404,
            detail=f"Team {team} is not found."
        )

    df_all = df_all.sort_values(by=['DP', 'GI'], ascending=[True, True])
    return df_all.to_dict('records')


@app.get("/worldcup/2023/qualifier")
async def wordcup_2023_qualifier(
    team: Optional[str] = None,
    zone: Optional[str] = None
) -> List[Dict]:
    """## Gets FIBA world cup 2023 qualifier game results by zone or by team.

    If team and zone are not specified, all results will be returned.

    Args:  
        &nbsp;&nbsp;team: The country code according to IOC such as USA, etc.  
        &nbsp;&nbsp;zone: The zone name [Africa, Americas, Asia and Europe].

    Returns:
        &nbsp;&nbsp;A dataframe of match results.    
    """
    csvfn = './data/worldcup/2023/qualifier/worldcup_2023_qualifier.csv'
    df = pd.read_csv(csvfn)
    if team is None:
        if zone is None:
            df = df.sort_values(by=['DP', 'GI'], ascending=[True, True])
            return df.to_dict('records')
        else:
            if not zone.lower() in ZONES:
                raise HTTPException(
                    status_code=404,
                    detail=f"The zone {zone} is not found. Available \
                             values are {ZONES}."
                )

            df_zone = df.loc[df['ZONE'].str.lower() == zone.lower()]
            df_zone = df_zone.sort_values(
                by=['DP', 'GI'],
                ascending=[True, True]
            )
            return df_zone.to_dict('records')
    else:
        df_left = df.loc[df['C1'].str.lower() == team.lower()]
        df_right = df.loc[df['C2'].str.lower() == team.lower()]
        df_all = pd.concat([df_left, df_right], ignore_index=True)

        if len(df_all) <= 0:
            raise HTTPException(
                status_code=404,
                detail=f"The team {team} is not found."
            )

        df_all = df_all.sort_values(by=['DP', 'GI'], ascending=[True, True])
        return df_all.to_dict('records')
