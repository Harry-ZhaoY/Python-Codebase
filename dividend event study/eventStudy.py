import pandas as pd

# import data
univ = pd.read_csv("inputs/univ.csv")
const = pd.read_csv("inputs/const.csv")
# rewrite NaNs in SP500 constitudents
const.loc[const["thru"].isnull(), ["thru"]] = 20190101
# merge the data
const = const.rename(columns = {"co_tic":"TICKER"})
univ_500 = pd.merge(univ, const, on = "TICKER")
# select dates
univ_500 = univ_500.loc[(univ_500["date"] >= univ_500["from"]) & (univ_500["date"] <= univ_500["thru"])]

# clean RETX
univ_500["RETX"] = univ_500["RETX"].convert_objects(convert_numeric=True)
univ_500 = univ_500.dropna(subset = ["RETX"])
# calculate excess return
univ_500["xRetx"] = univ_500["RETX"] - univ_500["sprtrn"]


# write 41 days of returns on one row
xRetxDt = univ_500.sort_values(["TICKER", "date"], ascending = [1,1])
for i in range(20):
    xRetxDt["lag"+str(i+1)] = xRetxDt["xRetx"].groupby([xRetxDt["TICKER"]]).shift(i+1)
    xRetxDt["lead"+str(i+1)] = xRetxDt["xRetx"].groupby([xRetxDt["TICKER"]]).shift(-(i+1))
# select data on ex-dividend date
xRetxDt_exd = xRetxDt.loc[pd.notna(xRetxDt["DIVAMT"]) & pd.notna(xRetxDt["lag20"]) & pd.notna(xRetxDt["lead20"])]
xRetxDt_exd = xRetxDt_exd.loc[:,["lag"+str(i) for i in range(20, 0, -1)] + ["xRetx"] + ["lead"+str(i+1) for i in range(20)]]
# compute mean return each day
xRetx_avg = xRetxDt_exd.mean(axis=0)

# plot
xRetx_avg.index = list(range(-20,0)) + [0] + list(range(1, 21))
xRetx_avg.plot()