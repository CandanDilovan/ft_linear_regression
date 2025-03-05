from ft_load_csv import ft_load


def main():
    try:
        theta = ft_load("trained_data.csv")
        if theta is None:
            theta = [0, 0]
        else:
            theta = theta.columns.tolist()
        while True:
            print("enter the mileage of the car")
            km = input()
            if not km.isnumeric() or int(km) < 0:
                print('please enter a round positive number')
            else:
                km = int(km)
                print(f'The price of the car is {predict_y(km, theta)}')
                break
    except (KeyboardInterrupt, AssertionError, InterruptedError) as msg:
        print(msg)


def predict_y(km: float, theta: list) -> float:
    """_summary_

    Args:
        km (float): mileage of the car
        line (dict): coordinate of the line

    Returns:
        float: return the predicted price
    """
    return (float(theta[1]) * km) + float(theta[0])


if __name__ == "__main__":
    main()
