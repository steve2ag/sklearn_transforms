from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
class my_Encoder(BaseEstimator, TransformerMixin):
    def __init__(self, columns = 'koi_pdisposition'):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()
        wt = {'CANDIDATE':1, 'FALSE POSITIVE':2}
        data['koi_pdisposition'] = data['koi_pdisposition'].map(wt)
        return data.drop(self.columns, axis='columns')
