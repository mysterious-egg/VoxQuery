import pandas as pd


def process_csv(uploaded_file):

    try:

        df = pd.read_csv(uploaded_file)

        result = {

            "dataframe": df,

            "columns": list(df.columns),

            "shape": df.shape,

            "preview": df.head(3),

            "dtypes": {
                col: str(dtype)
                for col, dtype in df.dtypes.items()
            },

            "missing": {
                col: int(count)
                for col, count in df.isnull().sum().items()
            }
        }

        print("DEBUG:")
        print(result.keys())

        return result


    except Exception as e:

        return {
            "error": str(e)
        }