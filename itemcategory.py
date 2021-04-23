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
    userDataframe = pd.read_csv('itemcategory.csv')
    print('Almondz',userDataframe)
    schema = DataFrameSchema(
        columns={
            "name": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "tags": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "note": Column(
                pandas_dtype=PandasDtype.String,
                checks=[Check.str_length(min_value=10,max_value =100
                                         )],
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "quantity": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=False,
                coerce=False,
                required=True,
                regex=False,
            ),
            "description": Column(
                pandas_dtype=PandasDtype.String,
                checks=[Check.str_length(min_value=10,max_value =100)],
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "itemType": Column(
                pandas_dtype=PandasDtype.String,
                checks=[
                    Check.isin(['goods','service'])
                ],
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
