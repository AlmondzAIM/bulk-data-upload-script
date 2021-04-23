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
    userDataframe = pd.read_csv('createvendor.csv')
    print('Almondz',userDataframe)
    schema = DataFrameSchema(
        columns={
            "organizationName": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "email": Column(
                pandas_dtype=PandasDtype.String,
                checks=[Check.str_matches(r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$')],
                nullable=False,
                allow_duplicates=False,
                coerce=False,
                required=True,
                regex=True,
            ),
            "phoneNumber": Column(
                pandas_dtype=PandasDtype.String,
                checks=[Check.str_length(min_value=10,max_value =10)],
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
                
            "vendorStatus": Column(
                pandas_dtype=PandasDtype.String,
                checks=[
                    Check.isin(['active','inactive','blocked'])
                ],
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "cinNo": Column(
                pandas_dtype=PandasDtype.String,
                checks=[Check.str_length(min_value=21,max_value =21)],
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "gstNo": Column(
                pandas_dtype=PandasDtype.String,
                checks=[Check.str_length(min_value=15,max_value =15)],
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "websiteUrl": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=False,
                coerce=False,
                required=True,
                regex=False,
            ),
            "address": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,

            ),
            "country": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=False,
                coerce=False,
                required=True,
                regex=False,
            ),
            "city": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=False,
                coerce=False,
                required=True,
                regex=False,
            ),
            "state": Column(
                pandas_dtype=PandasDtype.String,
                nullable=False,
                allow_duplicates=False,
                coerce=False,
                required=True,
                regex=False,
            ),
            "pincode": Column(
                pandas_dtype=PandasDtype.String,
                checks=[Check.str_length(min_value=6,max_value =6)],
                nullable=False,
                allow_duplicates=False,
                coerce=False,
                required=True,
                regex=False,
            ),
            
            "alternatePhoneNumber": Column(
                pandas_dtype=PandasDtype.String,
                checks=[Check.str_length(min_value=10,max_value =10)],
                nullable=False,
                allow_duplicates=True,
                coerce=False,
                required=True,
                regex=False,
            ),
            "alternateEmail": Column(
                pandas_dtype=PandasDtype.String,
                checks=[Check.str_matches(r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$')],
                nullable=False,
                allow_duplicates=False,
                coerce=False,
                required=True,
                regex=True,
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
