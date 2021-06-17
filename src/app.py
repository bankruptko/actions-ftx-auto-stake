import os
import ftx
from pprint import pprint


def stake(self: ftx.FtxClient, coin: str, size: float) -> dict:
    return self._post("srm_stakes/stakes", params={"coin": coin, "size": size})


setattr(ftx.FtxClient, stake.__name__, stake)
setattr(
    ftx.FtxClient.stake,
    ftx.FtxClient.authentication_required.__name__,
    ftx.FtxClient.authentication_required,
)

api_key = os.getenv("FTX_API_KEY")
api_secret = os.getenv("FTX_API_SECRET")
stake_symbols = os.getenv(
    "FTX_STAKE_SYMBOLS",
    ["SRM", "SRM_LOCKED", "MSRM", "MSRM_LOCKED", "SOL", "UBXT", "FIDA", "RAY"],
)

if isinstance(stake_symbols, str):
    stake_symbols = stake_symbols.split(",")

client = ftx.FtxClient(api_key=api_key, api_secret=api_secret)

balances = client.get_balances()

for s in stake_symbols:
    b = next(filter(lambda b: b["coin"] == s, balances), None)
    if b is None or b["free"] == 0:
        continue
    print(f"{b['coin']} - {b['free']}")
    res = client.stake(b["coin"], b["free"])
    print(f"{b['coin']} Staked.")
    pprint(res)
