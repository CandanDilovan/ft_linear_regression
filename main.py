from test import trainer


def main():
    theta = [0, 0]
    while True:
        if theta[0] == 0 and theta[1] == 0:
            print("type TRAIN to train a model with a given dataset")
            debut = input()
            if debut == 'TRAIN':
                theta = trainer('data.csv')
            else:
                print('The price of the car is 0')
        else:
            print("enter the mileage of the car")
            km = input()
            print(type(km))
            if not km.isnumeric():
                print('please enter a round number')
            else:
                km = int(km)
                print(f'The price of the car is {predict_y(km, theta)}')


def predict_y(km: float, theta: list) -> float:
    """_summary_

    Args:
        km (float): mileage of the car
        line (dict): coordinate of the line

    Returns:
        float: return the predicted price
    """
    return (theta[1] * km) + theta[0]


if __name__ == "__main__":
    main()
