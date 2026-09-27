import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class FeatureEngineer(BaseEstimator, TransformerMixin):
    """Create derived agronomic features from raw inputs."""

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_df = X.copy()

        farm_size = X_df["Farm_Size_ha"].replace(0, np.nan)
        soil_ph = X_df["Soil_pH"].replace(0, np.nan)

        X_df["Rainfall_Temperature_Index"] = X_df["Rainfall_mm"] * X_df["Temperature_C"]
        X_df["Input_Intensity"] = X_df["Fertilizer_kg_per_ha"] + X_df["Pesticide_kg_per_ha"]
        X_df["Fertilizer_per_Farm_Size"] = X_df["Fertilizer_kg_per_ha"] / farm_size
        X_df["Fertilizer_per_pH"] = X_df["Fertilizer_kg_per_ha"] / soil_ph

        return X_df


class QuantileCapper(BaseEstimator, TransformerMixin):
    """Cap selected numeric columns using train-fitted quantiles."""

    def __init__(self, columns, lower=0.01, upper=0.99):
        self.columns = columns
        self.lower = lower
        self.upper = upper

    def fit(self, X, y=None):
        X_df = X.copy()
        self.bounds_ = {}
        for col in self.columns:
            self.bounds_[col] = (
                X_df[col].quantile(self.lower),
                X_df[col].quantile(self.upper),
            )
        return self

    def transform(self, X):
        X_df = X.copy()
        for col, (lb, ub) in self.bounds_.items():
            X_df[col] = X_df[col].clip(lower=lb, upper=ub)
        return X_df
