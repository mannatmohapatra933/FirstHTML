import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [
            list(np.mean(arr, axis=0)),
            list(np.mean(arr, axis=1)),
            np.mean(arr.flatten())
        ],
        'variance': [
            list(np.var(arr, axis=0)),
            list(np.var(arr, axis=1)),
            np.var(arr.flatten())
        ],
        'standard deviation': [
            list(np.std(arr, axis=0)),
            list(np.std(arr, axis=1)),
            np.std(arr.flatten())
        ],
        'max': [
            list(np.max(arr, axis=0)),
            list(np.max(arr, axis=1)),
            np.max(arr.flatten())
        ],
        'min': [
            list(np.min(arr, axis=0)),
            list(np.min(arr, axis=1)),
            np.min(arr.flatten())
        ],
        'sum': [
            list(np.sum(arr, axis=0)),
            list(np.sum(arr, axis=1)),
            np.sum(arr.flatten())
        ]
    }

    return calculations