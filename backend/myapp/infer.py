import pandas as pd

class InferCSV():
    def __init__(self, csv_file, file_type):
      
        if file_type == 'csv':
            self.df = pd.read_csv(csv_file)
        elif file_type == 'xlsx':
            self.df = pd.read_excel(csv_file)
        else:
            raise TypeError("Only csv and Excel file types are allowed")

        self.infer_df = self.infer_and_convert_data_types()
        self.user_type = {
            'object': 'Text',
            'datetime64[ns]': 'Date',
            'int8': 'Integer (8 bit)',
            'category': 'Text'
        }
        

    def count_type(self, x):

        infer_type = 'string'

        try:
            x = int(x)
            infer_type = 'int'
        except ValueError:
            pass

        try:
            # condition for datetime format
            if len(x) >= 7 and x.count("/") == 2:
                x = pd.to_datetime(x)
                infer_type = 'date-time'

        except (ValueError, TypeError):
            pass
        return infer_type
    


    def infer_and_convert_data_types(self):
        
        df = self.df
        
        for col in df.columns:
            types = df[col].apply(self.count_type)
            types.name = "types"
            majority_type = types.value_counts(ascending=False).idxmax(axis=1)

            # remove the incorrect datetime format
            df = pd.concat([df, types], axis = 1)
            df = df.drop(df[(df['types'] != majority_type)].index)
            df = df.drop('types', axis=1)

            if majority_type == 'int':
                df[col] = df[col].astype('int8')

            elif majority_type == 'date-time':
                
                # remove incorrect datetime format
                df[col] = pd.to_datetime(df[col])

            # if majority_type == string
            else:
                if len(df[col].unique()) / len(df[col]) < 0.5: 
                    df[col] = pd.Categorical(df[col])

        return df

    def get_infer_types(self):
        dtypes = self.infer_df.dtypes.apply(lambda x: x.name).to_dict()
        for col_name, type_name in dtypes.items():
            if type_name in self.user_type:
                dtypes[col_name] = self.user_type[type_name]

        return dtypes

