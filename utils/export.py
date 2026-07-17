import pandas as pd

def export_csv(data, filename="outputs/results.csv"):

    df = pd.DataFrame(data)

    df.to_csv(filename, index=False)

    return filename