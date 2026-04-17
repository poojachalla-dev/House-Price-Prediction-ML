from load_dataset import df

features = ['GrLivArea', 'FullBath', 'BedroomAbvGr']
X = df[features]

y = df["SalePrice"]