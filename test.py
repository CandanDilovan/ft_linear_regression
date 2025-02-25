from ft_load_csv import ft_load
import matplotlib.pyplot as plt
import pandas as pd


def trainer(path: str) -> list:
    try:
        df = ft_load(path)
        line = {
            'slope': 1.0,
            'xy1': [((0 - df["km"].min()) / (df["km"].max() - df["km"].min())),
                    ((8000 - df["price"].min())
                     / (df["price"].max() - df["price"].min()))],

            'norm_km': ((df["km"] - df["km"].min())
                        / (df["km"].max() - df["km"].min())),

            'norm_price': ((df["price"] - df["price"].min())
                           / (df["price"].max() - df["price"].min()))
        }
        learning_test(df, line)
        denorm(df, line)
        plt.axline(line["xy1"], slope=line["slope"], color='r', linestyle='-')
        plt.xlabel('km')
        plt.ylabel('price')
        plt.xlim(0, 250000)
        plt.gca().invert_yaxis()
        plt.scatter(df["km"], df["price"])
        plt.show()
    except (KeyboardInterrupt, AssertionError) as msg:
        print(msg)
    return [line['xy1'][1], line['slope']]


def denorm(pd: pd.DataFrame, line: dict) -> dict:
    line["slope"] = line["slope"] * ((pd["price"].max() - pd["price"].min())
                                     / (pd["km"].max() - pd["km"].min()))

    line["xy1"][0] = 0

    line["xy1"][1] = line["xy1"][1] * ((pd["price"].max() - pd["price"].min())
                                       + pd["price"].min())


def learning_test(df: pd.DataFrame, line: dict):
    learn_rate = -0.1
    for x in range(10000):
        ssr = sum_squared_residuals(df, line)
        adaptative_rate = learn_rate / (1 + 0.1 * x)
        if ((abs(ssr["intercept"] * adaptative_rate) < 0.001)
           and abs(ssr["slope"] * adaptative_rate) < 0.001):
            break
        if abs(ssr["intercept"] * adaptative_rate) > 0.001:
            line['xy1'][1] += ssr["intercept"] * adaptative_rate
        if abs(ssr["slope"] * adaptative_rate) > 0.001:
            line['slope'] += (ssr["slope"] * adaptative_rate)


def predict_y(km: float, line: dict) -> float:
    """_summary_

    Args:
        km (float): mileage of the car
        line (dict): coordinate of the line

    Returns:
        float: return the predicted price
    """
    y_itercept = line["xy1"][1] - (line['slope'] * line["xy1"][0])
    point = (line['slope'] * km) + y_itercept
    return point


def derivative(price: float, intercept: float, slope: float,
               km: float) -> float:
    """_summary_

    Args:
        price (float): y axis of the graph
        intercept (float): the intercept (point were the line meet
                            the 0 on the x axis)
        slope (float): the degree of rotation of the line
        km (float): the x axis of the graph

    Returns:
        float: the derivative
    """
    return -2 * (price - (intercept + (slope * km)))


def slope(price: float, intercept: float, slope: float,
          km: float) -> float:
    """_summary_

    Args:
        price (float): y axis of the graph
        intercept (float): the intercept (point were the line meet
                            the 0 on the x axis)
        slope (float): the degree of rotation of the line
        km (float): the x axis of the graph

    Returns:
        float: the derivative
    """
    return -2 * km * (price - (intercept + (slope * km)))


def sum_squared_residuals(df: pd.DataFrame, line: dict):
    ssr = {
        'intercept': 0.0,
        'slope': 0.0
    }
    y_itercept = line["xy1"][1] - (line['slope'] * line["xy1"][0])
    for x in range(df["km"].size):
        ssr["intercept"] += derivative(line['norm_price'][x], y_itercept,
                                       line['slope'], line['norm_km'][x])

        ssr["slope"] += (slope(line['norm_price'][x], y_itercept,
                               line['slope'], line['norm_km'][x]))
    return ssr
