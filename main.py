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
    userDataframe = pd.read_csv('Users.csv')
    print('Harsh',userDataframe)
    schema = DataFrameSchema(
        columns={
            "Name": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "Email": Column(
                pandas_dtype=PandasDtype.String,
                checks=[Check.str_matches(r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$')],
                nullable=False,
                allow_duplicates=False,
                coerce=False,
                required=True,
                regex=True,
            ),
            "PhoneNumber": Column(
                pandas_dtype=PandasDtype.String,
                checks=[Check.str_length(min_value=10,max_value =10)],
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "Password": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "Role": Column(
                pandas_dtype=PandasDtype.String,
                checks=[
                    Check.isin(['superadmin','admin','dataEntry','manager',])
                ],
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "EmployeeId": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=False,
                coerce=False,
                required=True,
                regex=False,
            ),
            "LastLoggedIn": Column(
                pandas_dtype=PandasDtype.DateTime,
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
