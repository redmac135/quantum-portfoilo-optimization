from api import get_stock_data
from datetime import datetime, timedelta


def get_historical_stock_prices(ticker: str) -> list:
    data = get_stock_data(ticker)
    # should convert the dictionary from 'data' into a list of prices
    datelist = list(data.get("Time Series (Daily)").keys())[:300]
    time_series_daily = data.get("Time Series (Daily)")
    prices = []
    for date in datelist:
        if (
            "1. open" in time_series_daily[date]
            and "4. close" in time_series_daily[date]
        ):
            prices.append(
                float(time_series_daily[date]["1. open"]),
            )
        else:
            raise ValueError("Data is missing required fields")
    return prices


print(get_historical_stock_prices("TSLA"))


def calculate_covariance(list1: list, list2: list) -> float:
    if not len(list1) == len(list2):
        raise ValueError("Lists must be the same length")

    n = len(list1)

    # Calculate the mean of each list
    mean_list1 = sum(list1) / n
    mean_list2 = sum(list2) / n

    # Initialize the covariance sum
    cov_sum = 0.0

    # Calculate the covariance
    for i in range(n):
        cov_sum += (list1[i] - mean_list1) * (list2[i] - mean_list2)

    covariance = cov_sum / (n - 1)

    return covariance
