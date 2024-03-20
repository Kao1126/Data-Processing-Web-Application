# %%
import pandas as pd

def count_type(x):
    
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
    


def infer_and_convert_data_types(df):
    df = pd.read_csv('sample_data.csv')
    for col in df.columns:
        
        
        types = df[col].apply(count_type)
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

            if len(df[col].unique()) / len(df[col]) < 0.5:  # Example threshold for categorization
                df[col] = pd.Categorical(df[col])
            
    return df




csv_file = 'sample_data.csv'
df = infer_and_convert_data_types(csv_file)

# print(df["Name"].apply(type).value_counts())

# print('---')
print("\nData types after inference:")
print(df.dtypes)

