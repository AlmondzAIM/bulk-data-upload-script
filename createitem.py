from pandas import Timestamp
from pandera import (
     DataFrameSchema,
     Column,
     Check,
     Index,
     MultiIndex,
     PandasDtype,)

# import pandas lib as pd
import pandas as pd
  
# read by default 1st sheet of an excel file
def main():
    userDataframe = pd.read_csv('createitem.csv')
    print('Almondz',userDataframe)
    schema = DataFrameSchema(
        columns={
            "id": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "name": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "categoryId": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "description": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "itemStatus": Column(
                pandas_dtype=PandasDtype.String,
                checks=[
                    Check.isin(['assign','unassigned'])
                ],
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "userId": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "price": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=False,
                coerce=False,
                required=True,
                regex=False,
            ),
            "unitType": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "sku": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,

            ),
            "vendorId": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
        },
        index=Index(
            pandas_dtype=PandasDtype.String,
            nullable=False,
            coerce=False,
            name=None,
        ),
        coerce=True,
        strict=False,
        name=None,
    )

    #print(schema)
    schema.validate(userDataframe)

main()
