import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    array = np.array(list).reshape(3, 3)

    mean = [array.mean(axis=0).tolist(), array.mean(axis=1).tolist(), float(array.mean())]
    variance = [array.var(axis=0).tolist(), array.var(axis=1).tolist(), float(array.var())]
    standard_deviation = [array.std(axis=0).tolist(), array.std(axis=1).tolist(), float(array.std())]
    maximum = [array.max(axis=0).tolist(), array.max(axis=1).tolist(), int(array.max())]
    minimum = [array.min(axis=0).tolist(), array.min(axis=1).tolist(), int(array.min())]
    total_sum = [array.sum(axis=0).tolist(), array.sum(axis=1).tolist(), int(array.sum())]

    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': maximum,
        'min': minimum,
        'sum': total_sum
    }

    return calculations
